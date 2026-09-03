---
name: bot-costos
description: >
  Etapa 2 del sistema de bot de WhatsApp. Explica qué cuentas necesita el usuario y le muestra la
  tabla de costos reales en la moneda de su país, con la tarifa de WhatsApp que le corresponde e
  incluyendo el cambio de Meta del 1 de octubre de 2026, donde cada respuesta del bot pasa a
  costar. Cierra cuando el usuario acepta los costos explícitamente. Úsalo cuando el usuario
  escriba /bot-costos, o pregunte cuánto cuesta operar un bot de WhatsApp.
---

# Etapa 2 de 9 — Costos

**La etapa que evita el problema del mes 3.** Nadie abandona un bot porque no le gustó: lo
abandona porque le llegó una cuenta que no esperaba.


---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md` — necesitas la Ficha del Bot para estimar el volumen. **Si no existe o la ficha
   está a medias**, mándalo a `/bot-planificar` primero: sin saber qué hace el asistente ni cuánta
   gente le escribe, cualquier cifra que le des es inventada.
3. Carga `~/.claude/skills/bot-whatsapp/references/herramientas-costos.md`.

---

## Qué haces acá

### 1. Las cuentas, en una frase cada una

Cuatro cosas (cinco si va a agendar). Nada de arquitectura. Está la tabla lista en la referencia,
**Parte A**.

### 2. La tabla de costos

⚠️ **Muéstrale la columna de octubre en adelante, no la de antes.** Si le muestras el costo
actual, en un mes te reclama con razón.

Ajusta el volumen a lo que dijo en la Ficha del Bot. Si atiende 150 conversaciones al mes, no le
muestres la tabla de 500 — se va a asustar de gratis.

### 3. Las tres cosas que le tienen que quedar claras

1. **Lo que cuesta es cada mensaje que manda el asistente, no cada cliente.** Por eso un asistente
   que responde bien en 3 mensajes cuesta un tercio que uno que responde en 9.
2. **Mandar promociones es carísimo en Chile** — tercera tarifa más cara del mundo, ~$83 por
   mensaje. Una promo a 500 contactos son ~$41.000. Se presupuesta aparte.
3. **Hay una puerta gratis:** si el cliente llega por un anuncio con botón de WhatsApp, se abre
   una ventana de 72 horas sin costo.

### 4. Si el bot es para un cliente que le paga

Va la conversación de precios: **tarifa plana sin tope ya no cierra**. Está la tabla de qué
cobrar y las dos salidas honestas en la referencia.

⚠️ **Y el aviso del alojamiento:** el plan gratuito prohíbe el uso comercial. Si le pagan por
construirlo, necesita el plan de pago — pero ese plan cubre a todos sus clientes juntos.

---

## El gate de la etapa

- [ ] **El usuario aceptó los costos explícitamente.** No un "ya, sigamos": un sí a la cifra.

Si dice que es mucho, **no sigas**. Revisa alternativas con él, empezando por acortar las
respuestas del asistente, que es la palanca que más rinde. No lo metas a construir algo que no va
a poder pagar.

---

## Si algo no aparece

| Debería ver | Si no pasa |
|---|---|
| La tabla en **su** moneda, con su volumen real | Si le mostraste el ejemplo de 500 conversaciones a alguien con 5 al día, se asustó de gratis. Rehazla |
| Que acepta el costo explícitamente | Si duda, revisa alternativas antes de seguir. No lo metas a construir algo que no va a pagar en el mes 2 |
| No encuentras la tarifa de su país | Dilo: *"déjame confirmar el precio exacto en tu país"*. Nunca inventes la cifra |

Si pasa algo que no está en esta tabla, **no le pases el problema al usuario**: arréglalo y
cuéntale solo lo que necesita saber.

---

## Al cerrar

1. Actualiza `ESTADO.md`: costos aceptados, con la cifra y la fecha, en DECISIONES TOMADAS.
2. Manda al siguiente paso:

> *"Perfecto. Ahora viene la parte entretenida: voy a construir tu asistente y lo vas a probar
> desde tu teléfono — **sin conectar tu WhatsApp todavía**. Así lo ves funcionando antes de meterte
> en el trámite con Meta. Escribe **`/bot-probar`**."*
