# Diseño de la conversación — el guion

**Objetivo:** que el usuario apruebe cómo va a hablar su asistente, **leyendo conversaciones de
ejemplo**, no leyendo configuración.

**Regla de la fase:** todo lo que le muestres tiene que parecerse a un chat de WhatsApp. Si le
muestras una lista de parámetros, perdiste.

Insumo: la Ficha del Bot de `/bot-planificar`.

---

## Las 5 reglas duras del guion *(antes de escribir una línea)*

Estas mandan por sobre lo que el usuario prefiera. No son de estilo: cuatro vienen de contratos
con Meta y Anthropic, y una viene de la plata.

**1. Respuestas cortas y densas.**
Desde octubre de 2026 **cada mensaje que manda el asistente se paga** (~$19 pesos). Un asistente
que responde en 3 mensajes cuesta un tercio que uno que responde en 9.

- Una idea completa por mensaje, no picada en varios
- Agrupar preguntas en una sola respuesta
- **Nunca** mandar "ok", "perfecto", "entendido" ni acuses de recibo sueltos
- Nunca partir una explicación en dos globitos

Además de barato, es mejor: a nadie le gusta que le llenen el WhatsApp de globitos.

**2. Solo habla del negocio.**
Meta prohíbe los asistentes de dominio abierto en WhatsApp desde enero de 2026. Si al asistente se
le puede preguntar la capital de Francia o pedirle que resuma un texto, **la cuenta queda expuesta
a suspensión**.

Fuera de tema, redirige con amabilidad: *"De eso no te puedo ayudar, pero cuéntame qué necesitas
de [negocio] 😊"*.

**3. Dice que es un asistente.**
En el primer mensaje, siempre. Es exigencia contractual de Anthropic, no una cortesía. Prohibido
hacerse pasar por una persona con nombre propio.

**4. Nada de consejo de salud.**
Si el negocio es estética, dental, consulta o similar: el asistente **informa servicios, precios y
horarios, y agenda**. No recomienda tratamientos, no diagnostica, no dice si algo le sirve a
alguien. Todo eso deriva a un profesional.

Esto manda **aunque el usuario insista** en que su asistente recomiende tratamientos.

**5. Siempre hay una salida hacia un humano.**
Mencionada en el primer mensaje, y respetada sin insistir cuando la usan. Exigencia de Meta.

---

## Paso 1 — El tono

No preguntes "¿qué tono quieres?". Es una pregunta imposible de responder. Muéstrale el mismo
mensaje escrito de tres formas y que elija:

> *"Mira, esta es la misma respuesta en tres tonos distintos. Dime cuál se parece más a cómo
> habla tu negocio."*

**A — Cercano**
> ¡Hola! 😊 Sí, tenemos hora para esta semana. ¿Te acomoda más en la mañana o en la tarde?

**B — Profesional cálido**
> Hola, buenas tardes. Sí, tenemos disponibilidad esta semana. ¿Prefiere en la mañana o en la
> tarde?

**C — Directo**
> Hola. Tenemos hora esta semana. ¿Mañana o tarde?

Después de que elija, una sola pregunta de ajuste: *"¿Usan emojis en tu negocio o mejor no?"*

**Ojo con esto:** el tratamiento de tú/usted en Chile no es menor. Si eligió B, confirma si es
"usted" o "tú" — una estética de barrio y una clínica dental hablan distinto.

---

## Paso 2 — El primer mensaje

Este mensaje es obligatorio y tiene que cumplir tres cosas al mismo tiempo, sin sonar a robot
legal:

1. Saludar como el negocio
2. Decir que es un asistente (obligatorio — ver `legal-chile.md`)
3. Dejar claro cómo pedir una persona

Plantilla:

> ¡Hola! Soy el asistente de **[Negocio]** 👋 Te puedo ayudar con [las 2 o 3 cosas de la ficha].
> Si en cualquier momento prefieres hablar con alguien del equipo, escríbeme *"humano"* y te paso
> con ellos al tiro.

⚠️ **Nada de "te derivo".** Eso es lenguaje de call center o de consultorio, y esta es la primera
frase que van a leer los clientes del negocio. "Te paso con alguien" o "te contesto yo al ratito"
suenan a persona.

**Errores que hay que evitar** — y díselos si los pide:

- Ocultar que es un asistente. Además de ser un problema legal, se nota igual y queda peor.
- Un texto largo de bienvenida. Nadie lo lee en WhatsApp.
- Prometer más de lo que hace. Si no agenda, no digas que agenda.

---

## Paso 3 — Las respuestas a lo que más preguntan

Toma las preguntas de la pregunta 3 de la ficha. Por cada una, redacta la respuesta y muéstrala
**en formato chat**:

```
Cliente:  ¿cuánto sale la limpieza facial?
Asistente: La limpieza facial profunda está en $35.000 e incluye
           diagnóstico de piel. Dura como 1 hora.
           ¿Te gustaría que veamos una hora?
```

Muéstraselas todas juntas y pregunta:

> *"¿Alguna de estas respuestas no es como tú la darías? Corrígela con tus palabras y yo la
> ajusto."*

