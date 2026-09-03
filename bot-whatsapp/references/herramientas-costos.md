# Herramientas y costos

**Objetivo:** que el usuario entienda qué cuentas necesita y **cuánto le va a costar de verdad**,
antes de que se construya nada.

**Regla de la fase:** nunca digas "es gratis". Casi nada lo es, y lo que era gratis dejó de
serlo. Muestra la tabla y deja que él decida con el número a la vista.

Dos partes: **A** es lo que le explicas al usuario. **B** son los datos duros, que él no ve.

---

# 🚨 LO PRIMERO: el cambio de reglas del 1 de octubre de 2026

**Esto lo tienes que saber tú antes de abrir la boca en esta fase.**

Hasta el 30 de septiembre de 2026, responderle a un cliente por WhatsApp era gratis. Meta lo
cambió:

> *"Effective October 1, 2026, Meta will charge for service messages, which have not been charged
> since November 2024."*

**Cada respuesta del bot pasa a costar plata.** Para Chile, alrededor de **$0,0200 USD por
mensaje** (~19 pesos).

## Y hay una fecha límite dura

> *"For any Solution Provider or directly-integrated business that does not have a payment method
> on file by September 30, 2026, Meta will stop delivering service messages as of when they become
> charged on October 1, 2026."*

⚠️ **Sin método de pago registrado en la cuenta de WhatsApp Business al 30 de septiembre, el bot
deja de entregar respuestas el 1 de octubre.** El cliente escribe, el bot procesa, y la respuesta
nunca llega.

**Acción obligatoria en `/bot-conectar`:** verificar que hay método de pago registrado. Si el usuario
ya tiene bots andando de antes, **avísale hoy mismo**, aunque estén fuera de este proyecto.

## Lo que esto cambia en el diseño

Antes, el costo dominante era la IA. Ahora es WhatsApp, por lejos:

| Bot de N mensajes por conversación | WhatsApp (500 conv) | IA (Haiku) | Proporción |
|---|---|---|---|
| 15 mensajes | $150,00 | $21,95 | **7× más caro WhatsApp** |
| 8 mensajes | $80,00 | $21,95 | 3,6× |
| 5 mensajes | $50,00 | $21,95 | 2,3× |

**La palanca económica más grande ya no es el modelo ni el caching: es que el bot conteste en
menos mensajes.** Pasar de 15 a 5 mensajes por conversación ahorra ~93.000 CLP al mes por cliente.

**Instrucción concreta para el guion de `/bot-planificar` y el sistema de `/bot-probar`:**
- Respuestas densas, no picadas en varios mensajes
- Agrupar preguntas en una sola respuesta
- Nunca mandar "ok", "perfecto", ni acuses de recibo sueltos
- Nunca dividir una idea en dos mensajes

Esto no es solo ahorro: también es mejor experiencia. A nadie le gusta que le llenen el WhatsApp
de globitos.

---

# ⚠️ Antes de mostrar un solo número: la moneda y el país

**Las cifras de este archivo están en pesos chilenos como ejemplo trabajado.** No las copies tal
cual para un negocio de otro país.

**Lo que tienes que hacer:**

1. **Busca la tarifa de su país** en el anexo local (`legal-chile.md` para Chile) o en el rate
   card oficial de Meta. **Varían más de 12 veces** entre países: el marketing va de USD 0,0125 en
   Colombia a USD 0,1597 en Países Bajos.
2. **Convierte a su moneda** y muéstrale solo esa. Nunca le hables en dólares a alguien que piensa
   en pesos, soles o euros.
3. **Ajusta al volumen real** que dio en la pregunta 4b, no a los 500 del ejemplo.

**Los costos que NO cambian por país:** el modelo (USD 1 por millón de tokens de entrada con Haiku
4.5) y el alojamiento (USD 20/mes el plan de pago). Esos se convierten y ya.

**El costo que sí cambia, y es el dominante:** los mensajes de WhatsApp.

⚠️ **Si no encuentras la tarifa de su país, dilo.** Es preferible decir *"déjame confirmar el
precio exacto de los mensajes en tu país antes de darte un número"* que inventar una cifra que
después no se cumple.

---

# PARTE A — Lo que le explicas al usuario

## Las cuentas que va a necesitar

Cuatro cosas, cada una con una frase. Nada de arquitectura.

