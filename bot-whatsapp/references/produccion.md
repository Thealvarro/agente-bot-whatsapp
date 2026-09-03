# Encender el asistente — la etapa de publicar

Dos fases en un archivo porque son continuas: encender y acompañar.

---

# Antes de encender

## Antes de encender: la lista de las 12

Recórrela **con el usuario**, no por tu cuenta. Cada punto se confirma en voz alta.

- [ ] 🚨 **Método de pago registrado** en la cuenta de WhatsApp Business. **Verifícalo tú, no te
      quedes con un "sí, ya lo puse".** Sin esto, desde el 1 de octubre de 2026 el bot deja de
      entregar respuestas y el cliente no se entera.
- [ ] 🚨 **El bot no responde fuera del tema del negocio.** Lo comprobaste en la prueba 6d. Es
      exigencia de Meta, no preferencia de estilo.
- [ ] **Contrato de encargo firmado**, si el bot es para un tercero. Ver `entrega-cliente.md`.
- [ ] **Las 14 pruebas pasaron.** Todas. Ver `pruebas.md`.
- [ ] **El usuario sabe apagarlo solo**, sin preguntarte cómo. Ya lo demostró en la prueba 13.
- [ ] **El tope de gasto está puesto** y el usuario sabe cuál es el número.
- [ ] **El humano de respaldo está avisado** de que desde hoy le van a llegar derivaciones. No
      des por hecho que se enteró: que el usuario le escriba.
- [ ] **Los avisos legales están instalados** — ver `legal-chile.md`.
- [ ] **El aviso de "te atiende un asistente"** está en el primer mensaje.
- [ ] **El modo borrador está activo** (o el usuario decidió lo contrario, con la advertencia
      dada).
- [ ] **El número es el definitivo.** No se sale a producción en un número de prueba.
- [ ] **La Ficha del Bot está al día** con todo lo que cambió en el camino.

Si falta uno, no se enciende. Dile cuál falta y resuélvelo.

---

## El modo borrador

**Qué es, en palabras para el usuario:**

> *"Los primeros días el asistente no le va a escribir a nadie directamente. Va a preparar la
> respuesta y tú la apruebas antes de que salga. Vas a ver exactamente qué habría contestado. Si
> está bien, un toque y sale. Si está mal, lo corriges y yo ajusto."*

**Cuánto dura:** mínimo 3 días de conversaciones reales, o 20 conversaciones — lo que llegue
primero. No lo midas en horas: mídelo en conversaciones vistas.

**Por qué existe:** es la única forma de descubrir lo que las pruebas no encontraron. Los
clientes reales preguntan cosas que a nadie se le ocurrieron en `/bot-probar`.

**Cuándo se sale del modo borrador:** cuando el usuario aprueba 20 respuestas seguidas sin
corregir ninguna. Ese es el criterio, y es él quien lleva la cuenta.

⚠️ **Si el usuario quiere saltarse el modo borrador:** adviértele una vez, con un ejemplo
concreto — *"la primera respuesta rara la va a ver un cliente, no tú"*. Si insiste, es su
decisión: anótalo en la Ficha del Bot como riesgo aceptado y sigue. No pelees dos veces.

---

## El interruptor de apagado

Requisitos, no sugerencias:

- **En un solo lugar** que el usuario recuerde sin ayuda
- **Efecto inmediato**, no "en unos minutos"
- **Sin necesidad de ti**. Si el usuario tiene que escribirte para apagarlo, no existe.
- **Reversible por él mismo.** Prenderlo tiene que ser tan fácil como apagarlo.

Dale la regla de uso en una frase:

> *"Ante la duda, apágalo. Prefiero que lo apagues sin necesidad diez veces, a que lo dejes
> prendido una vez que había que apagarlo."*

---

## El tope de gasto

Pregunta directa, sin rodeos:

> *"¿Cuánto es lo máximo que estás dispuesto a gastar en un día, en el peor escenario, sin que
> te dé un infarto?"*

Toma ese número y ponlo como corte automático. Cuando se alcanza:
1. El asistente se apaga solo
2. Le llega un aviso al usuario
3. Los mensajes que entren quedan registrados para que un humano los conteste

**Regla:** un tope que solo avisa no es un tope. Tiene que cortar.

Además del tope diario, deja un **aviso al 50%** para que el usuario vea venir el problema antes
de que corte.

---

## El encendido

No lo enciendas y te vayas. Enciéndelo y quédate mirando.

**Las primeras 2 horas:**
- Que el usuario le escriba primero, como si fuera un cliente
- Revisen juntos las primeras 3 conversaciones reales que lleguen
- Confirma que las derivaciones están llegando al humano de respaldo
- Confirma que el gasto va donde debería

**Gate de la fase:** un cliente real fue atendido, el usuario vio la conversación, y sabe apagarlo
solo.


---

# LO QUE VIENE DESPUÉS

La operación diaria —la bandeja, las señales de alarma, el reporte semanal y el soltado gradual
con sus 5 métricas— vive en **`bandeja.md`**, y se usa desde los comandos `/bot-bandeja` y
`/bot-soltar`.

Acá queda solo lo que corresponde al encendido, más el hito de la primera semana.

---

## La revisión del día 7

Siéntate con el usuario y revisen 4 cosas:

**1. La métrica del éxito.** La que definió en la pregunta 12 de la Ficha del Bot. ¿Se movió?
Muéstrale el número, no una sensación.

**2. Las conversaciones que se derivaron.** ¿Fueron demasiadas? Si el asistente deriva el 80%,
está resolviendo poco y hay que enseñarle más. ¿Fueron muy pocas? Puede estar contestando cosas
que no debería.

**3. El gasto real de la semana.** Proyéctalo al mes y compáralo con lo estimado en
`/bot-costos`. Si se desvió mucho, explícale por qué. Lo más común: el asistente está respondiendo
en más mensajes de los necesarios, y eso se corrige en el guion.

**4. Qué le falta.** Ahora que lo vio andando, va a tener ideas. Anótalas en `ESTADO.md`. Las
chicas, hazlas. Las grandes, cotízalas aparte.

**Si las 5 métricas del soltado se cumplen**, díselo tú — no esperes que se le ocurra:

> *"Ya está para que responda solo. Escribe `/bot-soltar` cuando quieras."*
