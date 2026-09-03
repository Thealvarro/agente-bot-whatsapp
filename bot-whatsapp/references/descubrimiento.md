# Descubrimiento del negocio — las 13 preguntas

**Objetivo:** salir de esta fase con una **Ficha del Bot** aprobada — un documento corto, en
español simple, que define qué hace el asistente, qué **no** hace, y quién responde cuando él no
puede.

**Regla de la fase:** una pregunta por turno. Sin excepciones. Son 13 preguntas y son 13 turnos.

⚠️ **Atajo obligatorio:** si en la pregunta 1 el rubro roza la salud o el cuerpo, **salta de
inmediato a la pregunta 13** y vuelve después. Cambia el régimen legal del proyecto completo y
conviene saberlo temprano, no al final.

Cuenta como tal: estética, dental, consulta médica, kinesiología, nutrición, psicología,
**peluquería, barbería, podología, masajes, tatuajes y micropigmentación**.

**Ojo con los que no son obvios.** Una peluquería parece inofensiva hasta que te acuerdas de que
pregunta por alergias a las tinturas y por el estado del cuero cabelludo, y que las clientas
mandan **fotos de su pelo**. Eso es información de salud y son imágenes corporales. Si dudas de
si el rubro califica, salta igual a la 13: preguntar de más cuesta un turno, y no preguntar
cuesta la infracción más grave de la ley de datos.

**Tono:** esto es una conversación, no un formulario. Reacciona a lo que te cuenta. Si dice algo
que cambia el panorama, profundiza ahí antes de seguir con la lista.

---

## Antes de la primera pregunta

Encuadra la fase en dos frases:

> *"Ahora te voy a hacer unas preguntas sobre tu negocio. No son técnicas — son para que el
> asistente hable como tú y sepa lo que tiene que saber. Vamos de a una."*

---

## Las 13 preguntas

*(La 4 tiene dos partes que van en el mismo turno: el proceso actual y el volumen de mensajes.)*

### 1. ¿Qué es el negocio?

*"Cuéntame qué hace tu negocio, en tus palabras."*

**Qué buscas:** rubro, tamaño, si es de él o de un cliente suyo.

**Ojo:** si el bot es para un cliente de él, anótalo — cambia `/bot-entregar` completa y cambia quién
responde legalmente por los datos.

---

### 2. ¿Quién te escribe hoy por WhatsApp?

*"¿Qué tipo de persona te escribe? ¿Son clientes nuevos preguntando, clientes que ya te
compraron, o de todo un poco?"*

**Qué buscas:** la proporción entre gente nueva y gente conocida. Cambia completamente el guion:
a un cliente nuevo hay que presentarse y calificarlo; a uno que ya compró hay que reconocerlo.

---

### 3. ¿Cuáles son las preguntas que más te hacen?

*"De todo lo que te preguntan por WhatsApp, ¿cuáles son las 5 o 6 que se repiten hasta el
cansancio?"*

**Esta es la pregunta más importante de la fase.** Esas preguntas repetidas son el 80% del valor
del bot.

**Si no las tiene claras**, hay un orden que importa. 🚨 **Este es el punto donde más gente
abandona el proceso completo**, así que manéjalo con cuidado.

**Primero — sácale las que sí sabe.** Siempre sabe dos o tres, solo que no las tiene ordenadas:

> *"A ver, dime las dos que más te achacan. Esas que ya sabes qué te van a preguntar apenas ves
> el mensaje."*

Con dos o tres ya se puede avanzar. Las demás aparecen solas en el reporte semanal de la bandeja
cuando el asistente esté andando.

**Segundo — si necesitas más, háganlo JUNTOS, sin cortar la conversación:**

> *"¿Tienes el WhatsApp a mano? Abre los últimos chats y dime en voz alta qué te preguntaron. Yo
> voy anotando — no tienes que escribir nada."*

Así no se va: sigue contigo, solo cambia de app un momento.

⚠️ **Último recurso — mandarlo a hacer la tarea solo.** Solo si de verdad no puede en ese momento.
Y **nunca lo sueltes sin ancla**:

> *"Perfecto, revísalo con calma. Cuando vuelvas, escribe `/bot-planificar` y seguimos justo
> acá — ya tengo guardado todo lo que me contaste, no vas a repetir nada. ¿Te parece si lo vemos
> mañana?"*

