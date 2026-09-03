# Conectar WhatsApp

**La fase más frágil de todo el proyecto.** Es donde el usuario tiene que hacer cosas con sus
manos, donde intervienen terceros que no controlas, y donde un error se paga con un número
quemado para siempre.

**Objetivo:** que un mensaje real, mandado desde el teléfono del usuario, llegue al sistema.

**Regla de la fase:** guías clic por clic. Si algo se puede hacer por él, lo haces tú. Lo único
que él hace es lo que requiere su identidad o su decisión.

---

# ⚠️ ANTES DE QUE TOQUE NADA

Estas tres advertencias van **completas y juntas**, antes del primer clic. No las dosifiques.

## 1. El número que conecte queda dedicado al bot

> *"El número que conectemos va a quedar dedicado al asistente. No uses tu WhatsApp personal.
> Tampoco el número principal del negocio sin que conversemos antes qué cambia."*

**Por qué importa:** un número de WhatsApp personal **no se puede usar**. Meta exige WhatsApp
Business. Y si el número ya tiene una cuenta personal activa, hay que borrarla primero — con todo
lo que eso significa para el dueño.

## 2. Si te banean, el número se pierde para siempre

> *"Si Meta bloquea el número por mal uso y la apelación se rechaza, ese número queda quemado.
> No se puede volver a registrar. Por eso vamos a hacer las cosas bien desde el principio y por
> eso no experimentamos con tu número principal."*

## 3. 🚨 Hay una fecha límite: 30 de septiembre de 2026

> *"Meta cambió las reglas. Desde el 1 de octubre empieza a cobrar por cada respuesta que manda
> el asistente. Y si no hay un método de pago registrado antes del 30 de septiembre, **el
> asistente simplemente deja de entregar respuestas**. El cliente escribe, y nunca le llega nada."*

**Esto no es opcional y no admite postergarse.** Va en la lista de verificación de esta fase.

⚠️ **Si el usuario ya tiene otros bots andando de antes de este proyecto, avísale hoy mismo** —
aunque estén fuera de este trabajo. Es un favor que vale más que el proyecto entero.

---

# PASO 1 — Elegir el número

Tres caminos. Preséntaselos y que elija. **La decisión no es reversible sin costo.**

## Camino A — Usar el número que ya tiene en WhatsApp Business *(el más común)*

Si el negocio ya usa la app de WhatsApp Business, se puede mantener el mismo número funcionando
**en la app y con el asistente al mismo tiempo**.

**Lo bueno:**
- No cambia el número que sus clientes ya conocen
- El equipo sigue usando la app como siempre
- Se sincronizan hasta **6 meses de historial** y los contactos

**Lo que hay que saber antes de decidir** — dilo completo, son limitaciones reales:

| Qué cambia | Detalle |
|---|---|
| Grupos de la app | Dejan de sincronizarse |
| Llamadas de voz y video | No funcionan a través del asistente |
| Mensajes temporales | Se apagan en las conversaciones uno a uno |
| Ver una sola vez | Se deshabilita en uno a uno |
| Listas de difusión | Se deshabilitan en la app |
| Velocidad de envío | Queda fija en 20 mensajes por segundo (irrelevante a esta escala) |

⚠️ **Advertencia importante:** este emparejamiento es **exclusivo de un proveedor**. Si el negocio
ya tenía otra herramienta conectada a ese número, hay que desconectarla primero **desde el
teléfono** (Ajustes → Cuenta → Plataforma Business → Desconectar). **No se puede hacer a
distancia.**

## Camino B — Un número nuevo del negocio

El negocio consigue una línea nueva dedicada al asistente.

**Lo bueno:** cero interferencia con lo que ya existe, y si algo sale mal no arrastra el número
principal.

**Lo malo:** hay que avisarle a los clientes que hay un número nuevo, y perder el historial.

## Camino C — Un número provisto por el proveedor

El proveedor vende un número dedicado, desde ~$3 USD al mes.

**Lo bueno:** se activa en unos 30 segundos en algunos países, sin conseguir línea.

🔴 **El problema serio — dilo antes de que elija:** **ese número no se puede llevar a otro
proveedor.** No existe forma de portarlo. Si el día de mañana quiere cambiarse, **pierde el
número** y hay que avisarle a todos sus clientes.

**Recomendación:** este camino solo para pruebas o para algo temporal. **Nunca para el número
principal de un negocio.**

⚠️ En países con regulación —y hay que verificar dónde cae Chile— se pide un formulario de
identidad con documento y dirección local, y la activación demora **1 a 3 días hábiles**.

---

## La recomendación por defecto

**Camino A si el negocio ya usa WhatsApp Business. Camino B si no.**

En ambos, el número queda **a nombre del negocio**, dentro de su propia cuenta de Meta Business.
Eso significa:
- Las plantillas aprobadas, el nombre visible, la calificación de calidad y el nivel de
  mensajería **viven en la cuenta del negocio y se los lleva** si cambia de proveedor