| Cuenta | Para qué sirve, en una frase |
|---|---|
| **WhatsApp del negocio** | Para recibir y mandar mensajes |
| **El cerebro** | Entiende lo que le escriben y redacta las respuestas |
| **Donde vive** | Un computador arrendado que está prendido siempre, para que tu asistente nunca duerma. **No es el tuyo** — el tuyo lo apagas cuando quieras |
| **La memoria** | Donde se guardan las conversaciones y los contactos |

Y si en `/bot-planificar` dijo que quiere agendar:

| **La agenda** | Para ver tus horas libres y anotar las citas |

---

## La tabla de costos

⚠️ **Muéstrale la columna de octubre en adelante, no la de antes.** Si le muestras el costo
actual, en un mes te va a reclamar con razón.

### Negocio chico — 150 conversaciones al mes, bot que responde corto

| Concepto | Costo mensual |
|---|---|
| Mensajes de WhatsApp | ~$14.000 |
| El cerebro del asistente | ~$1.400 |
| Donde vive | $0 – $19.000 |
| La memoria | $0 |
| La agenda | $0 |
| **Total** | **~$15.000 – $34.000** |

### Negocio con harto movimiento — 500 conversaciones al mes

| Concepto | Costo mensual |
|---|---|
| Mensajes de WhatsApp | ~$47.000 |
| El cerebro del asistente | ~$4.600 |
| Donde vive | $0 – $19.000 |
| La memoria | $0 |
| **Total** | **~$52.000 – $71.000** |

*Ambas con un asistente que responde en pocos mensajes. Si responde picado, el costo de WhatsApp
se puede triplicar.*

### Lo que le tienes que explicar de estos números

**1. Lo que cuesta es cada mensaje que manda el asistente, no cada cliente.**
Por eso un asistente que responde bien en 3 mensajes cuesta un tercio que uno que responde en 9.
No es una optimización técnica: es la diferencia entre que el negocio cierre o no.

**2. Mandar promociones es carísimo en Chile.**
Chile tiene la **tercera tarifa de marketing más cara del mundo**: **~$83 pesos por mensaje de
promoción**. Una promo a 500 contactos son **~$41.000**, más que todo el resto del mes junto.

Si quiere mandar promociones, se presupuesta aparte y se le muestra el número antes.

**3. Hay una puerta gratis que conviene usar.**
Si el cliente llega por un **anuncio de Facebook o Instagram con botón de WhatsApp**, se abre una
ventana de **72 horas donde todo es gratis**. Si el negocio ya pauta, canalizar el tráfico por ahí
es plata directa al bolsillo.

---

## El punto donde deja de ser gratis

⚠️ **Si el bot es para un cliente que te paga, el alojamiento no puede ser el plan gratis.**

Los términos prohíben el uso comercial en el plan gratuito, y "comercial" incluye que *a ti* te
paguen por construirlo — aunque el cliente no cobre nada por el bot.

**La buena noticia:** el plan de pago son ~$19.000 al mes y **cubre a todos tus clientes juntos**,
no uno cada uno. Con 5 clientes son $3.800 por cliente.

**Si el bot es para su propio negocio y no le cobra a nadie**, el plan gratis está bien.

---

## Si el usuario va a vender esto a clientes

Solo si en `/bot-planificar` dijo que el bot es para un tercero.

### Costo real por cliente, desde octubre

| Perfil del cliente | Costo/mes | Cobrar mínimo (60% margen) |
|---|---|---|
| 150 conv, bot corto | ~$19.000 | **~$48.000/mes** |
| 300 conv, bot corto | ~$33.000 | ~$83.000/mes |
| 500 conv, bot corto | ~$51.000 | ~$128.000/mes |
| 500 conv, bot largo | ~$167.000 | ~$418.000/mes |

*Con 5 clientes, para repartir el costo fijo del alojamiento.*

⚠️ **La conversación incómoda que hay que tener:**

Antes de octubre se podía cobrar una tarifa plana de $30.000 sin problema. **Ese modelo ya no
cierra** si el cliente tiene volumen.

**Las dos salidas honestas:**

1. **Tope de conversaciones incluidas en el contrato.** Es la mejor. 150 conversaciones al mes es
   bastante para una peluquería o una dental chica, y el modelo cierra cómodo cobrando $48.000.
   Sobre el tope, se cobra el excedente.

