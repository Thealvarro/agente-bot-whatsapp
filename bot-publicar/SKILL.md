---
name: bot-publicar
description: >
  Etapa 6 del sistema de bot de WhatsApp. Enciende el asistente para atender clientes reales, en
  modo borrador por defecto: el bot redacta y un humano aprueba antes de que salga. Configura el
  tope de gasto que corta, el interruptor de apagado y los avisos legales. Úsalo cuando el usuario
  escriba /bot-publicar, o cuando ya pasó la revisión de seguridad y quiera encender su bot.
---

# Etapa 6 de 9 — Publicar

Encender no es apretar un botón y salir corriendo. Es encender y quedarse mirando.


---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md`. **La revisión tiene que estar pasada.**
3. Carga `~/.claude/skills/bot-whatsapp/references/produccion.md`.
4. Carga los textos obligatorios de `~/.claude/skills/bot-whatsapp/references/legal-chile.md`,
   sección 4.

---

## La lista de las 12, con el usuario

Recórrela **con él**, en voz alta, no por tu cuenta. Está completa en `produccion.md`.

Los encabezados: método de pago registrado · el bot no habla fuera de tema · contrato de encargo
si es para un tercero · las 14 pruebas pasadas · sabe apagarlo solo · tope de gasto puesto ·
humano de respaldo avisado · avisos legales instalados · declaración de IA en el primer mensaje ·
modo borrador activo · número definitivo · ficha al día.

**Si falta uno, no se enciende.** Dile cuál falta y resuélvelo.

---

## Las tres cosas que se configuran acá

### 1. El modo borrador *(activo por defecto)*

> *"Los primeros días tu asistente no le va a escribir a nadie directamente. Prepara la respuesta
> y tú la apruebas antes de que salga. Vas a ver exactamente qué habría contestado."*

⚠️ Si quiere saltárselo, adviértele **una vez** con un ejemplo concreto: *"la primera respuesta
rara la va a ver un cliente, no tú"*. Si insiste, es su decisión: va a RIESGOS ACEPTADOS.

### 2. El tope de gasto

Pregunta directa: *"¿Cuánto es lo máximo que estás dispuesto a gastar en un día, en el peor
escenario, sin que te dé un infarto?"*

Ese número corta automático. Más un aviso al 50% para que vea venir el problema.

**Un tope que solo avisa no es un tope.**

### 3. El interruptor de apagado

En un solo lugar que recuerde, efecto inmediato, sin necesitarte a ti, y tan fácil de prender
como de apagar.

Dale la regla de uso en una frase:

> *"Ante la duda, apágalo. Prefiero que lo apagues sin necesidad diez veces, a que lo dejes
> prendido una vez que había que apagarlo."*

---

## El encendido

**No lo enciendas y te vayas.** Las primeras 2 horas:

- Que el usuario le escriba primero, como si fuera un cliente
- Revisen juntos las primeras 3 conversaciones reales
- Confirma que las derivaciones llegan al humano de respaldo
- Confirma que el gasto va donde debería

---

## El gate de la etapa

- [ ] Un cliente real fue atendido y el usuario vio la conversación
- [ ] El usuario sabe apagarlo solo, sin preguntarte cómo
- [ ] Las derivaciones llegan al canal real

---

## Al cerrar

1. Actualiza `ESTADO.md`: publicado con fecha, modo borrador activo, tope de gasto configurado.
2. Explícale la rutina que viene:

> *"Ya está atendiendo. Ahora, todos los días, entra con **`/bot-bandeja`** para aprobar sus
> respuestas y ver cómo va. Cuando lleve una semana respondiendo bien, lo soltamos
> para que conteste solo."*
