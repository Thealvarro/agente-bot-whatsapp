---
name: bot-bandeja
description: >
  Etapa 7 del sistema de bot de WhatsApp, y la única que se usa a diario. Muestra los borradores
  de respuesta pendientes para que el dueño los apruebe, corrija o rechace uno por uno, revisa las
  señales de alarma y genera el reporte semanal con las preguntas nuevas que el asistente no sabía
  contestar. Úsalo cuando el usuario escriba /bot-bandeja, o cuando quiera revisar qué respondió
  su bot y aprobar sus respuestas.
---

# Etapa 7 de 9 — La bandeja *(uso diario)*

**La única etapa que no se cierra.** Se usa todos los días mientras el asistente está en modo
borrador, y después queda como el lugar donde se mira cómo va.


---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md`. **El asistente tiene que estar publicado.** Si todavía no se encendió, no hay
   borradores que revisar — mándalo a `/bot-publicar`.
3. Carga `~/.claude/skills/bot-whatsapp/references/bandeja.md`.

---

## Qué haces cada vez

### 1. Los borradores pendientes, uno por uno

Muestra cada uno **en formato conversación**, con las 4 opciones: **Va · Corregir · No · Saltar**.

⚠️ **Cuando el usuario elige "Corregir", guarda su versión.** Cada corrección es él enseñándole
cómo habla su negocio, y es lo que alimenta el reporte semanal.

Si hay muchos pendientes, no los tires todos juntos. De a uno, y ofrécele parar cuando quiera:

> *"Van 8 de 15. ¿Seguimos o los dejamos para después?"*

### 2. Las 3 preguntas de la rutina

> **1. ¿Hay alguna respuesta que te dé vergüenza?**
> **2. ¿Llegaron todas las derivaciones a quien correspondía?**
> **3. ¿El gasto va donde esperabas?**

### 3. Revisar las señales de alarma

Las 5 están en la referencia. **La del cruce de conversaciones se apaga de inmediato**, sin
esperar confirmación de nadie.

### 4. Si es lunes (o pasaron 7 días): el reporte semanal

El formato completo está en la referencia. Lo importante:

- Cuántas aprobó sin cambios (el porcentaje que después habilita el soltado)
- **Qué le tocó corregir más** — patrones, no casos sueltos
- **Preguntas nuevas** que no estaban en el guion, con la respuesta que él dio

Y la pregunta que cierra el reporte:

> *"¿Quieres que le enseñe estas respuestas para que las conteste solo?"*

Si dice que sí, **aplícalas al guion y actualiza la Ficha del Bot en `ESTADO.md`**. Esto es lo que
hace que el asistente mejore de verdad — no pasa solo.

---

## Cuándo mandarlo a soltar

Cuando las 5 métricas se cumplan (están en la referencia), díselo tú. No esperes que se le ocurra:

> *"Tu asistente lleva 9 días y aprobaste 82% de sus respuestas sin corregir nada. Ya está para
> soltarlo y que responda solo. Escribe **`/bot-soltar`** cuando quieras."*

---

## Al cerrar cada sesión

Actualiza `ESTADO.md` con: borradores revisados, correcciones, y las métricas al día. Sin ese
registro no se puede evaluar el soltado después.