2. **Cobrar por volumen real**, con un mínimo mensual.

**Lo que no se puede hacer:** tarifa plana sin tope. Un cliente que se vuelve popular te deja
pagando de tu bolsillo.

**Si el usuario ya vendió bots con tarifa plana antes de octubre:** tiene que repactar ahora.
Dile que es mejor una conversación incómoda en septiembre que una pérdida en noviembre.

**Gate de la fase:** el usuario aceptó los costos explícitamente. Si dice que es mucho, revisa
alternativas antes de seguir — empezando por acortar las respuestas del bot, que es lo que más
rinde.

---

# PARTE B — Datos duros *(el usuario no ve esto)*

Verificado a agosto de 2026. Lo marcado ⚠️ hay que confirmarlo antes de comprometerlo.

## B1 · WhatsApp — las tarifas reales de Chile

**Chile es un mercado propio en el rate card de Meta.** No cae en "Rest of Latin America".

Fila del CSV oficial: `Chile,USD,0.0889,0.0200,0.0200,n/a,n/a`

| Categoría | USD/mensaje | Cuándo se cobra |
|---|---|---|
| **Marketing** | **$0,0889** | Siempre, incluso dentro de la ventana |
| **Utility** | **$0,0200** | Desde el 1-oct-2026, también dentro de la ventana |
| **Authentication** | **$0,0200** | Siempre |
| **Service** (respuestas del bot) | **$0 hasta 30-sep-2026, después ≈$0,0200** | Cada mensaje del bot |

⚠️ **La tarifa exacta de service para Chile no estaba publicada al cierre de esta investigación.**
Meta se comprometió a publicarla antes del 1-sep-2026; la columna decía `n/a`. La estimación de
$0,0200 asume paridad con utility, que es lo que Meta anunció. **Verifica el rate card antes de
cotizar.**

**Marketing en Chile es carísimo:** 3ª tarifa más alta del mundo, detrás de Países Bajos
($0,1597) y Alemania ($0,1365). Es **7× Colombia** ($0,0125) y **2,9× México** ($0,0305).

**Sin descuentos por volumen para service** (utility y authentication sí los tienen).

**Lo que sigue gratis:** la ventana de **72 horas** del Free Entry Point — cliente que llega por
anuncio Click-to-WhatsApp o botón de página de Facebook. Cubre marketing, utility, auth **y
service**. Dato curioso y aprovechable: los mensajes del agente de IA propio de Meta **no** son
gratis en esa ventana; los de un bot propio sí.

**Tiers de mensajería:** 250 → 2.000 → 10K → 100K → ilimitado, contactos únicos por 24 h. **Solo
aplican a mensajes que el negocio inicia.** Un bot reactivo no los toca. Para pasar de 250 a
2.000 se necesita verificación de negocio en Meta, verificación vía partner, o 2.000 mensajes de
calidad en 30 días.

**Meta agregó una 5ª categoría el 1-jul-2026:** "Meta Business Agent", su propio agente de IA,
cobrado por token ($2,00/1M). Un bot propio cae en **service**, no ahí. Meta lo dice explícito:
el servicio *"puede ser proporcionado por una persona… o por una solución de IA de terceros"*.

## B2 · Proveedor de WhatsApp — Zernio vs. directo

**Zernio no cobra markup sobre Meta y no cobra por mensaje.** Textual: *"Zernio never marks up or
re-bills Meta's fees — they appear on your Meta invoice"*.

| Concepto | Costo |
|---|---|
| Cuentas 1–2 conectadas | **Gratis para siempre**, sin tarjeta ($12 de crédito/mes) |
| Cuentas 3–10 | $6/cuenta/mes (graduado) |
| Cuentas 11–100 | $3/cuenta/mes |
| Número dedicado comprado a Zernio | Desde $3/mes (Chile no verificado) |
| Mensajes | **$0** — los cobra Meta directo a la WABA del cliente |

**Con número propio (BYO), Zernio cuesta literalmente $0 dentro de las 2 cuentas gratis.**

🚨 **RIESGO #1 — verificar antes de construir nada sobre el free tier:**

Hay una contradicción sin resolver en la propia documentación de Zernio:
- La página de precios dice: *"Every feature is included on every account, nothing is gated
  behind a plan"*