Y **anótalo en `ESTADO.md`**, en "Esperando de [nombre]", con la fecha en que quedaron.

**Por qué tanto cuidado:** esta es la única instrucción de todo el sistema que saca a la persona
de la conversación con permiso explícito. Se va a su WhatsApp, encuentra clientes reales
esperando respuesta, y ese día se acabó. No por falta de interés: porque la vida le pasó por
encima y nadie la estaba esperando.

**Nunca sigas con una lista inventada por ti.** Pero tampoco la mandes sola si puedes evitarlo.

---

### 4. ¿Qué pasa hoy cuando alguien te escribe?

*"Hoy, sin bot: llega un mensaje. ¿Quién lo ve, en cuánto rato le contestan, y qué pasa
después?"*

**Qué buscas:** el proceso real, con sus tiempos reales. Acá salen las verdades incómodas ("a
veces contesto al otro día", "los fines de semana nadie mira"). Esas verdades son exactamente el
argumento de venta del bot.

Anota el tiempo de respuesta actual. Sirve para medir el éxito en la pregunta 12.

### 4b. ¿Cuánta gente te escribe? *(en el mismo turno)*

⚠️ **Este dato es obligatorio: sin él, la tabla de costos de `/bot-costos` es una adivinanza.**

No preguntes "¿cuántas conversaciones al mes tienes?" — nadie lleva esa cuenta. Pregunta algo
que sí se pueda responder:

> *"¿Y más o menos cuántas personas distintas te escriben en un día normal? No necesito el
> número exacto, un promedio a ojo."*

**Si no tiene idea**, dale anclas concretas para que elija:

> *"¿Dirías que son como 5 al día, como 15, o más de 30?"*

**Y valídalo con algo que sí sabe:** *"¿cuántas clientas atiendes en un día bueno?"*. El número de
mensajes suele ser parecido o un poco mayor.

**Conviértelo tú** y anótalo en la ficha: 5/día ≈ 150 al mes · 15/día ≈ 450 · 30/día ≈ 900.

**Nunca le muestres la tabla de costos de 500 conversaciones a alguien que recibe 5 al día.** Se
va a asustar de gratis y no vuelve.

---

### 5. ¿Qué vendes y a qué precio?

*"Necesito tu lista de servicios o productos con precios. Los que sean — aunque sean 'desde tanto'."*

⚠️ **Punto crítico.** Si no hay precios definidos, el asistente **no puede inventarlos**. Las
opciones son:

- **A)** Define precios ahora, aunque sean rangos ("desde $X").
- **B)** El bot no habla de precios y escala a un humano cada vez que preguntan. Funciona, pero
  pierde buena parte de la gracia, porque el precio es casi siempre la primera pregunta.

Presenta las dos y deja que elija. No decidas tú por él.

---

### 6. ¿Cuál es tu horario de atención?

*"¿Qué días y a qué hora atienden?"*

**Y en el turno siguiente**, no en el mismo — son dos preguntas y la regla es una por turno:

> *"¿Y qué prefieres que pase cuando alguien te escribe fuera de ese horario? Tres opciones:
> que responda igual como si nada, que responda avisando que están cerrados y que mañana lo
> contactan, o que solo tome el dato y no prometa nada."*

**Qué buscas:** el horario real, y la decisión de qué hace el asistente de noche. La segunda
opción es la que mejor funciona en la práctica: no pierde al interesado y no promete algo que
nadie va a cumplir a las 11 de la noche.

---

### 7. ¿Cómo agendas hoy?

*"Cuando alguien quiere una hora, ¿cómo se la das? ¿Tienes calendario, agenda de papel, te
coordinas por mensaje?"*

**Qué buscas:** si hay un calendario digital que se pueda consultar, o si el agendamiento va a
tener que pasar por un humano sí o sí.

**Si no hay calendario digital:** el bot puede tomar la solicitud y pasársela a un humano, o se
puede montar un calendario simple. Ofrece ambas, con el costo de cada una (se detalla en `/bot-costos`).

**Nunca** dejes que el bot confirme una hora que no puede verificar. Esa es la forma más rápida
de tener dos clientes en el mismo horario y un dueño enojado.

---

### 8. ¿Qué te gustaría que el asistente resuelva solo?

