# Reglas que no pusiste tú — Meta, Anthropic y datos personales

**Esto aplica en todos los países.** Son condiciones contractuales de Meta y Anthropic, iguales
en Santiago, Ciudad de México o Madrid.

Lo que cambia según dónde esté el negocio —la ley de datos, las tarifas por mensaje, la autoridad
del consumidor— va en el anexo de su país. Ver el final de este archivo.

Se consulta en cinco momentos: al dar el brief, en la pregunta del rubro, al armar el guion, al
conectar el número y antes de encender.

⚠️ **Esto es investigación, no asesoría legal.** Al final está la lista de dónde se necesita
abogado de verdad. Datos verificados a agosto de 2026.

---

# LO QUE NO PUEDE FALLAR — resumen

1. **Meta prohíbe los bots de IA de propósito general.** El system prompt tiene que estar acotado
   al negocio. Es cumplimiento de términos, no una decisión de diseño.
2. **Anthropic obliga a declarar que es una IA.** Meta no lo exige; Anthropic sí, por contrato.
3. **Anthropic prohíbe que el bot dé consejo de salud** sin revisión de un profesional.
4. **Meta exige una vía clara para hablar con una persona.**
5. **Si el negocio toca salud o el cuerpo, los datos que guarda son delicados** y casi todas las
   leyes del mundo los tratan aparte. Ese es el riesgo grande, no los teléfonos.

---

# 1. LO QUE EXIGE META

## 1.1 La ventana de 24 horas

Cuando un cliente escribe, se abre una ventana de 24 horas, y se reinicia con cada mensaje nuevo
suyo.

| | Dentro de la ventana | Fuera de la ventana |
|---|---|---|
| Qué puedes mandar | Cualquier mensaje libre | **Solo plantillas pre-aprobadas** |
| Costo hasta 30-sep-2026 | Gratis | Se paga la plantilla |
| Costo desde 1-oct-2026 | **Se paga por mensaje** | Se paga |

**Si la violas:** no hay multa — la API rechaza el mensaje con error (`131026`). El riesgo real es
abusar de plantillas para evadirla; eso sí gatilla bloqueo.

El proveedor de mensajería no expone cuándo vence la ventana. Hay que calcularla desde la fecha
del último mensaje entrante.

## 1.2 🚨 El cambio del 1 de octubre de 2026 y su fecha límite

Meta lo anunció el 10 de agosto de 2026:

> *"Effective October 1, 2026, Meta will charge for service messages, which have not been charged
> since November 2024."*

**Cada respuesta libre del bot dentro de la ventana pasa a cobrarse.** Los mensajes entrantes del
cliente siguen gratis, y la ventana de 72 horas por anuncios Click-to-WhatsApp se mantiene
gratuita.

**Y hay una fecha límite dura:**

> *"For any Solution Provider or directly-integrated business that does not have a payment method
> on file by September 30, 2026, Meta will stop delivering service messages as of when they become
> charged on October 1, 2026."*

🚨 **Sin método de pago registrado en la cuenta de WhatsApp Business al 30 de septiembre de 2026,
el bot deja de entregar respuestas el 1 de octubre.** No falla con error visible: el cliente
escribe y la respuesta nunca llega.

**Las tarifas cambian mucho por país** — ver el anexo local. Como referencia del rango: el
marketing va de USD 0,0125 en Colombia a USD 0,1597 en Países Bajos, más de 12 veces de
diferencia.

## 1.3 El diseño reactivo — la decisión que hace barato todo

**El negocio publica el número del bot y el cliente escribe primero.** Nunca al revés.

No es un detalle operativo: es lo que mantiene el sistema barato y simple.

| Un bot reactivo | Un bot que inicia conversaciones |
|---|---|
| Sin límites de contactos por día | Tope de 250 contactos únicos/24 h al empezar |
| Sin verificación de negocio para funcionar | Verificación obligatoria para subir el tope |
| El consentimiento existe: el cliente escribió | Necesitas opt-in registrado y demostrable |
| Solo pagas por responder | Pagas plantillas de marketing, las más caras |
| Nada que te haga perder el número | La causa #1 de bloqueo es el envío masivo |