- El spec de la API devuelve **`403 Inbox addon required`** en ~40 endpoints, **incluidos todos
  los de `/v1/inbox/conversations/*`** — que son exactamente los que necesita un bot
- Y la doc de WhatsApp Inbox dice que el Inbox viene con toda cuenta **de pago**

**Interpretación probable:** restos del modelo de planes anterior (Zernio es el rebrand de
"Late"). **Pero no está confirmado que el Inbox funcione en el tier gratuito sin tarjeta.**

**Qué hacer:** probarlo con una cuenta real, o preguntarle a soporte, **antes** de prometerle al
usuario que es gratis. Si resulta que el Inbox exige plan de pago, el free tier de Zernio no
sirve para un bot y hay que replantear `/bot-conectar`.

**Alternativas evaluadas:**

| Opción | Costo | Veredicto |
|---|---|---|
| **Cloud API directo (Meta)** | $0 de plataforma | Más barato, pero te comes toda la plomería: app propia, App Review, y construyes inbox, persistencia y dedupe tú |
| **Zernio** | $0 con BYO en free tier | Buen atajo. Empresa joven (WhatsApp lanzado jun-2026), sin SLA contractual |
| **Twilio** | **+$0,005 por mensaje, entrante y saliente** | ❌ Mal alineado. Una conversación de 6 turnos son $0,06 solo de Twilio — **1,5× lo que cobra Meta**. Descartado |
| **360dialog** | €49/mes fijo | Sin markup por mensaje, pero pagas el fijo aunque no mandes nada. Malo a bajo volumen |
| **Evolution API** | Gratis, self-hosted | ❌ **Viola los términos de WhatsApp.** Riesgo real de ban permanente. Jamás para un cliente |

## B3 · Alojamiento

**Vercel Hobby prohíbe el uso comercial.** Texto literal de las Fair Use Guidelines:

> *"Hobby teams are restricted to non-commercial personal use only."*
>
> *"Commercial usage is defined as any Deployment that is used for the purpose of financial gain
> of **anyone** involved in **any part of the production** of the project, **including a paid
> employee or consultant writing the code**."*

No es zona gris. **El punto de quiebre es el cliente #1, no un límite de volumen.**

Los límites técnicos sobran: 500 conversaciones/mes consumen ~3% de invocaciones y ~10% del CPU.
El techo técnico está cerca de 5.000 conversaciones/mes.

**Vercel Pro: $20/mes**, proyectos ilimitados. El compute de 5 clientes cuesta ~$1,50/mes, dentro
del crédito incluido. **Costo fijo del negocio, no por cliente.**

**Alternativa si el costo es bloqueo:** Cloudflare Workers free **sí permite uso comercial**
(100.000 requests/día). Contra: menos camino pavimentado y límite de 10ms de CPU.

## B4 · El modelo — Haiku 4.5

| Modelo | Input | Output | 500 conv (15 turnos) |
|---|---|---|---|
| **Claude Haiku 4.5** | $1/MTok | $5/MTok | **$21,95** |
| Claude Sonnet 5 | $2/MTok | $10/MTok | $41,76 |

⚠️ **No implementes prompt caching de entrada.**

1. **Haiku 4.5 exige un prefijo mínimo de 4.096 tokens.** Un system prompt típico (~1.650 tokens
   con tools) queda bajo el mínimo y **no cachea nada, sin devolver error**. Falla en silencio.
   Si lo activas igual, verifica `usage.cache_read_input_tokens`: si sale 0 siempre, no cachea.
2. **El TTL es de 5 minutos.** En WhatsApp la gente responde en minutos u horas.

**El número que decide:** Haiku sin cache ($21,95) sale más barato que Sonnet con cache perfecto
($23,19).

**Cuándo sí conviene:** si el system prompt supera los 4.096 tokens (catálogo largo, FAQ extenso).
Ahí Haiku sí cachea, con ~25% de ahorro.

**Palanca más efectiva:** el 66% del input es prefijo repetido, no historial. **Acortar el system
prompt rinde mucho más que truncar la conversación** (truncar a 6 pares ahorra solo 9%).

Pero recuerda: desde octubre, **todo esto es secundario frente a reducir la cantidad de mensajes
que manda el bot**.

**Rate limits (Start tier):** 1.000 RPM / 2M ITPM. De sobra. Tope por defecto $500/mes — bájalo
al valor de `/bot-publicar`.

