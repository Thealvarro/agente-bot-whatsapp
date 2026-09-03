# Cómo se construye — guía técnica

**Esto es para ti, el agente. El usuario nunca ve nada de este archivo.**

Se carga en `/bot-probar`, antes de escribir la primera línea de código.

⚠️ **Por qué existe este archivo:** la API de WhatsApp de Zernio se lanzó en junio de 2026. **No
está en lo que sabes de memoria.** Si improvisas endpoints, vas a inventar rutas que no existen —
y el usuario, que no programa, no tiene cómo darse cuenta. Va a ver "no funciona" sin entender por
qué.

**Antes de escribir código, lee la documentación oficial:** `docs.zernio.com` y
`zernio.com/openapi.yaml`. Lo de acá abajo es correcto al cierre de la investigación, pero
verifica lo que uses.

---

# 1. La decisión que ordena todo el diseño

**Una interfaz de canal propia, con dos implementaciones intercambiables.**

```
                 ┌──────────────┐
   simulador ───▶│              │
                 │  interfaz    │──▶  el bot (cerebro, memoria, acciones)
   Zernio    ───▶│    Canal     │
                 └──────────────┘
```

El bot **nunca** habla con Zernio directamente. Habla con `Canal`, y `Canal` tiene dos
implementaciones: `CanalDemo` (el simulador) y `CanalZernio` (WhatsApp real).

**Esto no es una abstracción especulativa. Es lo que hace posible el producto entero:**

1. **Permite probar antes de conectar** — la promesa central del sistema. El simulador y WhatsApp
   entran por la misma puerta, así que lo que probaste es lo que va a correr.
2. **Evita el lock-in.** Si Zernio sube precios, cae o cambia condiciones, se escribe otra
   implementación y el bot no se toca. Es un proveedor joven: la vertical de WhatsApp tiene
   pocos meses y no hay SLA contractual.

La interfaz mínima:

```ts
interface Canal {
  enviar(conversacionId: string, texto: string): Promise<void>
  marcarLeido(conversacionId: string): Promise<void>
  escribiendo(conversacionId: string): Promise<void>
  ventanaAbierta(conversacionId: string): Promise<boolean>
}
```

Todo lo demás —firmas, reintentos, formatos— vive dentro de cada implementación.

---

# 2. Stack

| Pieza | Elección | Por qué |
|---|---|---|
| Framework | Next.js (App Router) | Necesitas rutas de servidor y una pantalla para el simulador y la bandeja |
| Alojamiento | Vercel | Hobby si el bot es del propio usuario; **Pro si le cobra a un cliente** (Hobby prohíbe uso comercial) |
| Modelo | **Claude Haiku 4.5** | Ver `herramientas-costos.md` B4. No actives prompt caching |
| Base de datos | Neon o Supabase, **una sola** | Región **São Paulo**, decisión irreversible |
| Mensajería | **HTTP directo a Zernio** | Ver abajo |

## Por qué HTTP directo y no el Chat SDK

Existe `@zernio/chat-sdk-adapter` para el Chat SDK de Vercel, y ahorra algo de código repetido.
**No lo uses de entrada.** Tiene muy poca adopción, es una capa joven sobre otra capa joven, y
cuando algo falle vas a estar depurando el adaptador en vez del bot — con un usuario que no puede
ayudarte a diagnosticar.

La API REST de Zernio está bien documentada y es directa. Menos capas, menos sorpresas.

---

# 3. Estructura del proyecto

```
app/
  api/webhook/zernio/route.ts   La puerta. Valida, confirma y encola
  demo/page.tsx                 El simulador que se ve como WhatsApp
  bandeja/page.tsx              Aprobar, corregir o rechazar borradores
  api/apagar/route.ts           El interruptor

lib/
  canal/
    tipos.ts                    La interfaz Canal
    demo.ts                     CanalDemo
    zernio.ts                   CanalZernio
  bot/
    cerebro.ts                  La llamada al modelo
    prompt.ts                   Arma el system prompt desde la Ficha del Bot
    acciones.ts                 Las acciones, con validación dura
  datos/
    conversaciones.ts
    contactos.ts                Incluye bloqueado y baja de marketing
  guardas/
    firma.ts                    Verificación HMAC
    idempotencia.ts
    limites.ts                  Por teléfono y por conversación
    gasto.ts                    Tope diario que corta
```

---

# 4. Zernio — lo que necesitas saber

Base: `https://zernio.com/api/v1` · Auth: `Authorization: Bearer sk_...`