*"De todo lo que hablamos, ¿qué te encantaría no tener que contestar nunca más?"*

**Qué buscas:** el alcance que él quiere. Anótalo tal cual lo dice.

**Si pide demasiado** (que cierre ventas, que cobre, que negocie), no lo cortes en seco. Anótalo
y aterrízalo en la pregunta siguiente, que es donde corresponde.

---

### 9. ¿Qué NUNCA debe hacer solo?

*"Ahora al revés, y esta es la pregunta más importante de todas: ¿qué cosa, si el asistente la
hace mal, te causa un problema de verdad?"*

**Esta pregunta define los límites del sistema.** Las respuestas típicas — y todas válidas:

- Dar un descuento
- Confirmar una hora que no existe
- Prometer un resultado (médico, estético, legal)
- Hablar de temas de salud o dar diagnósticos
- Contestarle a un cliente enojado o a un reclamo
- Negociar precios
- Comprometer un plazo de entrega

Todo lo que salga acá va a la Ficha del Bot como **límite duro** y se traduce en una regla del
sistema en `/bot-probar`. No es una sugerencia al modelo: es un bloqueo.

Si en la pregunta 8 pidió algo que acá aparece como prohibido, muéstrale la contradicción con
calma y que resuelva él.

---

### 10. ¿Quién es el humano de respaldo?

⚠️ **Normaliza la respuesta ANTES de preguntar.** En la mayoría de los negocios chicos el humano
de respaldo es el dueño, y punto. Si preguntas en seco "¿quién es tu humano de respaldo?", la
persona que trabaja sola siente que le están diciendo que su negocio es demasiado chico para
esto. Y quien se siente chico, se va.

Pregúntalo así:

> *"Cuando el asistente diga 'déjame consultarlo', ese aviso le tiene que llegar a alguien. En la
> mayoría de los negocios es el dueño mismo — o sea tú. ¿Te lo mando a ti, o hay alguien más del
> equipo que contesta mensajes?"*

**Qué buscas:** una persona concreta y un canal que **realmente mire**. Un correo que nadie abre
no sirve de nada.

**El seguimiento, también con cuidado.** No preguntes "¿y si estás de vacaciones?" como si fuera
una falla del negocio. Preséntalo como algo que el asistente resuelve:

> *"Y si estás con un cliente y no puedes mirar el teléfono, ¿prefieres que el asistente le diga
> a la persona que le respondes apenas te desocupes, o que le dé un horario concreto?"*

Así la respuesta útil sale igual, sin que nadie tenga que confesar que trabaja solo.

Si no hay plan B, anótalo en la ficha sin dramatizar — es lo normal en un negocio de dos personas,
no un defecto.

---

### 11. ¿Qué es lo que más miedo te da que pase?

*"Si esto sale mal, ¿qué es lo peor que se te viene a la cabeza?"*

**Por qué esta pregunta:** te dice dónde poner el esfuerzo, y te da el guion de `/bot-probar`. Lo que
él teme se convierte en una prueba específica que va a ver pasar con sus propios ojos.