## B5 · Persistencia — multi-tenant obligatorio

⚠️ **Supabase free permite solo 2 proyectos activos**, y el límite aplica a todas las
organizaciones donde seas Owner o Admin. **Con 5 clientes topas en el cliente #3.**

**Solución obligatoria:** un proyecto multi-tenant con RLS por `client_id`. Además de resolver el
límite, es la práctica correcta de seguridad (bloque B5 de `seguridad.md`).

Otros límites: 500 MB de base (sobra), 5 GB de egress, **pausa tras 7 días sin actividad**.

⚠️ **El riesgo real de la pausa:** un cliente con poco tráfico que pasa una semana en silencio se
pausa, y el próximo que escriba encuentra el bot muerto.

**Alternativa: Neon** (0,5 GB, 100 CU-hrs/mes), mejor para leads por SQL real. ⚠️ Autosuspende a
los 5 min, no desactivable en free. Con tráfico agrupado son ~21 CU-hrs/mes; con mensajes muy
espaciados puede llegar a ~156 y pasarse. **Nunca le pongas un health-check frecuente: eso solo se
come el cupo.**

**Vercel Global Config (ex Edge Config) NO sirve para conversaciones** — hasta 10 segundos para
propagar. El bot se repetiría o se olvidaría de lo que acaba de decir. **Su uso legítimo:**
configuración por cliente (horarios, servicios, interruptor de apagado).

**Upstash Redis:** 256 MB, 500K comandos/mes (~20 clientes). ⚠️ Se archiva tras 30 días de
inactividad — no pierdes datos pero **cambia el endpoint**.

**Recomendación:** una sola base (Neon o Supabase). A este volumen no necesitas Redis, y es una
dependencia menos. **Vercel KV ya no existe** — migrado a Upstash en dic-2024.

## B6 · Agenda — service account con calendario compartido

**Google Calendar API es gratis:** 1.000.000 queries/día. Un bot usa ~83/día. ⚠️ Google avisa que
excederse pasará a cobrarse "later in 2026", con 90 días de aviso.

**El camino correcto con un Gmail gratis:**

| Enfoque | ¿Funciona con Gmail gratis? |
|---|---|
| OAuth 2.0 con consentimiento | ✅ Sí, con pantalla de advertencia y verificación |
| Service account + domain-wide delegation | ❌ **NO — exige Google Workspace pagado** |
| **Service account + el dueño comparte su calendario** | ✅ **Este es el camino** |

**Lo que hace el dueño (2 minutos, guíalo en vivo):** Google Calendar → Configuración de mi
calendario → *Compartir con determinadas personas* → pegar el correo del service account →
**"Hacer cambios en los eventos"** → Enviar.

**Por qué es clave para el modelo de negocio:** **un solo service account sirve a todos los
clientes.** Cero OAuth por cliente, cero tokens que expiran, cero verificación de Google.

**Tres letras chicas:**
1. **No puedes agregar invitados al evento** (403 `forbiddenForServiceAccounts`). Impacto casi
   nulo: pon nombre y teléfono en título y descripción. ⚠️ Confirmado por la comunidad, ausente de
   la doc oficial.
2. ⚠️ **Google no documenta explícitamente este flujo para Calendar.** Funciona en la práctica —
   **pruébalo con un Gmail desechable antes de prometérselo a un cliente**.
3. Si el dueño se enreda, alternativa: que el service account cree un calendario secundario y le
   dé acceso.

**Evita Cal.com y Calendly.** Cal.com: el plan Platform está deprecado para nuevos registros desde
dic-2025. Calendly free **no tiene webhooks** — sin ellos no detectas cancelaciones.

## B7 · Restricciones de arquitectura que no se negocian

⚠️ **Doble timeout, y son distintos:**

| Proveedor | Plazo de respuesta | Reintentos |
|---|---|---|
| **Meta directo** | ~3 segundos | Backoff exponencial **hasta 7 días** |
| **Zernio** | **5 segundos** | **7 intentos**: inmediato → 10s → 1m40s → 16m40s → 2h46m → 24h → 24h, después dead-letter |

Una llamada a Claude demora entre 3 y 10 segundos. **Confirmar recepción de inmediato y procesar
en segundo plano es obligatorio**, no una optimización. Si no, el cliente recibe respuestas
duplicadas y tú pagas las llamadas duplicadas — que ahora, además, cuestan mensaje de WhatsApp.