- **El lock-in es casi nulo**
- Legalmente, el negocio es el dueño de sus datos — que es lo correcto (ver `legal.md`)

---

# PASO 2 — Probar sin comprometer nada

**Antes de conectar el número definitivo, se prueba en un ambiente de prueba.**

Hay dos formas, según el proveedor:
- Un **modo de prueba** que manda mensajes desde un número compartido a un teléfono que el usuario
  registre
- La **cuenta de prueba de Meta**, que crea un número de prueba automáticamente y permite mandar
  gratis a hasta **5 números** registrados, sin tarjeta

**Esto es suficiente para construir y demostrar el asistente completo.** Úsalo en `/bot-probar` y en
buena parte de la 6, y deja la conexión del número real para el final.

**Ventaja para el usuario:** puede ver su asistente funcionando antes de tomar decisiones
irreversibles sobre su número.

---

# PASO 3 — Crear las cuentas

Guíalo clic por clic. Una acción por turno. Si algo se puede hacer sin él, hazlo tú.

**Lo que él hace:**
1. Crear la cuenta en el proveedor de mensajería (correo y contraseña — **que use un gestor de
   contraseñas o una clave larga**)
2. Conectar WhatsApp desde el panel, siguiendo el flujo que le muestra la pantalla
3. Durante ese flujo se crea o se conecta su cuenta de Meta Business
4. Copiar la llave de acceso que aparece **una sola vez** y pegártela en el chat

⚠️ **Avísale antes:** *"la llave se muestra una sola vez. Cópiala apenas aparezca y pégamela acá.
Si se pierde, hay que generar otra."*

**Lo que haces tú:** todo lo demás.

**Recordatorio de seguridad — dilo una vez, sin dramatizar:**
> *"Esa llave es como la contraseña de tu WhatsApp del negocio. No la mandes por WhatsApp, no la
> pegues en un grupo, no se la pases a nadie. Si crees que se filtró, me avisas y la cambiamos al
> tiro."*

---

# PASO 4 — 🚨 El método de pago *(no se salta)*

**Hay que registrar un método de pago en la cuenta de WhatsApp Business del negocio.**

Dos razones:
1. **Antes del 30 de septiembre de 2026**, o el asistente deja de entregar respuestas el 1 de
   octubre
2. Sin método de pago, Meta bloquea la entrega de plantillas desde ya

**Quién la pone:** el **negocio**, en su propia cuenta. No el desarrollador. Esto conecta con la
regla de `entrega-cliente.md` — las cuentas son del cliente.

**Verifícalo tú mismo antes de cerrar la fase.** No te quedes con un "sí, ya la puse".

---

# PASO 5 — Verificación del negocio *(si va a mandar mensajes que él inicia)*

**Solo hace falta si el negocio va a iniciar conversaciones** (recordatorios, promociones). Un
asistente que solo responde **no la necesita** para funcionar.

Sin verificar, el negocio puede iniciar conversaciones con **250 contactos únicos cada 24 horas**.
Con verificación, sube a **2.000**.

**Lo que se necesita en Chile:**
- **RUT de empresa**, no personal
- e-RUT, escritura de constitución, comprobante de domicilio comercial
- **Un sitio web con dominio propio**, que muestre nombre, servicios y datos de contacto

**Demora 2 a 7 días hábiles.**

⚠️ **La causa número uno de rechazo son las inconsistencias**: que el nombre, la dirección y el
RUT no calcen exacto entre los documentos. Revísalo con él **antes** de enviar.

💡 **Si el negocio no tiene sitio web**, esto es un bloqueo — y también una oportunidad obvia de
venderle uno.

---

# PASO 6 — El gate de la fase

**El usuario manda un mensaje desde su teléfono al número del bot, y tú confirmas que llegó.**

Dile exactamente esto:

> *"Ahora agenda el número [X] en tu teléfono y mándale un 'hola'. Avísame cuando lo hayas
> mandado."*

Cuando confirme, verifica que el mensaje llegó al sistema.

**Sin este gate, no se construye nada.** Todo lo de `/bot-probar` asume que los mensajes llegan. Si no
llegan, vas a construir a ciegas y a descubrirlo en `/bot-probar`.

**Checklist antes de cerrar la fase:**
- [ ] El mensaje del usuario llegó al sistema
- [ ] 🚨 **Método de pago registrado en la cuenta de WhatsApp Business**
- [ ] Las cuentas están a nombre del negocio, no del desarrollador
- [ ] La llave de acceso está guardada en el servidor, no en un chat
- [ ] El usuario sabe qué número quedó dedicado al bot
- [ ] Si eligió el camino A, entendió las limitaciones que aceptó
- [ ] Verificación del negocio iniciada, si la necesita