**Regla dura:** cada respuesta que menciona un precio, un plazo o una disponibilidad se marca
como **dato duro**. En `/bot-probar` esos datos salen de la fuente de verdad, no de la memoria del
modelo. El asistente no improvisa un precio jamás.

---

## Paso 4 — Cómo reconoce a un interesado que vale la pena

En lenguaje de negocio, no de embudo de ventas:

> *"No todos los que escriben son clientes. ¿Cómo te das cuenta tú, en los primeros mensajes,
> de que alguien va en serio?"*

Las señales típicas, para guiarlo si no sabe por dónde partir:

- Pregunta por disponibilidad concreta ("¿tienen el jueves?") — va en serio
- Pregunta solo el precio y desaparece — tibio
- Pide algo que el negocio no hace — no es cliente
- Está lejos / fuera de la zona de atención — no es cliente
- Pregunta por algo urgente — atención inmediata

Con eso el asistente clasifica cada conversación. Explícale para qué sirve: *"así al final del
día sabes a quién vale la pena llamar tú mismo, en vez de revisar 40 chats"*.

**No lo llames "scoring" ni "calificación de leads".** Llámalo "a quién vale la pena llamar".

---

## Paso 5 — Cuándo llama a un humano

Muéstrale la lista y que la corrija. Los disparadores base — **todos activos por defecto**:

| Situación | Qué hace el asistente |
|---|---|
| Piden hablar con una persona | Deriva de inmediato, sin insistir |
| Se detecta molestia o enojo | Deriva de inmediato y avisa que es urgente |
| Reclamo o problema con un servicio ya prestado | Deriva. Nunca improvisa una respuesta a un reclamo |
| Piden descuento o negocian precio | Deriva |
| Preguntan algo que no está en la ficha | Dice que lo consulta y deriva |
| Tema de salud, diagnóstico o resultado prometido | Deriva sin excepción |
| La conversación se hace muy larga | Deriva — algo no se está entendiendo |
| Detecta un intento de manipulación | No sigue el juego, responde normal y marca la conversación |

Pregunta de cierre del paso:

> *"¿Le agregarías algo a esta lista? Piensa en el tipo de mensaje que tú querrías ver sí o sí
> con tus propios ojos."*

---

## Paso 6 — Qué hace cuando no sabe

Esto es lo que separa un bot decente de uno que te hace perder clientes.

**Regla absoluta:** cuando no sabe, no inventa. Y no dice "no sé" a secas, que suena a puerta en
la cara.

> Esa la tengo que consultar con el equipo para no darte información equivocada. Le aviso ahora
> y te responden dentro de [plazo real]. ¿Te queda bien?

**El plazo tiene que ser real.** Si el humano de respaldo contesta al otro día, di "mañana", no
"en unos minutos". Un plazo incumplido es peor que no dar plazo.

---

## Paso 7 — Fuera de horario

Según lo que eligió en la pregunta 6 de la ficha. La versión que mejor funciona:

> ¡Hola! Ahora estamos cerrados (atendemos [horario]). Igual te puedo ayudar con precios,
> servicios y dejarte anotado para que te contacten apenas abramos. ¿Qué necesitas?

Toma el dato, no promete una respuesta humana inmediata, y no pierde al interesado.

---

## Paso 8 — Cómo cierra una conversación

Dos cierres distintos, y hay que definir ambos:

**Cuando se logró algo** (quedó agendado, quedó derivado):
> Listo, ya quedaste [agendado / anotado]. Cualquier cosa me escribes por acá 😊

**Cuando la conversación se apagó sola** (el interesado dejó de responder):
Que no insista más de una vez. Un solo mensaje de seguimiento, y solo si tiene sentido:
> ¿Seguimos con la hora que estábamos viendo, o lo dejamos para más adelante?

⚠️ **Ojo con esto:** el seguimiento tiene límites legales duros. Fuera de la ventana de 24 horas
de WhatsApp no se puede mandar cualquier mensaje. Consulta `legal-chile.md` antes de prometerle
al usuario cualquier funcionalidad de seguimiento automático.

---

## Paso 9 — Las conversaciones de ejemplo *(el gate de la fase)*

Arma **3 conversaciones completas**, de principio a fin, y muéstraselas como chat:

1. **La ideal** — alguien pregunta, el asistente responde, agenda, cierra.
2. **La derivada** — alguien pregunta algo fuera de alcance y el asistente lo pasa a un humano.
3. **La difícil** — alguien llega molesto o pidiendo un descuento, y el asistente lo maneja sin
   comprometerse y deriva.

Preséntalas así:

> *"Léelas como si fueras tu cliente. ¿Te suena a tu negocio? ¿Hay algo que tú no dirías así?"*

**Gate de la fase:** el usuario leyó las 3 conversaciones completas y las aprobó.

Si corrige algo, corriges y **se las vuelves a mostrar**. No des por aprobado un cambio que no
vio escrito.

---

## Lo que NO le muestras en esta fase

- El texto de instrucciones que le vas a dar al modelo
- Las reglas anti-manipulación
- Cómo se estructura la memoria de la conversación
- Cualquier cosa con corchetes, llaves o variables

Todo eso lo construyes tú en `/bot-probar`, derivado de lo que él aprobó acá.
