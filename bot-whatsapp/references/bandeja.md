# La bandeja y el soltado

Las dos herramientas de la operación diaria. La bandeja es lo que se usa todos los días; el
soltado es lo que se hace una vez que la bandeja demostró que el asistente está listo.

---

# PARTE 1 — LA BANDEJA

## Qué es

Mientras el asistente está en modo borrador, **no le escribe a nadie directamente**. Prepara la
respuesta y espera aprobación.

La bandeja es donde el dueño ve esos borradores y decide.

---

## Dónde vive

**Una pantalla que el dueño abre desde su teléfono.** Un link que guarda como favorito, igual que
cualquier página. Sin app que instalar y sin contraseña que recordar.

🚫 **No es un comando de Claude Code.** El dueño de una peluquería no va a abrir una herramienta
de programador todos los días para aprobar respuestas — y los primeros días son justamente los
críticos. Si la bandeja vive donde él no entra, el modo borrador se abandona y el asistente se
suelta sin estar listo.

🚫 **Y el asistente tampoco le manda cada borrador por WhatsApp.** Desde octubre de 2026 **cada
mensaje que sale se paga**, así que avisarle uno por uno puede costar más que atender a los
clientes.

---

## Cómo se entera de que hay borradores

**Es una elección suya, con el precio a la vista** — igual que todo lo demás en el sistema.
Preséntale las opciones al encender, en `/bot-publicar`:

| Cómo quiere enterarse | Costo mensual aproximado |
|---|---|
| No me avises, yo reviso la pantalla | **$0** |
| Un resumen al día | 30 avisos |
| Agrupado cada 30 minutos | ~60 avisos |
| Por Telegram, cada vez | **$0** — si lo usa |
| Por WhatsApp, cada vez | ~300 avisos |

*Los avisos se cobran como cualquier mensaje. Convierte a su moneda con la tarifa de su país y
muéstrale pesos, no cantidades.*

**Recomienda el resumen diario o el agrupado.** El "cada vez" casi nunca vale lo que cuesta.

⚠️ **El riesgo que hay que decirle al elegir:** en modo borrador el cliente **no recibe respuesta
hasta que él aprueba**. Si elige "no me avises" y no mira la pantalla en tres horas, ese cliente
esperó tres horas — peor que no tener asistente.

**Por eso el sistema necesita un plazo máximo de borrador.** Si un borrador lleva demasiado sin
aprobarse, el asistente le avisa al cliente que una persona le responde en vez de dejarlo colgado.
Ese plazo se define acá, con él, y por defecto es corto.

⚠️ **Y hay que identificar al dueño por su número.** Si no, el asistente lo trata como cliente y
le empieza a ofrecer hora para cortarse el pelo en su propia peluquería.

## Las 4 decisiones por borrador

Por cada respuesta pendiente, se le muestra la conversación y la respuesta propuesta, y elige:

| Opción | Qué hace | Cuándo se usa |
|---|---|---|
| **Va** | Sale tal cual | La respuesta está bien |
| **Corregir** | Él la reescribe y sale la suya | Está cerca pero no es como él lo diría |
| **No** | No sale nada, la conversación queda para que la tome un humano | El asistente no debería haber contestado esto |
| **Saltar** | La deja para después | No tiene tiempo ahora |

⚠️ **"Corregir" es la opción más valiosa del sistema.** Cada corrección es el dueño enseñándole
cómo habla su negocio. Se guardan todas.

## Cómo se le presenta un borrador

En formato conversación, nunca como formulario:

```
Cliente (+569 xxxx 4821) · hace 3 minutos
─────────────────────────────────────────
Cliente:  hola, tienen hora para mañana en la tarde?

Tu asistente quiere responder:
  Hola! Sí, mañana tengo a las 15:00 y a las 17:30.
  ¿Cuál te acomoda?

  [Va]  [Corregir]  [No]  [Saltar]
```

## La rutina diaria

Tres preguntas, no una lista de tareas:

> **1. ¿Hay alguna respuesta que te dé vergüenza?** → la corriges y yo ajusto el guion
> **2. ¿Llegaron todas las derivaciones a quien correspondía?** → si se perdió una, hay que verlo hoy
> **3. ¿El gasto va donde esperabas?** → si se disparó, algo pasa

## Las 5 señales de alarma

Si el dueño ve cualquiera de estas, **apaga y avisa**:

| Señal | Qué significa | Qué hace |
|---|---|---|
| Responde cosas sin relación | Se rompió el entendimiento | Apaga y avisa |
| Dice precios que no son los suyos | Está inventando — lo más peligroso | Apaga y avisa **urgente** |
| **Un cliente menciona datos de otro cliente** | Se cruzaron conversaciones | **Apaga de inmediato.** Es una filtración |
| El gasto se disparó sin más clientes | Alguien está abusando | Apaga y avisa |
| Dejó de responder del todo | Se cayó algo | Avisa, contesta a mano mientras tanto |

⚠️ **La tercera se apaga sin pensarlo dos veces.** Las demás pueden esperar cinco minutos; esa no.

## El reporte semanal

Cada semana, muéstrale lo que la bandeja aprendió. **Esto es lo que convierte la operación diaria
en mejora real:**

```
SEMANA DEL [fecha] — [negocio]

Respuestas revisadas:      34
Aprobadas sin cambios:     28  (82%)
Corregidas por ti:          5
Rechazadas:                 1

LO QUE TE TOCÓ CORREGIR MÁS
· 3 veces le bajaste el tono — sonaba muy formal para tu negocio
· 2 veces agregaste el dato del estacionamiento

PREGUNTAS NUEVAS que no estaban en tu guion
· "¿atienden con Fonasa?"     → tú respondiste: [lo que contestó]
· "¿tienen delivery?"          → tú respondiste: [lo que contestó]

¿Quieres que le enseñe estas dos respuestas para que las conteste solo?
```

⚠️ **Las "preguntas nuevas" son oro.** Es lo que vive en la cabeza del dueño y nunca escribió en
ninguna parte. Capturarlas es lo que hace que el asistente mejore de verdad.

**Y recuérdale la verdad incómoda:** el asistente **no aprende solo**. Estas mejoras las aplicas
tú cuando él las aprueba. Si nadie las aplica, no pasa nada.

---

# PARTE 2 — EL SOLTADO

## Cuándo se puede soltar

**No cuando "parece que va bien".** Cuando estas 5 métricas se cumplen:

| Métrica | Mínimo | Por qué |
|---|---|---|
| Días con bandeja abierta | **7** | Menos de una semana no cubre un ciclo completo del negocio |
| Respuestas revisadas | **20** | Bajo eso no hay muestra suficiente |
| Aprobadas sin corregir, de las últimas 20 | **80%** | Si corriges 1 de cada 3, todavía no habla como tú |
| Errores de precio | **0** | Un solo precio inventado y no se suelta. Ninguno |
| Errores de agenda | **0** | Una hora inventada = dos clientes en el mismo horario |

Muéstrale las 5 con sus números reales. **Él decide**, pero decide informado:

```
¿ESTÁ LISTO PARA SOLTARLO?

Días con bandeja abierta     9 de 7    ✓
Respuestas revisadas        34 de 20   ✓
Aprobadas sin corregir      82% de 80% ✓
Errores de precio            0          ✓
Errores de agenda            1          ✗  ← el jueves ofreció una hora ocupada

Todavía no. Arreglo lo de la agenda y lo vemos de nuevo mañana.
```

⚠️ **Si el usuario quiere soltarlo con métricas en rojo:** dile cuál está en rojo y qué pasa si
eso falla sin nadie mirando. Si insiste, es su decisión — a RIESGOS ACEPTADOS. No pelees dos
veces.

## Se suelta por partes, nunca todo junto

**El orden importa, de menos a más riesgoso:**

| Paso | Qué se suelta | Se puede dar cuando… |
|---|---|---|
| **1** | **Responder** dentro del horario de atención | Las 5 métricas se cumplen |
| **2** | **Responder** fuera de horario | Paso 1 lleva 3 días sin incidentes |
| **3** | **Agendar** solo | Paso 2 estable y cero errores de agenda en 2 semanas |

**Nunca al revés.** De noche nadie está mirando, y agendar es lo que más caro sale cuando falla.

**Lo que NO se suelta nunca:** los límites duros de la Ficha del Bot. Descuentos, promesas,
reclamos y temas de salud siguen derivando a un humano por siempre, sin importar qué tan bien
responda.

## Qué le dices al soltar

En una frase, sin ceremonia:

> *"Desde ahora responde solo dentro de tu horario. Tú sigues viendo todas las conversaciones,
> pero ya no tienes que aprobar cada una. El botón de apagado sigue en el mismo lugar."*

## Después de soltar

- La bandeja **no desaparece**: sigue mostrando lo que el asistente derivó y lo que respondió.
- La rutina baja de diaria a semanal.
- **Cuándo volver a mirar en serio:** cambio de precios, servicio nuevo, o temporada alta.