**Si el negocio quiere mandar promociones**, todo lo de la columna derecha se activa de golpe. Se
puede, pero es otro proyecto: presupuesto aparte, verificación de negocio, plantillas aprobadas y
las obligaciones de publicidad de su país.

## 1.4 Plantillas

Obligatorias siempre que el negocio inicie la conversación, o pasadas las 24 horas.

Tres categorías: **marketing** (promos, la más cara), **utility** (confirmaciones, recordatorios)
y **authentication** (códigos).

**Aprobación:** las primeras de una cuenta nueva demoran 24–48 horas; después bajan a minutos.
**No hay apelación formal** si te rechazan: corriges y reenvías.

**Por qué rechazan:** meter texto promocional en una plantilla marcada como *utility* (Meta revisa
la categoría antes que el contenido), variables mal formadas, faltas de ortografía, mayúsculas
excesivas.

⚠️ **Categoriza honestamente.** Marcar marketing como utility para pagar menos es la vía rápida a
que te bajen la calidad de la cuenta.

## 1.5 Opt-in

Meta pide dos cosas: que la persona haya dado su número, y que haya un permiso confirmando que
quiere recibir mensajes **de ese negocio**. El aviso debe nombrar el negocio y cumplir la ley
local.

No tiene que ser dentro de WhatsApp — vale web, formulario en papel, código QR, en persona.

⚠️ **Meta es flexible; las leyes de datos locales suelen ser más exigentes. Cumplir Meta no es
cumplir tu país.**

## 1.6 🚨 Meta prohíbe los bots de IA de propósito general

**Vigente para todas las cuentas desde el 15 de enero de 2026.**

**Prohibido:** asistentes de dominio abierto tipo ChatGPT usando WhatsApp como canal. Definición
de Meta: corre sobre un modelo de lenguaje, admite conversación de dominio abierto, **no está
restringido a un proceso de negocio específico**.

**Permitido y fomentado:** bots que un negocio corre para sus propios clientes — soporte,
agendamiento, seguimiento de pedidos, calificación de interesados, ventas.

| | |
|---|---|
| ✅ Bot que agenda horas, responde precios, explica servicios y deriva | **Cumple** |
| ❌ Bot al que le puedes preguntar "¿cuál es la capital de Francia?" | **Expone a suspensión** |

**Acción obligatoria:** el system prompt acota el dominio y rechaza lo que se salga del negocio.
Se verifica en la prueba 6d.

## 1.7 Qué hace que te bajen el número

Por frecuencia real:

1. **Mensajes masivos sin consentimiento.** Causa #1.
2. **Tasa alta de bloqueos y reportes.** La calidad cae en horas.
3. **Versiones no oficiales de WhatsApp.** Baneo sin excepciones.
4. **Nombre visible inconsistente** con la marca real.
5. **Registrar en la API un número con cuenta personal activa.** Hay que borrarla primero.
6. **Suplantar a otro negocio** o contenido prohibido.

**El bloqueo va asociado al número**, no a la cuenta ni al dispositivo.

## 1.8 Calidad y límites

**Calificación de calidad:** últimos 7 días, según bloqueos y reportes. Verde / amarillo / rojo.

**Estados:** *Connected* · *Flagged* (calidad baja, 7 días para recuperar) · *Restricted* (tope
diario alcanzado; puedes seguir respondiendo entrantes).

**Niveles** — destinatarios únicos que puedes **iniciar** por 24 h: 250 → 2.000 → 10.000 →
100.000 → ilimitado. **No aplican a un bot reactivo.**

⚠️ Desde octubre de 2025 los límites son **por portafolio de negocio**, no por número.

⚠️ **No confirmado:** algunas fuentes de 2026 dicen que Meta eliminó el estado "Flagged".
Verifícalo en el WhatsApp Manager de la cuenta real.

## 1.9 Si te banean

| Tipo | Duración típica |
|---|---|
| Restricción por calidad baja | 24–72 horas si corriges |
| Restricción por límite diario | Se libera sola en 24 h |
| Suspensión por violación de políticas | Una semana a permanente |

