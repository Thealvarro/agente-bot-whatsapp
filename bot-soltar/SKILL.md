---
name: bot-soltar
description: >
  Etapa 8 del sistema de bot de WhatsApp. Evalúa las 5 métricas de madurez y pasa el asistente de
  modo borrador a automático, por partes y en orden: primero responder en horario, después fuera
  de horario, y al final agendar solo. Úsalo cuando el usuario escriba /bot-soltar, o cuando
  quiera que su bot conteste sin aprobación previa.
---

# Etapa 8 de 9 — Soltar

Pasar de "el bot propone y tú apruebas" a "el bot responde solo". **Por partes, nunca todo
junto.**


---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md` — de ahí salen las métricas.
3. Carga `~/.claude/skills/bot-whatsapp/references/bandeja.md`, **Parte 2**.

---

## 1. Muéstrale las 5 métricas con sus números reales

No opines antes de mostrar los números:

```
¿ESTÁ LISTO PARA SOLTARLO?

Días con bandeja abierta     9 de 7    ✓
Respuestas revisadas        34 de 20   ✓
Aprobadas sin corregir      82% de 80% ✓
Errores de precio            0          ✓
Errores de agenda            0          ✓

Está listo.
```

Si alguna está en rojo, dilo con el detalle de qué pasó:

> *"Todavía no: el jueves ofreció una hora que estaba ocupada. Lo arreglo y lo vemos mañana."*

⚠️ Si quiere soltarlo igual con métricas en rojo, dile qué pasa si eso falla sin nadie mirando. Si
insiste, va a RIESGOS ACEPTADOS y sigues. No pelees dos veces.

---

## 2. Suelta un paso, no los tres

| Paso | Qué se suelta | Requisito |
|---|---|---|
| **1** | Responder **dentro** del horario | Las 5 métricas |
| **2** | Responder **fuera** de horario | Paso 1, 3 días sin incidentes |
| **3** | **Agendar** solo | Paso 2 estable y cero errores de agenda en 2 semanas |

**Nunca al revés.** De noche nadie está mirando, y agendar es lo que más caro sale cuando falla.

Si viene a soltar el paso 2 o 3, verifica el requisito del paso anterior antes de habilitarlo.

---

## 3. Lo que NO se suelta nunca

Los límites duros de la Ficha del Bot siguen derivando a un humano **por siempre**, sin importar
qué tan bien responda:

- Descuentos y negociación de precios
- Reclamos
- Promesas de resultado
- Temas de salud
- Todo lo que el usuario puso en "lo que nunca hace solo"

Recuérdaselo al soltar, para que no piense que soltó todo:

> *"Ojo: sigue derivándote los reclamos, los descuentos y todo lo que definimos que no maneja
> solo. Eso no cambia nunca."*

---

## 4. Qué le dices

En una frase, sin ceremonia:

> *"Desde ahora responde solo dentro de tu horario. Tú sigues viendo todas las conversaciones,
> pero ya no tienes que aprobar cada una. El botón de apagado sigue en el mismo lugar."*

---

## El gate de la etapa

- [ ] Las 5 métricas cumplidas (o el riesgo aceptado y anotado)
- [ ] Se soltó **un solo** paso
- [ ] El usuario entiende qué sigue derivando siempre

---

## Al cerrar

1. Actualiza `ESTADO.md`: qué paso se soltó, con fecha, y cuándo se puede evaluar el siguiente.
2. Bájale la frecuencia de la rutina:

> *"Ya no necesitas entrar todos los días. Una vez por semana con **`/bot-bandeja`** basta. Y
> vuelve a mirar en serio cuando cambies precios, agregues un servicio o venga temporada alta."*

3. **Si el bot es para un cliente suyo**, mándalo a la última etapa:

> *"Como esto es para un cliente tuyo, falta la entrega: el manual, los precios y el contrato.
> Escribe **`/bot-entregar`**."*