Variables: `ZERNIO_API_KEY`, `ZERNIO_WEBHOOK_SECRET`

## 4.1 · Recibir mensajes

Evento principal: **`message.received`**. Otros útiles: `message.delivered`, `message.read`,
`message.failed`, `conversation.started`, `account.disconnected`.

**Verificación de firma:**

- Header `X-Zernio-Signature` (también emite el alias antiguo `X-Late-Signature` — Zernio es el
  rebrand de "Late")
- HMAC-SHA256 del **cuerpo crudo**, secreto como clave, hexadecimal minúscula

```ts
const raw = await req.text()            // el cuerpo CRUDO, sin parsear
const esperada = crypto.createHmac('sha256', secret).update(raw).digest('hex')
const recibida = req.headers.get('x-zernio-signature') ?? ''

const a = Buffer.from(esperada, 'hex')
const b = Buffer.from(recibida, 'hex')
if (a.length !== b.length || !crypto.timingSafeEqual(a, b)) {
  return new Response('no', { status: 401 })
}
```

⚠️ **Dos debilidades del esquema que compensas tú:**

1. **No hay marca de tiempo firmada → sin protección contra reenvío.** Un mensaje capturado se
   puede reenviar indefinidamente. **Obligatorio:** deduplicar por `X-Zernio-Event-Id` (o el `id`
   del cuerpo) con expiración, y rechazar eventos con `createdAt` viejo.
2. **El ejemplo oficial de Node compara con `!==`**, que no es seguro ante ataques de tiempo. Usa
   `timingSafeEqual`, como arriba.

**Plazo de respuesta: 2xx en 5 segundos o menos.** Una llamada al modelo demora entre 3 y 10.

```ts
// confirmar PRIMERO, procesar después
await encolar(evento)
return new Response('ok', { status: 200 })
```

Si te pasas del plazo: **7 reintentos** con espera creciente (inmediato → 10s → 1m40s → 16m40s →
2h46m → 24h → 24h) y después cola de descarte. En la práctica: el cliente recibe la misma
respuesta varias veces y tú pagas cada llamada al modelo **y cada mensaje de WhatsApp**.

Semántica de **al-menos-una-vez**: la deduplicación no es opcional.

## 4.2 · Enviar mensajes

```
POST /v1/inbox/conversations/{conversationId}/messages
{ "accountId": "...", "message": "hola" }
```

Campos útiles: `attachmentUrl` + `attachmentType`, `buttons` (**máximo 3**), `quickReplies`
(máximo 13), `replyTo`, `category: "utility"`.

**Idempotencia:** header `Idempotency-Key`, retenido 24 horas. Misma clave + mismo cuerpo →
repite la respuesta. ⚠️ **Solo se guardan las respuestas 2xx**: ante un error del servidor o un
tiempo agotado la clave se libera, así que un reintento ciego **puede duplicar el mensaje**.

**Iniciar conversación o reabrir fuera de la ventana** (requiere plantilla aprobada):

```
POST /v1/inbox/conversations
{ "participantId": "+56912345678", "templateName": "...", "templateLanguage": "es",
  "templateParams": [...] }
```

## 4.3 · Leer

```
GET /v1/inbox/conversations/{id}/messages?accountId=X&limit=100&cursor=...&sortOrder=asc
GET /v1/inbox/conversations?platform=whatsapp&accountId=X
```

`limit` máximo 100. El cursor es **opaco**: si lo alteras, error 400.

## 4.4 · Trampas de la API

| Cosa | Detalle |
|---|---|
| **`conversationId` es opaco** | Doc textual: *"do not assume a fixed format"*. Guárdalo y devuélvelo tal cual |
| **`sentVia` puede venir vacío** | Vacío = **desconocido**, no "lo mandó un humano". Los mensajes entrantes y los anteriores a agosto de 2026 vienen así. Si lo usas para no responderte a ti mismo, trata el vacío como "no sé" |
| **Ventana de 24 h** | Zernio **no expone** cuándo vence. Calcúlala tú desde la fecha del último mensaje entrante |
| **Mensajes interactivos** | Todos son de sesión: solo dentro de la ventana |
| **Ritmo por destinatario** | ~10 mensajes por minuto a la misma persona. Más rápido da error `131056`. Paraleliza entre destinatarios, nunca contra uno |
| **Rate limit de la API** | 60 req/min con el plan gratuito (2 cuentas), 600 con 3 o más. Lee los headers `X-RateLimit-*` en vez de asumir |