**Cómo apelar:** por Meta Business Support Home o el WhatsApp Manager. Junta evidencia **antes**.
**Una sola apelación, factual, sin drama.** Las repetidas empeoran el caso.

🚨 **Si la apelación se rechaza, el número queda quemado para siempre.**

**Por eso:** nunca el número personal del dueño ni el principal del negocio para experimentar. Y
el **dueño debe ser propietario del portafolio de negocio en Meta**, no el desarrollador.

## 1.10 Verificación del negocio

Solo hace falta si el negocio va a iniciar conversaciones. Un bot que solo responde **no la
necesita**.

Requiere identificación tributaria de empresa (no personal), documentos de constitución,
comprobante de domicilio comercial, y **un sitio web con dominio propio**. Demora 2 a 7 días
hábiles.

⚠️ **La causa #1 de rechazo son las inconsistencias** entre nombre, dirección e identificación
tributaria en los distintos documentos.

---

# 2. LO QUE EXIGE ANTHROPIC

## 2.1 🚨 Hay que declarar que es una IA

Usage Policy vigente desde el 15-sep-2025:

> *"All consumer-facing chatbots, including any external-facing or interactive AI agent, must
> disclose to users that they are interacting with AI rather than a human."*

Y prohíbe expresamente hacerse pasar por humano. **No es opcional: es condición de uso del
servicio.** Si el bot se presenta como "la Cami de recepción", se están violando los términos.

## 2.2 🚨 El bot no puede dar consejo de salud

> *"When using our products or services to provide advice, recommendations, or in subjective
> decision-making directly affecting individuals or consumers, a qualified professional in that
> field must review the content or decision prior to dissemination or finalization."*

**Traducción para una estética, dental o consulta:** el bot **no recomienda tratamientos, no
diagnostica, no desaconseja procedimientos.** Informa servicios, precios y horarios, y agenda.
Todo lo demás deriva a un profesional.

## 2.3 Qué pasa con los datos que se le mandan

**Anthropic NO entrena con datos de la API.** Commercial Terms: *"Anthropic may not train models
on Customer Content from Services."*

⚠️ **La confusión típica:** en agosto de 2025 cambiaron los términos **de consumidor** (claude.ai
Free/Pro/Max) a entrenamiento por defecto con opt-out. **Eso NO aplica a la API.**

**Única excepción:** el feedback explícito (pulgar arriba/abajo) sí puede usarse para entrenar y
se guarda hasta 5 años. → **No implementes botones de calificación en el bot.**

**Retención:** 30 días por defecto para la API. Contenido marcado por trust & safety, hasta 2
años.

**Zero Data Retention** existe pero se negocia con ventas; una cuenta de pago por uso
realistamente no califica.

⚠️ **Si el bot maneja datos de salud:** los modelos más nuevos designados "Covered Models" exigen
retención de 30 días y **no admiten ZDR** bajo ningún contrato. Haiku, Sonnet y Opus sí son
elegibles.

**Dónde se procesa:** Estados Unidos por defecto. La API directa no tiene región europea.

**Rol contractual:** el acuerdo de tratamiento dice *"Customer is the controller and Anthropic is
Customer's processor."*

---

# 3. DATOS PERSONALES — principios universales

Las leyes cambian por país, pero estos principios se repiten en casi todas y **cumplirlos deja al
negocio en buen pie en cualquier parte**. Lo específico va en el anexo local.

## 3.1 Lo que aplica en todos lados

1. **Tener una razón legítima para tratar los datos.** Que un cliente escriba pidiendo hora
   normalmente basta para atenderlo; guardar su historial para otra cosa, no.
2. **Informar.** Un aviso de privacidad accesible, que diga quién trata los datos, para qué,
   cuánto los guarda y cómo ejercer derechos.
3. **Usarlos solo para lo que se recolectaron.**
4. **Guardar solo lo necesario.** Nada "por si acaso".
5. **Poder borrarlos si el titular lo pide**, y en un plazo razonable.
6. **Medidas de seguridad** proporcionales al riesgo.
7. **Contrato escrito con cada proveedor** que trate datos por encargo.
8. **Avisar si hay una filtración.**

## 3.2 🚨 El riesgo grande: los datos delicados