**Semántica at-least-once.** Deduplicación obligatoria por identificador de evento
(`X-Zernio-Event-Id` o el `id` del payload).

## B8 · Verificación de firma con Zernio

- **Header:** `X-Zernio-Signature` (alias legacy `X-Late-Signature` — el rebrand desde "Late" aún
  emite ambos)
- **Algoritmo:** HMAC-SHA256 del **raw body**, secret como clave, hex minúscula
- **Variable:** `ZERNIO_WEBHOOK_SECRET`

⚠️ **Dos problemas del esquema que tienes que compensar tú:**

1. **No hay timestamp firmado → no existe protección anti-replay nativa.** Un payload capturado se
   puede reenviar indefinidamente. **Mitigación obligatoria:** deduplicar por identificador de
   evento con TTL, y rechazar eventos con `createdAt` viejo.
2. **El ejemplo oficial de Node usa `!==`, que no es timing-safe.** Usa `crypto.timingSafeEqual`.
   (El ejemplo de Python sí usa `hmac.compare_digest`.)

## B9 · Herramientas de construcción

**Vercel Chat SDK** (paquete `chat`, v4.39.0, MIT, gratis). Escribes la lógica una vez y sirve
para varios canales.

⚠️ **El state adapter no es opcional.** Doc explícita: *"You must provide a state adapter when
creating a `Chat` instance."* Maneja suscripciones, bloqueo distribuido y deduplicación. En
serverless hay que usar Redis o Postgres — **por eso la base de datos es costo obligatorio**.

**Limitaciones del adapter de WhatsApp:** no soporta historial, edición ni borrado. Tarjetas con
**máximo 3 botones** (títulos de 20 caracteres); si te pasas, cae a texto plano. Body máximo 1.024
caracteres, auto-chunking sobre 4.096. Sí soporta reacciones, confirmaciones de lectura,
indicador de escritura, descarga de multimedia y ubicación.

⚠️ **Sin declaración formal de disponibilidad general.** El adapter de WhatsApp tiene ~6 meses. Es
MIT y Vercel lo documenta como producción, pero es joven.

El adapter de Zernio (`@zernio/chat-sdk-adapter`, MIT) tiene **6 stars en GitHub** — adopción
mínima, cero validación comunitaria. Es un wrapper delgado sobre la API REST; siempre puedes
bajarte a HTTP directo.

**Antes de escribir código con cualquiera de estos, lee la documentación oficial.** Son recientes
y cambian; no te fíes de la memoria.

---

## Decisiones por defecto

| Decisión | Elección | Por qué |
|---|---|---|
| **Largo de las respuestas** | **Lo más corto posible** | Desde oct-2026, es la palanca económica #1 |
| Modelo | Haiku 4.5 | Más barato que Sonnet incluso con cache perfecto |
| Prompt caching | No, de entrada | No alcanza el mínimo de Haiku; falla en silencio |
| Proveedor de WhatsApp | Zernio con número propio | $0 en free tier, sin markup. **Verificar el Inbox antes** |
| Alojamiento (propio) | Vercel Hobby | Gratis y permitido si nadie cobra |
| Alojamiento (cliente) | **Vercel Pro** | Hobby prohíbe uso comercial. $20 cubre todos |
| Base de datos | Neon o Supabase, una sola | Menos dependencias |
| Multi-cliente | Un proyecto con RLS | El free tier no da para uno por cliente |
| Agenda | Service account + calendario compartido | Uno solo sirve a todos los clientes |
| Procesamiento | **Background obligatorio** | 3s de Meta / 5s de Zernio vs. 3-10s del modelo |
| Método de pago en la WABA | **Antes del 30-sep-2026** | Sin esto, el bot deja de responder |

---

## Lo que hay que verificar antes de comprometerlo

1. 🚨 **Que el Inbox de Zernio funcione en el free tier sin tarjeta.** Es el riesgo #1: sin eso,
   no hay bot en plan gratis.
2. 🚨 **La tarifa de service para Chile** en el rate card oficial. Meta debía publicarla el
   1-sep-2026.
3. Que el service account escriba en un calendario Gmail compartido — pruébalo con una cuenta
   desechable.
4. Estabilidad real del adapter de WhatsApp del Chat SDK.
