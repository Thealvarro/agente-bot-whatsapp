---
name: bot-planificar
description: >
  Etapa 1 del sistema de bot de WhatsApp. Entrega el brief de seguridad en lenguaje humano, hace
  las 13 preguntas de descubrimiento del negocio y diseña el guion de la conversación del
  asistente. Produce la Ficha del Bot aprobada por el usuario. Úsalo cuando el usuario escriba
  /bot-planificar, o cuando esté empezando a crear un bot de WhatsApp y necesite definir qué hará
  el asistente, qué NO hará, y cómo va a hablar.
---

# Etapa 1 de 9 — Planificar

La etapa más larga y la más importante. Todo lo que venga después sale de acá.

**No tiene que ser de una sentada** — de hecho es mejor
partirla en dos. Díselo al empezar para que no se sienta atrapado.

---

## Antes de la primera palabra

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md` — las 9 reglas de oro.
2. Carga `~/.claude/skills/bot-whatsapp/references/estado.md` — cómo se lleva el estado.
3. Si existe `ESTADO.md`, léelo: puede que ya hayan avanzado parte de esta etapa.

---

## Los 3 bloques

Es la etapa más larga del proceso, y la persona probablemente está trabajando mientras conversa
contigo.

🚫 **No le anuncies cuánto va a demorar.** Ni horas, ni cantidad de preguntas. Un número grande al
principio hace que lo deje para después y no vuelva.

**Al terminar cada bloque, actualiza `ESTADO.md` y OFRÉCELE PARAR.** Explícitamente, sin que él
tenga que pedirlo:

> *"Con esto ya sé todo lo que necesito de tu negocio. ¿Seguimos con cómo va a hablar tu
> asistente, o lo dejamos acá y retomamos después? Lo que llevamos ya está guardado."*

**Por qué importa:** alguien que se siente atrapado en una conversación larga abandona y no
vuelve. Alguien a quien le ofrecieron salir se queda, o vuelve al día siguiente. Ofrecer la
salida es lo que evita perderlo.

Y si en medio de un bloque lo notas cortante, apurado o respondiendo con monosílabos, ofrécele
parar ahí mismo aunque el bloque esté a medias. Lo guardas y sigues después.

### Bloque A — Seguridad y expectativas *(obligatorio, no se salta)*

Carga `~/.claude/skills/bot-whatsapp/references/seguridad.md`, **Parte A**.

Las 7 protecciones en lenguaje humano, en **un solo mensaje**, cortas. No hagas 7 turnos con esto.

🚫 **No es una lista de riesgos, es una lista de lo que ya viene resuelto.** El texto exacto está
en la referencia y hay que usar ese: la diferencia entre *"alguien te puede vaciar la cuenta"* y
*"tú pones un tope de gasto y se apaga solo"* es la diferencia entre que la persona siga o se vaya.

Después, lo que el bot **no** va a poder hacer. Es mejor decepcionar acá que en la etapa de
pruebas.

**Cierra preguntando:** *"¿Te hace sentido seguir sabiendo esto?"*

⚠️ Si quiere saltarse la seguridad, aplica la regla 6: no se salta. Ofrece hacerlo rápido.

### Bloque B — Las 13 preguntas

Carga `~/.claude/skills/bot-whatsapp/references/descubrimiento.md`.

**Una pregunta por turno.** Sin excepciones. Son 13 preguntas y son 13 turnos.

⚠️ **Atajo obligatorio:** si en la pregunta 1 el rubro roza la salud (estética, dental, consulta,
kinesiología, nutrición, psicología), salta de inmediato a la pregunta 13 y vuelve después.
Cambia el régimen legal del proyecto completo.

Produce la **Ficha del Bot** y guárdala en `ESTADO.md`.

### Bloque C — El guion

Carga `~/.claude/skills/bot-whatsapp/references/conversacion.md`.

Empieza por **las 5 reglas duras** del guion — cuatro vienen de contratos con Meta y Anthropic, y
una viene de la plata. No son de estilo y no se negocian.

Todo lo que le muestres tiene que parecerse a **un chat de WhatsApp**. Si le muestras una lista
de parámetros, perdiste.

---

## El gate de la etapa

Dos cosas, y las dos las tiene que hacer el usuario:

- [ ] **Leyó la Ficha del Bot** y la aprobó o la corrigió
- [ ] **Leyó las 3 conversaciones de ejemplo** completas y las aprobó

Si te dice "sí sí, está bien" sin haber mirado, insiste una vez: *"en serio, léela — es lo único
que va a saber tu asistente"*.

---

## Si algo no aparece

| Debería ver | Si no pasa |
|---|---|
| Las 7 protecciones, en un mensaje corto | Si te salió largo, lo estás haciendo mal: es la versión corta primero |
| Su Ficha del Bot, para leer y aprobar | Si dice "sí sí" sin leerla, insiste una vez. Es lo único que su asistente va a saber |
| 3 conversaciones de ejemplo | Si no las reconoce como su negocio, corrige y **vuelve a mostrárselas** |
| Se traba en las preguntas frecuentes | Es el punto donde más gente abandona. Sácale dos de memoria y sigue |

Si pasa algo que no está en esta tabla, **no le pases el problema al usuario**: arréglalo y
cuéntale solo lo que necesita saber.

---

## Al cerrar

1. Actualiza `ESTADO.md`: etapa Planificar cerrada, Ficha del Bot completa, siguiente comando.
2. Manda al siguiente paso:

> *"Listo, tu asistente ya tiene personalidad y sabe qué decir. Ahora te muestro cuánto cuesta
> esto de verdad, antes de construir nada. Escribe **`/bot-costos`**."*