**Si el negocio toca salud o el cuerpo, el riesgo no son los teléfonos: es lo que la gente cuenta
de su salud.**

Casi todas las leyes del mundo tratan aparte la información de salud, y suelen exigir
**consentimiento expreso** —no basta con "es necesario para atenderlo"— y castigan su mal uso con
las sanciones más altas de su escala.

Cuenta como tal: estética, dental, consulta médica, kinesiología, nutrición, psicología,
peluquería, barbería, podología, masajes, tatuajes y micropigmentación.

**Ojo con los que no son obvios.** Una peluquería parece inofensiva hasta que te acuerdas de que
pregunta por alergias a las tinturas y por el estado del cuero cabelludo, y que las clientas
mandan **fotos de su pelo**.

**Qué hacer:** pedir permiso explícito antes de la primera pregunta sobre salud, guardar ese
permiso con fecha y texto exacto, y **no guardar fotos corporales** sin un consentimiento aparte.

## 3.3 Quién responde legalmente

| Rol | Quién |
|---|---|
| **Responsable** (decide para qué se usan los datos) | **El negocio** |
| **Encargado** (los trata por instrucción) | **El desarrollador**, si opera la infraestructura |
| **Encargado** | Meta, Anthropic, el alojamiento, la base de datos |

**El negocio responde ante la autoridad y ante los clientes.** No puede escudarse en "me lo hizo
un freelance".

**Pero esto es lo que protege al desarrollador, o lo hunde:** sin contrato escrito, el negocio
queda expuesto… y después demanda civilmente al desarrollador. **El contrato protege a los dos.**

**La distinción que cambia toda la exposición:**

| Si el desarrollador… | Su rol | Exposición |
|---|---|---|
| **Solo construye y entrega**, el negocio opera con sus propias cuentas | Proveedor de desarrollo — no trata datos | Baja |
| **Hospeda, opera o accede** a las conversaciones | **Encargado del tratamiento** | Alta, contrato obligatorio |

**Defínelo el día uno, por escrito.** Es la decisión con más impacto legal del proyecto.

**Contenido mínimo del contrato:** que el encargado trata datos solo bajo instrucciones; medidas
de seguridad concretas; confidencialidad; deber de asistir en solicitudes de los titulares;
notificación de filtraciones y plazo; autorización de subencargados; devolución o eliminación al
terminar; derecho de auditoría.

🔴 **No entregues un bot sin este contrato firmado. Lo debe redactar o revisar un abogado.**

## 3.4 Datos fuera del país

Los proveedores (alojamiento, modelo, base de datos) suelen estar en Estados Unidos. Casi todas
las leyes modernas exigen una garantía contractual para eso.

**En la práctica es más fácil de lo que suena** — los proveedores ya traen su acuerdo de
tratamiento con cláusulas contractuales tipo:

| Proveedor | Acuerdo |
|---|---|
| **Anthropic** | Se acepta automáticamente con los Commercial Terms. No hay que firmar nada aparte |
| **Vercel** | Cláusulas contractuales tipo, módulos 1/2/3 |
| **Supabase** | Sí, y ofrece varias regiones |
| **Meta / WhatsApp** | Meta actúa como encargado para Cloud API |

💡 **Decisión de arquitectura gratis: elegir la región de la base de datos más cercana al
negocio**, y de un país con ley integral de protección de datos. Para América Latina, São Paulo.
⚠️ **Se decide al crear el proyecto y no se puede cambiar después.**

## 3.5 Publicidad y bajas

**Principio universal:** si el negocio manda promociones, cada mensaje debe incluir una forma
clara de dejar de recibirlas, y la baja se respeta **para siempre**.

Casi todos los países lo exigen por ley del consumidor, con multas que suelen calcularse **por
persona afectada** — así que un envío masivo mal hecho escala rápido.

**Qué hacer siempre:** línea de baja en toda plantilla de marketing, registro de bajas con fecha,
y respetarlas de forma permanente. Cuesta cero y evita el problema completo.

---

# 4. TEXTOS BASE

⚠️ **Son borradores de trabajo, no documentos legales validados.** Adáptalos al país del negocio y
hazlos revisar por un abogado antes de publicarlos.

