---
name: bot-conectar
description: >
  Etapa 4 del sistema de bot de WhatsApp. Conecta el número de WhatsApp real al asistente, guiando
  al usuario clic por clic. Cubre la elección del número entre tres caminos con su lock-in, las
  advertencias sobre el número que se quema si Meta banea, el método de pago obligatorio antes del
  30 de septiembre de 2026, y la verificación del negocio. Úsalo cuando el usuario escriba
  /bot-conectar, o cuando ya probó su bot en demo y necesite conectar WhatsApp.
---

# Etapa 4 de 9 — Conectar WhatsApp

**La fase más frágil de todo el proyecto.** Es donde el usuario hace cosas con sus manos, donde
intervienen terceros que no controlas, y donde un error se paga con un número quemado para
siempre.

⚠️ Es la etapa que depende de terceros: Meta puede pedir verificación del negocio y eso no lo controlamos nosotros.

---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md`. **Las 14 pruebas tienen que estar pasadas.** Si no, mándalo a `/bot-probar`
   primero — no metas a nadie en este trámite con un bot sin probar.
3. Carga `~/.claude/skills/bot-whatsapp/references/conexion-whatsapp.md`.

---

## Encuadra la etapa

> *"Esta es la parte más lenta, y no depende de nosotros sino de Meta. La buena noticia es que ya
> sabes que tu asistente funciona: lo probaste tú mismo. Ahora solo hay que darle un número."*

---

## Las 3 advertencias, antes del primer clic

Van **completas y juntas**. No las dosifiques. Están desarrolladas en la referencia:

1. **El número queda dedicado al bot.** Un WhatsApp personal no se puede usar — Meta exige
   WhatsApp Business.
2. **Si te banean, el número se pierde para siempre.** Si la apelación se rechaza, no se puede
   volver a registrar.
3. 🚨 **Fecha límite: 30 de septiembre de 2026.** Sin método de pago registrado, el asistente deja
   de entregar respuestas el 1 de octubre. No falla con error: el cliente escribe y nunca le llega
   nada.

⚠️ **Si el usuario ya tiene otros bots andando de antes de este proyecto, avísale hoy mismo** —
aunque estén fuera de este trabajo. Es un favor que vale más que el proyecto entero.

---

## Los pasos

Todos están detallados en la referencia. Resumen del orden:

1. **Elegir el número** — 3 caminos, cada uno con su lock-in. Recomendación por defecto: usar el
   número que ya tiene en WhatsApp Business, o uno nuevo del negocio. **Nunca** un número del
   proveedor para el número principal de un negocio: no hay forma de portarlo.
2. **Crear las cuentas** — él crea, copia la llave y te la pega. Una acción por turno.
3. 🚨 **Método de pago** — lo pone el negocio, en su propia cuenta. **Verifícalo tú**, no te quedes
   con un "sí, ya lo puse".
4. **Verificación del negocio** — solo si va a iniciar conversaciones. Requiere RUT de empresa y
   sitio web propio. 2 a 7 días hábiles.

---

## El gate de la etapa

- [ ] **El usuario mandó un mensaje desde su teléfono al número del bot y tú confirmaste que
      llegó**
- [ ] 🚨 Método de pago registrado y verificado por ti
- [ ] Las cuentas están a nombre del negocio, no del desarrollador
- [ ] La llave está guardada en el servidor, no en un chat
- [ ] Si eligió mantener su número de WhatsApp Business, entendió las limitaciones que aceptó

---

## Si algo sale mal

La referencia tiene la tabla completa de síntomas y salidas: número ya conectado en otro lado,
cuenta personal activa, PIN de verificación, formulario de identidad, verificación rechazada,
nombre visible rechazado.

**Manéjalos tú.** Al usuario solo le llega la solución, nunca el error.

---

## Al cerrar

1. Actualiza `ESTADO.md`: número conectado, cuál es, método de pago confirmado.
2. Manda al siguiente paso:

> *"Tu número ya está conectado. Antes de encenderlo con clientes reales voy a correr la revisión
> de seguridad — es la última red de protección. Escribe **`/bot-revisar`**."*