**Errores que vas a ver:** `131026` ventana cerrada · `131021` número inválido o sin WhatsApp ·
`131047` límite de ritmo · `132001` plantilla no encontrada · `131031` cuenta bloqueada por Meta ·
`133005` PIN de verificación en dos pasos.

**Media:** imagen 5 MB (JPEG/PNG) · video 16 MB (MP4) · documento 100 MB · audio 16 MB. Nota de
voz real requiere `.ogg` OPUS mono.

🚨 **Verificar antes de construir sobre el plan gratuito:** la documentación de Zernio se
contradice sobre si los endpoints de `inbox` —los que necesita un bot— están disponibles sin
plan de pago. Ver `herramientas-costos.md` B2. **Pruébalo con una cuenta real antes de prometer
que el plan gratis alcanza.**

---

# 5. El simulador

`CanalDemo` guarda los mensajes en la misma base que usaría WhatsApp y los sirve a
`app/demo/page.tsx`. **Sin credenciales, sin número, sin trámite.**

Requisitos, que salen de las 14 pruebas:

- **Se ve como WhatsApp.** Burbujas, horas, indicador de escribiendo. Si parece un panel técnico,
  el usuario no puede opinar de lo que ve.
- **Dos clientes simultáneos** en la misma pantalla — la prueba 11 los necesita y **no** un
  segundo teléfono.
- **Botones para mandar audio, foto, sticker y ubicación**, aunque sean simulados. La prueba 9 los
  usa.
- **Contador de costo en vivo.** Cada respuesta suma lo que costaría en WhatsApp más el modelo. Es
  la mejor explicación posible de por qué el bot debe responder corto.
- **Botón de apagado**, en el mismo lugar donde va a estar en producción. La prueba 13 lo exige.

---

# 6. El cerebro

**El system prompt se arma desde la Ficha del Bot**, no se escribe a mano. Si la ficha cambia, el
prompt cambia.

Estructura obligatoria:

```
[SISTEMA]
  Identidad y tono          ← de la Ficha
  Qué hace / qué NO hace    ← los límites duros de la pregunta 9
  Dominio acotado           ← exigencia de Meta
  Declaración de IA         ← exigencia de Anthropic
  Nada de consejo de salud  ← exigencia de Anthropic
  Respuestas cortas         ← cada mensaje cuesta
  Datos duros: precios, horarios, servicios

[USUARIO]
  <mensaje_cliente>...</mensaje_cliente>   ← delimitado y marcado como no confiable
```

⚠️ **Nunca concatenes el mensaje del cliente con las instrucciones.** Va en su propio bloque,
marcado explícitamente como contenido no confiable, con la instrucción de que es información y
jamás una orden que cambie las reglas.

**Las acciones se validan en código, no en el prompt.** El modelo propone, el código verifica
contra la fuente de verdad, y recién ahí se ejecuta:

```ts
// El modelo pide agendar el jueves a las 11
const libre = await calendario.estaLibre(fecha)   // ← la verdad está acá
if (!libre) return sugerirOtras()
```

Un precio que no está en la lista **no existe**, por más que el modelo lo proponga.

---

# 7. Orden de construcción

No lo cambies. Cada pieza se verifica antes de montar la siguiente.

| # | Pieza | Listo cuando |
|---|---|---|
| 1 | **La puerta** | Un evento válido queda registrado; uno sin firma se rechaza con 401 |
| 2 | **La memoria** | Dos conversaciones simultáneas no se cruzan |
| 3 | **El cerebro** | Responde el precio exacto de la lista, nunca uno inventado |
| 4 | **Las acciones** | Solo ofrece horas que existen de verdad |
| 5 | **Los controles** | El apagado corta de inmediato; el tope de gasto **corta**, no solo avisa |
| 6 | **El simulador** | El usuario conversa con su bot desde su pantalla |

Construir el cerebro primero es el error clásico: si los mensajes no llegan ni se guardan, depuras
a ciegas.

---

# 8. Antes de dar la construcción por terminada

- [ ] Los **51 ítems** de `seguridad.md` Parte B, verificados contra el sistema real
- [ ] Base de datos en **São Paulo** — irreversible, se decide al crear
- [ ] Aislamiento por cliente con seguridad a nivel de fila, si atiende a más de un negocio
- [ ] `.env` fuera del control de versiones **antes** del primer guardado
- [ ] Ninguna credencial en el código, en logs ni en respuestas
- [ ] `CanalDemo` y `CanalZernio` implementan la **misma** interfaz — si divergen, lo que probaste
      no es lo que va a correr