### A) Primer mensaje del bot — obligatorio por Anthropic

```
¡Hola! 👋 Soy el asistente virtual de [NEGOCIO]. Te atiendo con
inteligencia artificial, disponible 24/7.

Puedo ayudarte con horarios, servicios, precios y agendar tu hora.
Si prefieres hablar con una persona del equipo, escribe HUMANO y
te paso con ellos.

Al continuar, tus mensajes se procesan según nuestra política de
privacidad: [URL]
```

### B) Consentimiento para datos de salud

```
Para orientarte mejor necesito hacerte algunas preguntas sobre tu
piel y tu salud. Esa información es delicada y solo la usamos para
atenderte en [NEGOCIO].

¿Autorizas que la registremos? Responde SÍ para continuar, o
escribe HUMANO si prefieres conversarlo con nuestro equipo.
```

**Guardar siempre:** fecha y hora, el texto exacto mostrado, la respuesta literal y el teléfono.

### C) Aviso de privacidad

```
POLÍTICA DE PRIVACIDAD — [NOMBRE], [ID TRIBUTARIO]

Quién trata tus datos: [Razón social], [ID], [dirección].
Contacto: [email].

Qué datos guardamos: tu número de WhatsApp, tu nombre y el
contenido de nuestras conversaciones. Si nos consultas por
tratamientos, también información de salud.

Para qué: responder tus consultas, agendar horas y llevar tu
historial de atención.

Base legal: la ejecución de nuestra relación comercial y, para
datos de salud, tu consentimiento expreso.

Con quién los compartimos: WhatsApp/Meta (mensajería), Anthropic
(procesamiento con IA), y nuestros proveedores de infraestructura.
Algunos operan fuera del país, con cláusulas contractuales que
garantizan tu protección.

Cuánto los guardamos: [N] meses desde tu última interacción.
Después se eliminan.

Tus derechos: puedes pedir acceso, rectificación, eliminación,
oposición y portabilidad de tus datos escribiendo a [email].
Respondemos en máximo [N] días.

Usamos inteligencia artificial para responderte. Puedes pedir
atención humana en cualquier momento.
```

### D) Pie de plantillas de marketing

```
Responde BAJA para no recibir más promociones.
```

## Dónde va cada texto

| Texto | Dónde |
|---|---|
| Primer mensaje | Primera respuesta de cada conversación nueva, y tras 30+ días de inactividad |
| Consentimiento de salud | Antes de la primera pregunta sobre tratamientos |
| Política completa | Sitio web, URL fija. Enlazada desde el perfil y el primer mensaje |
| Línea de BAJA | Todas las plantillas de **marketing**. No en utility ni service |

---

# 5. QUÉ GUARDAR Y QUÉ NO

## Guardar sí o sí — es la defensa

- ✅ **Registro de opt-in:** teléfono, fecha, canal, texto mostrado, respuesta literal
- ✅ **Registro de consentimiento para datos de salud**, por separado
- ✅ **Registro de bajas** con fecha
- ✅ **Registro de actividades de tratamiento** — una planilla: qué datos, para qué, con quién se
  comparten, cuánto se guardan
- ✅ **Log de solicitudes de los titulares** y cuándo se respondieron
- ✅ Contrato de encargo firmado

## No guardar — reduce el riesgo más que cualquier cláusula

- ❌ **Identificación tributaria**, salvo que sea imprescindible para facturar
- ❌ **Datos de tarjeta o medios de pago.** Nunca. Que lo maneje la pasarela
- ❌ **Fotos de tratamientos o imágenes corporales** sin consentimiento expreso y separado
- ❌ Datos de terceros que el cliente mencione
- ❌ Conversaciones de gente que nunca se convirtió en cliente, más allá de unas semanas

💡 **La mitigación más barata y efectiva: enmascarar los datos personales antes de armar el
prompt.** Identificaciones, teléfonos, direcciones y correos se sustituyen por marcadores antes de
salir hacia el modelo.

## Cuánto retener

Ninguna ley fija plazos exactos — dicen "solo el tiempo necesario". Esto es buena práctica:

| Dato | Plazo sugerido |
|---|---|
| Conversaciones de clientes activos | 24 meses desde la última interacción |
| Conversaciones de no-clientes | 6 meses |
| Datos de salud | 12 meses, salvo ficha clínica formal (régimen propio) |
| Registro de opt-in y consentimientos | Mientras dure la relación **+ 5 años** — es la prueba |
| Registro de bajas | **Indefinido** — si lo borras, vuelves a contactar a quien pidió baja |
| Logs técnicos con teléfonos | 90 días |

**Implementación:** un proceso automático de borrado. Sin automatización no se cumple. Y **el
código tiene que hacer lo que la política dice.**

---

# 6. CHECKLIST DE CUMPLIMIENTO

**Antes de construir:**
- [ ] Definido por escrito si el desarrollador **opera** o **solo entrega**
- [ ] **Contrato de encargo** redactado o revisado por abogado
- [ ] Cuentas a nombre del **negocio**
- [ ] Número de WhatsApp **dedicado**, nunca el personal del dueño

**En la construcción:**
- [ ] Base de datos en una región cercana y con ley de datos — irreversible
- [ ] Seguridad a nivel de fila en todas las tablas
- [ ] Credenciales solo en el servidor
- [ ] **Indicador de bloqueo** que corte el procesamiento a pedido del titular
- [ ] Registro de baja de marketing con fecha
- [ ] Borrado automático según la tabla de retención
- [ ] **Enmascarado de datos personales** antes de mandar el prompt

**En el guion:**
- [ ] System prompt **acotado al dominio** — exigencia de Meta
- [ ] **Declaración de IA** en el primer mensaje — exigencia de Anthropic
- [ ] Palabra HUMANO que derive a una persona — exigencia de Meta
- [ ] **Nada de consejo de salud** — exigencia de Anthropic
- [ ] **Sin botones de calificación** — evita la retención de 5 años

**Operación:**
- [ ] 🚨 Método de pago registrado en la cuenta de WhatsApp Business
- [ ] Plantillas con categoría honesta
- [ ] Línea de baja en toda plantilla de marketing
- [ ] Monitoreo de la calificación de calidad

---

# 7. DÓNDE SE NECESITA ABOGADO

| Tema | Por qué |
|---|---|
| 🔴 **Contrato de encargo** | Define quién responde. Es el blindaje del desarrollador |
| 🔴 **Política de privacidad definitiva** | Los borradores de arriba son punto de partida |
| 🔴 **Si los datos del negocio califican como de salud** | Determina la gravedad de un error |
| 🟡 Si aplica evaluación de impacto o delegado de protección de datos | Los umbrales rara vez están definidos numéricamente |
| 🟡 Las obligaciones de publicidad de su país | Suelen ser más viejas que WhatsApp y hay que interpretarlas |

---

# 8. EL ANEXO DEL PAÍS

**Pregunta en qué país está el negocio** y carga el anexo si existe:

| País | Anexo |
|---|---|
| Chile | `legal-chile.md` |
| Otros | *(no hay anexo todavía)* |

**Si no hay anexo para su país**, dilo con honestidad y sigue con los principios de arriba:

> *"Las reglas de WhatsApp y de la inteligencia artificial son iguales en todas partes y ya las
> tenemos cubiertas. Lo que cambia de un país a otro es la ley de datos personales y las tarifas
> por mensaje. Voy a dejar todo armado según buenas prácticas que sirven en casi cualquier parte,
> y te voy a marcar los dos o tres puntos que conviene que revise un abogado de tu país antes de
> salir con clientes reales."*

**Lo que hay que averiguar para armar un anexo nuevo:**
1. La ley de datos personales vigente y si hay autoridad fiscalizadora operativa
2. Cómo se tratan los datos de salud y qué base legal exigen
3. Plazos para responder solicitudes de los titulares
4. Qué exige la ley del consumidor para publicidad y bajas
5. Las tarifas de WhatsApp para ese país en el rate card oficial de Meta
6. Qué se necesita para verificar un negocio ante Meta ahí

**Nunca inventes el marco legal de un país que no investigaste.** Es preferible decir "esto lo
tiene que ver un abogado local" que dar una cifra o un plazo equivocado.