---

# QUÉ PUEDE SALIR MAL

Los problemas reales de esta fase, con su salida. **Manéjalos tú; al usuario solo le llega la
solución.**

| Síntoma | Qué pasa | Qué haces |
|---|---|---|
| El número ya está conectado en otro lado | Un número solo puede estar activo en un lugar | El usuario lo desconecta desde el panel del otro proveedor, o desde su teléfono si es la app |
| El número tiene WhatsApp personal activo | Meta no lo permite | Hay que borrar la cuenta personal de ese número, o usar el camino A con la app Business |
| Pide un PIN de verificación en dos pasos | El número tiene verificación activada | Pídele el PIN al usuario y regístralo. Si no lo recuerda, se resetea desde el teléfono |
| Piden formulario de identidad | Países con regulación | Ayúdalo a llenarlo. Son 1 a 3 días hábiles. Avísale del plazo, no lo dejes esperando |
| Rechazaron la verificación del negocio | Casi siempre, documentos inconsistentes | Revisa que nombre, dirección y RUT calcen exacto. Corrige y reenvía |
| El nombre visible fue rechazado | Genérico, promocional, o no coincide con la marca | Que use el nombre real del negocio, tal como aparece en sus documentos |
| Dejaron de llegar mensajes de un momento a otro | El canal se cayó o alguien desconectó desde el teléfono | Verifica el estado del número. Los avisos automáticos de desconexión no son confiables — comprueba activamente |

⚠️ **Advertencia técnica seria si conectas por credenciales directas:** ese método **redirige la
entrega de eventos de la cuenta hacia el nuevo proveedor de inmediato y sin período de
solapamiento.** Si el negocio ya tenía otra integración sobre esa cuenta, **se corta en seco**.
Pregunta antes si hay algo más conectado.

---

# NOTAS TÉCNICAS *(el usuario no ve esto)*

## Verificación de la firma

- Header `X-Zernio-Signature` (también emite el alias antiguo `X-Late-Signature` — Zernio es el
  rebrand de "Late")
- HMAC-SHA256 del cuerpo crudo, secreto como clave, hexadecimal en minúscula
- Variable: `ZERNIO_WEBHOOK_SECRET`

⚠️ **Dos debilidades del esquema que compensas tú:**
1. **No hay marca de tiempo firmada → sin protección contra reenvío.** Un mensaje capturado se
   puede reenviar indefinidamente. **Obligatorio:** deduplicar por identificador de evento con
   expiración, y rechazar eventos viejos.
2. **El ejemplo oficial en Node usa comparación directa, que no es segura ante ataques de
   tiempo.** Usa comparación en tiempo constante.

## Plazos de respuesta

| Proveedor | Plazo | Reintentos |
|---|---|---|
| Meta directo | ~3 segundos | Backoff exponencial hasta 7 días |
| Zernio | **5 segundos** | 7 intentos, después cola de descarte |

Una llamada al modelo demora 3–10 segundos. **Confirmar recepción de inmediato y procesar en
segundo plano es obligatorio.** Semántica de al-menos-una-vez: deduplicación obligatoria.

## Límites operativos

- **Ritmo por destinatario:** ~10 mensajes por minuto a la misma persona. Ráfagas mayores dan
  error `131056`. Paraleliza entre destinatarios, no contra uno.
- **Media:** imagen 5 MB (JPEG/PNG), video 16 MB (MP4/3GPP), documento 100 MB, audio 16 MB. Nota
  de voz real requiere `.ogg` OPUS mono.
- **Ventana de 24h:** hay que calcularla desde el último mensaje entrante — el proveedor no la
  expone.
- **Mensajes interactivos:** todos son de sesión, solo dentro de la ventana.

## Errores frecuentes

`131026` ventana cerrada · `131021` número inválido o sin WhatsApp · `131047` límite de ritmo ·
`132001` plantilla no encontrada · `131031` cuenta bloqueada por Meta · `133005` PIN de
verificación en dos pasos

## Campo útil

El campo que indica el origen del mensaje sirve para no responderte a ti mismo. ⚠️ **Cuando viene
vacío significa "desconocido"** (mensajes entrantes, enviados desde la app, o anteriores a
agosto de 2026 — no se rellenó hacia atrás). **Nunca lo trates como "lo mandó un humano".**

## 🚨 Verificar antes de construir sobre el plan gratuito

Hay una contradicción sin resolver en la documentación de Zernio: la página de precios dice que
nada está restringido por plan, pero la especificación de la API devuelve **`403 Inbox addon
required`** en los endpoints de conversaciones — justo los que necesita un bot.

**Pruébalo con una cuenta real o pregúntale a soporte antes de prometerle al usuario que el plan
gratuito le sirve.** Si resulta que el Inbox exige plan de pago, hay que replantear los costos de
`/bot-costos`.