También destapa miedos que no son técnicos ("que los clientes se den cuenta de que es un robot y
se sientan estafados"), que se resuelven con el guion y con el aviso, no con código.

---

### 12. ¿Cómo vas a saber en un mes que valió la pena?

⚠️ **No preguntes por "métricas" ni por "indicadores".** Es idioma de consultor y hace sentir a la
persona que está en una reunión donde no debería estar. Nadie que corta pelo mide nada, y no tiene
por qué.

Pregúntalo con opciones concretas, que son mucho más fáciles de responder que una pregunta
abierta:

> *"Una última. En un mes, ¿qué tendría que haber pasado para que digas 'esto valió la pena'? Te
> tiro tres que le pasan a casi todos, dime cuál te suena más:*
>
> *· Que no se te escape gente que escribe cuando estás ocupado o cerrado*
> *· Que dejes de contestar las mismas preguntas mil veces*
> *· Que te lleguen más reservas"*

**Después, aterrízalo a un número que él pueda ver.** Si eligió la primera:

> *"¿Y más o menos cuánta gente crees que se te pierde así al mes? ¿Dos, cinco, más?"*

Con eso ya tienes con qué comparar en la revisión del día 7 — sin haber dicho nunca la palabra
"métrica".

Sin esto, en un mes nadie sabe si el bot sirvió, y no hay forma de justificar el gasto ni de
subirle el precio al cliente.

---

---

### 13. ¿Se va a hablar de salud? ⚠️

*"¿Tus clientes te van a contar cosas sobre su salud por WhatsApp? Cosas como condiciones de la
piel, alergias, si están tomando algún medicamento, si están embarazadas, ese tipo de cosas."*

**Por qué esta pregunta cambia el proyecto entero:** en Chile, la información de salud es **dato
sensible**. Guardarla sin autorización expresa es la infracción más grave de la ley de datos
—hasta 20.000 UTM— y **no basta con el "interés legítimo"**: se necesita consentimiento expreso,
pedido y guardado.

Y hay una segunda capa: **Anthropic prohíbe por contrato que el asistente dé consejo de salud**
sin que un profesional revise. No es opcional.

**Si la respuesta es sí** — y en una estética o una dental casi siempre lo es:

Explícale en lenguaje simple, sin asustarlo:

> *"Entonces tu asistente va a tener dos reglas especiales. Primera: antes de preguntarle a
> alguien por su piel o su salud, le va a pedir permiso explícito y va a guardar ese permiso.
> Segunda: no va a recomendar tratamientos ni decir qué le sirve a quién — eso lo deriva a ti o a
> tu equipo. Puede informar qué servicios tienen, cuánto cuestan y agendar, que es el 90% de lo
> que la gente pregunta igual."*

**Y agrégale la advertencia de las fotos:**

> *"Ojo con algo: la gente te va a mandar fotos de su piel. Eso es lo más delicado que puede pasar
> por ahí. Vamos a definir juntos qué hacemos con esas fotos, porque guardarlas sin permiso
> explícito es meterse en un problema serio."*

**Registra en la ficha:** si maneja datos de salud, y qué se hace con las fotos.

**Si la respuesta es sí, esto se activa después:**
- El texto de consentimiento de `legal-chile.md` (sección 4, texto B)
- La prohibición de consejo de salud en el guion de `/bot-planificar`
- El registro de consentimiento por separado en `/bot-probar`
- La conversación sobre contrato de encargo en `/bot-entregar`

---

## La Ficha del Bot

Cuando tengas las 13 respuestas, arma la ficha y **muéstrasela completa**. Formato exacto:

```
FICHA DEL ASISTENTE — [Nombre del negocio]

QUÉ ES EL NEGOCIO
[una o dos frases]

A QUIÉN ATIENDE
[tipo de cliente]

CUÁNTA GENTE ESCRIBE
[N] personas al día ≈ [N×30] conversaciones al mes
Tiempo de respuesta hoy: [lo que dijo en la pregunta 4]

LO QUE EL ASISTENTE RESUELVE SOLO
· [cosa 1]
· [cosa 2]
· [cosa 3]

LO QUE EL ASISTENTE NUNCA HACE SOLO
· [límite 1]
· [límite 2]
· [límite 3]

HORARIO
Atención: [días y horas]
Fuera de horario: [qué hace]

PRECIOS QUE PUEDE DECIR
[lista, o "ninguno — escala siempre"]

CÓMO SE AGENDA
[el mecanismo]

HUMANO DE RESPALDO
[nombre] — se le avisa por [canal]
Plan B si no está: [plan, o "sin plan B definido"]

CÓMO MEDIMOS EL ÉXITO
[la métrica del mes 1]

¿SE HABLA DE SALUD?
[sí/no] — Fotos de tratamientos: [qué se hace con ellas]

RIESGOS ACEPTADOS
[vacío por ahora — acá se anota lo que el usuario decida asumir]
```

Preséntala así:

> *"Esta es la ficha de tu asistente. Léela completa, porque todo lo que construya de acá en
> adelante sale de esto. ¿Está bien, o hay algo que corregir?"*

**Gate de la fase:** el usuario leyó la ficha y la aprobó o la corrigió.

No avances con una ficha que no leyó. Si te dice "sí sí, está bien" sin haberla mirado, insiste
una vez: *"en serio, léela — es lo único que va a saber tu asistente"*.

---

## Guarda la ficha

La Ficha del Bot es la fuente de verdad del proyecto. Guárdala como archivo y actualízala cada
vez que algo cambie. En `/bot-entregar` es parte de lo que se le entrega al cliente.
