# Transversal — Políticas de Meta, Anthropic y ley chilena

**No es una fase.** Se consulta en tres momentos:
- **`/bot-planificar`** — las advertencias del brief
- **`/bot-planificar`** — los avisos que van dentro del guion
- **`/bot-publicar`** — los textos obligatorios antes de encender

⚠️ **Esto es investigación, no asesoría legal.** Al final está la lista de dónde se necesita
abogado de verdad. Datos al 31 de agosto de 2026.

---

# LO QUE NO PUEDE FALLAR — resumen para ti

Seis cosas. Si te llevas solo esto:

1. **La Ley 21.719 todavía NO rige.** Entra el 1-dic-2026 y el Gobierno evalúa postergarla. Hoy
   rige la vieja Ley 19.628, mucho más laxa. **No vendas urgencia falsa.**
2. **Lo que sí puede multar HOY es el SERNAC**, no la ley de datos. Hasta 300 UTM (~$21,5
   millones) **por consumidor**.
3. **Meta prohíbe los bots de IA de propósito general desde enero de 2026.** El system prompt
   tiene que estar acotado al negocio. **Es cumplimiento de términos, no una decisión de diseño.**
4. **Anthropic obliga a declarar que es IA.** Meta no lo exige; Anthropic sí, por contrato.
5. **Anthropic prohíbe que el bot dé consejo de salud** sin revisión de un profesional.
6. **Si el negocio es de salud o estética, el riesgo grande son los datos de salud, no los
   teléfonos.** Infracción gravísima, hasta 20.000 UTM.

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

**Si la violas:** no hay multa — la API rechaza el mensaje con error (`131026`). No se puede
"romper" técnicamente. El riesgo real es abusar de plantillas para evadirla; eso sí gatilla
bloqueo.

### 🚨 El cambio del 1 de octubre de 2026 y su fecha límite

Meta lo anunció el 10 de agosto de 2026:

> *"Effective October 1, 2026, Meta will charge for service messages, which have not been charged
> since November 2024."*

**Cada respuesta libre del bot dentro de la ventana pasa a cobrarse.** Para Chile, ≈$0,0200 por
mensaje. Los mensajes entrantes del cliente siguen gratis, y la ventana de 72 horas por anuncios
Click-to-WhatsApp se mantiene gratuita.

**Y hay una fecha límite dura:**

> *"For any Solution Provider or directly-integrated business that does not have a payment method
> on file by September 30, 2026, Meta will stop delivering service messages as of when they become
> charged on October 1, 2026."*

🚨 **Sin método de pago registrado en la cuenta de WhatsApp Business al 30 de septiembre de 2026,
el bot deja de entregar respuestas el 1 de octubre.** No falla con error visible: el cliente
escribe y la respuesta nunca llega.

**Acción:** es ítem obligatorio del checklist de `/bot-conectar` y de la lista previa al encendido de la
`/bot-publicar`. **Y si el usuario tiene otros bots andando de antes de este proyecto, avísale — aunque
estén fuera de este trabajo.**

**Zernio no expone un campo con el vencimiento de la ventana.** Hay que calcularla desde la fecha
del último mensaje entrante.

## 1.2 Plantillas

Obligatorias siempre que el negocio inicie la conversación, o pasadas las 24 horas.

| Categoría | Para qué | Costo Chile (USD/mensaje) |
|---|---|---|
| **Marketing** | Promos, ofertas, reactivación | **$0,0889** |
| **Utility** | Confirmación de hora, recordatorio | **$0,0200** |
| **Authentication** | Códigos | **$0,0200** |

**Aprobación:** las primeras de una cuenta nueva demoran **24–48 horas**; después bajan a minutos.
**No hay apelación formal** si te rechazan: corriges y reenvías.

**Por qué rechazan:** meter texto promocional en una plantilla marcada como *utility* (Meta revisa
la categoría antes que el contenido), variables mal formadas, faltas de ortografía, mayúsculas
excesivas.

⚠️ **Categoriza honestamente.** Marcar marketing como utility para pagar menos es la vía rápida a
que te bajen la calidad de la cuenta.

## 1.3 Opt-in

Meta pide dos cosas y es flexible: que la persona haya dado su número, y que haya un permiso
confirmando que quiere recibir mensajes **de ese negocio**.

El aviso debe decir que se suscribe a comunicaciones del negocio, **nombrar el negocio**, y
cumplir la ley local. **No tiene que ser dentro de WhatsApp** — vale web, formulario en papel,
SMS, código QR, en persona.

⚠️ **Meta permite opt-in general. La ley chilena es más exigente. Cumplir Meta ≠ cumplir Chile.**

## 1.4 🚨 Meta prohíbe los bots de IA de propósito general

**Vigente para todas las cuentas desde el 15 de enero de 2026.** Meta cambió los WhatsApp Business
Solution Terms.

**Prohibido:** asistentes de dominio abierto tipo ChatGPT usando WhatsApp como canal. Definición
de Meta: corre sobre un modelo de lenguaje, admite conversación de dominio abierto, **no está
restringido a un proceso de negocio específico**.

**Permitido y fomentado:** bots que un negocio corre para sus propios clientes — soporte,
agendamiento, seguimiento de pedidos, calificación de interesados, ventas.

| | |
|---|---|
| ✅ Bot que agenda horas, responde precios, explica servicios y deriva | **Cumple** |
| ❌ Bot al que le puedes preguntar "¿cuál es la capital de Francia?" | **Expone a restricción o suspensión** |

**Acción obligatoria en `/bot-probar`:** el system prompt **acota el dominio** y rechaza lo que se
salga del negocio. Esto no es UX — es cumplimiento de términos.

Contexto: Meta lanzó su propio agente de IA (junio 2026) y la Business Agent Platform (julio
2026). Compite en este espacio. Razón de más para que el bot sea claramente "de negocio".

## 1.5 Qué hace que te bajen el número

Por frecuencia real:

1. **Mensajes masivos sin consentimiento** (listas compradas). Causa #1.
2. **Tasa alta de bloqueos y reportes.** El quality rating cae en horas.
3. **Versiones no oficiales de WhatsApp.** Baneo sin excepciones.
4. **Display name inconsistente** con la marca real, o genérico.
5. **Registrar en la API un número que aún tiene cuenta activa en la app.** Hay que borrarla
   primero (o usar Coexistence).
6. **Suplantar a otro negocio**, contenido prohibido.
7. **Base de datos sucia** → rebotes → reputación degradada.

**El bloqueo va asociado al número**, no a la cuenta ni al dispositivo.

## 1.6 Calidad y límites

**Quality rating:** evaluación de los últimos 7 días, con señales de usuario (bloqueos, reportes,
y el motivo escrito al bloquear). Verde / Amarillo / Rojo.

**Estados:** *Connected* (normal) · *Flagged* (calidad baja, 7 días para recuperar) · *Restricted*
(tope diario alcanzado; puedes seguir respondiendo entrantes).

**Tiers** — destinatarios únicos que puedes **iniciar** por 24h: 250 (sin verificar) → 2.000 →
10.000 → 100.000 → ilimitado.

⚠️ **Los tiers no aplican a un bot reactivo.** Solo limitan conversaciones que inicia el negocio.
Para pasar de 250 a 2.000 se necesita **verificación de negocio en Meta**, verificación vía
partner, o 2.000 mensajes de calidad en 30 días.

⚠️ Desde octubre de 2025 los límites son **por Meta Business Portfolio**, no por número. Varios
números bajo el mismo portfolio comparten cupo.

⚠️ **No confirmado:** algunas fuentes de 2026 dicen que Meta eliminó el estado "Flagged".
Verifícalo en el WhatsApp Manager de la cuenta real.

## 1.7 Si te banean

| Tipo | Duración típica |
|---|---|
| Restricción por calidad baja | 24–72 horas si corriges |
| Restricción por límite diario | Se libera sola en 24h |
| Suspensión por violación de políticas | Una semana a permanente |

**Cómo apelar:** por Meta Business Support Home o el WhatsApp Manager. Junta evidencia **antes**:
registros de opt-in, documentos del negocio, prueba de que los contactos son clientes reales.
**Una sola apelación, factual, sin drama.** Apelaciones repetidas empeoran el caso.

🚨 **Si la apelación se rechaza, el número queda quemado para siempre.** Registrar de nuevo con el
mismo número no funciona.

**Por eso:** nunca uses el número personal del dueño ni el principal del negocio para
experimentar. Y el **dueño debe ser propietario del Meta Business Portfolio**, no el
desarrollador.

## 1.8 Verificación del negocio en Chile

- Requiere **RUT de empresa** (no personal): e-RUT, escritura de constitución, comprobante de
  domicilio comercial
- Meta exige **presencia web con dominio propio**, con nombre, servicios y contacto
- **Demora 2 a 7 días hábiles**
- **Causa #1 de rechazo:** inconsistencias entre nombre, dirección y RUT en los documentos. Que
  todo calce exacto.

---

# 2. LO QUE EXIGE ANTHROPIC

## 2.1 🚨 Hay que declarar que es una IA

Meta no lo exige. **Anthropic sí, por contrato.** Usage Policy vigente desde el 15-sep-2025:

> *"All consumer-facing chatbots, including any external-facing or interactive AI agent, must
> disclose to users that they are interacting with AI rather than a human."*

Y prohíbe expresamente hacerse pasar por humano.

**No es opcional: es condición de uso del servicio.** Si el bot se presenta como "la Cami de
recepción", se están violando los términos.

## 2.2 🚨 El bot no puede dar consejo de salud

Misma Usage Policy:

> *"When using our products or services to provide advice, recommendations, or in subjective
> decision-making directly affecting individuals or consumers, a qualified professional in that
> field must review the content or decision prior to dissemination or finalization."*

Aplica a salud, entre otros.

**Traducción para una estética, una dental o una consulta:** el bot **no puede recomendar
tratamientos, diagnosticar condiciones ni desaconsejar procedimientos.** Puede informar servicios,
precios y horarios, y agendar. Todo lo que huela a consejo de salud **deriva a un profesional**.

Esto va en el system prompt **y** en el diseño del flujo de `/bot-planificar`.

## 2.3 Qué pasa con los datos que se le mandan

**Anthropic NO entrena con datos de la API.** Commercial Terms: *"Anthropic may not train models
on Customer Content from Services."*

⚠️ **La confusión típica:** en agosto de 2025 Anthropic cambió los términos **de consumidor**
(claude.ai Free/Pro/Max) a entrenamiento por defecto con opt-out. **Eso NO aplica a la API.**
Textual: *"These updates do not apply to services under our Commercial Terms, including… Our
API"*.

**Única excepción:** el feedback explícito (pulgar arriba/abajo) sí puede usarse para entrenar y
se guarda **hasta 5 años**.

→ **Acción: no implementes botones de feedback en el bot**, o desactívalo en la configuración de
la organización.

**Retención:**

| Caso | Retención |
|---|---|
| Inputs/outputs de API (por defecto) | **30 días** |
| Contenido marcado por trust & safety | hasta 2 años |
| Feedback explícito | 5 años |

**Zero Data Retention existe pero se negocia con ventas.** Una cuenta pay-as-you-go realistamente
no califica. Planifica asumiendo 30 días.

⚠️ **Si el bot maneja datos de salud:** los modelos más nuevos designados "Covered Models" exigen
retención obligatoria de 30 días y **no admiten ZDR** bajo ningún contrato. Haiku, Sonnet y Opus
sí son elegibles. Un argumento más para quedarse en Haiku 4.5.

**Dónde se procesa:** EEUU por defecto. La API directa no tiene región europea.

**Rol contractual:** el DPA dice *"Customer is the controller and Anthropic is Customer's
processor."*

---

# 3. LEY CHILENA

## 3.1 🚨 La Ley 21.719 todavía no rige

- Publicada el 13-dic-2024. **Entrada en vigencia: 1 de diciembre de 2026.**
- **La Agencia de Protección de Datos no está operativa.** El Consejo Directivo debía constituirse
  a fines de mayo de 2026; el Senado rechazó la terna propuesta y a agosto de 2026 sigue sin
  nombrarse.
- **El Gobierno está evaluando postergar la entrada en vigencia.** Sin anuncio oficial.

**Qué rige hoy: la Ley 19.628**, de 1999. Mucho más laxa. Multas de 2 a 50 UTM (~$143.000 a
~$3.582.000). **Sin autoridad fiscalizadora** — hay que ir a tribunales civiles.

**Cómo leer esto sin equivocarse:** el riesgo regulatorio **hoy** es bajo. El riesgo desde
diciembre es alto. Diseñar bien hoy cuesta casi lo mismo que diseñar mal; adaptarlo después cuesta
mucho más. **Pero no le vendas urgencia falsa al usuario: la fecha se puede mover.**

## 3.2 🔴 Lo que SÍ puede multar hoy: SERNAC

**Artículo 28 B de la Ley 19.496**, vigente:

> *"Los proveedores que dirijan comunicaciones promocionales o publicitarias a los consumidores
> por medio de… servicios de mensajería telefónica, deberán indicar una forma expedita en que los
> destinatarios podrán solicitar la suspensión de las mismas…"*

Una vez pedida la suspensión, **mandar nuevas comunicaciones queda prohibido**.

**Multas de hasta 300 UTM ≈ $21,5 millones — por cada consumidor afectado.**

Existe además el **Sistema "No Molestar"** del SERNAC, donde los consumidores se inscriben.

**Acción obligatoria:** toda plantilla de **marketing** cierra con línea de baja, y el bot procesa
la baja automáticamente. **Es obligación legal vigente hoy**, no buena práctica.

⚠️ *"Servicios de mensajería telefónica"* se redactó antes de que existiera WhatsApp. Un abogado
podría discutir si aplica. **Lo prudente es asumir que sí** — cumplir cuesta cero.

## 3.3 🚨 El riesgo grande: los datos sensibles

**Si el negocio es una estética, dental, consulta o similar, el riesgo no son los teléfonos: son
los datos de salud.**

En Chile son **datos sensibles**: salud, perfil biológico y biométrico, origen racial, afiliación
sindical o política, convicciones religiosas, vida y orientación sexual, y —particularidad
chilena— **situación socioeconómica**.

Una estética conversa de tratamientos, condiciones de piel, procedimientos. **Eso es dato de
salud.** Consecuencias:

- Requiere **consentimiento expreso**. El interés legítimo **no sirve** como base para datos
  sensibles.
- **Tratarlos sin autorización es infracción gravísima** → hasta 20.000 UTM (~$1.433 millones).
- Puede gatillar Evaluación de Impacto si es "a gran escala" (zona gris para un negocio chico).

**Bases de licitud aplicables al bot:**

| Situación | Base |
|---|---|
| Cliente escribe pidiendo hora | Medidas precontractuales — **no necesita consentimiento aparte** |
| Guardar historial para dar mejor servicio | Interés legítimo (con test de balanceo documentado) |
| Mandarle promociones después | **Consentimiento** + art. 28 B del SERNAC |
| Conversar sobre tratamientos, piel, alergias | 🔴 **Consentimiento expreso obligatorio** |

## 3.4 Quién responde legalmente

| Rol | Quién |
|---|---|
| **Responsable** (decide finalidades y medios) | **El negocio** |
| **Encargado** (trata datos por instrucción) | **El desarrollador**, si opera la infraestructura |
| **Encargado** | Meta, Anthropic, Vercel, Supabase |

**El negocio responde ante la Agencia y ante los titulares.** No puede escudarse en "me lo hizo un
freelance".

**Pero ojo — esto es lo que protege al desarrollador, o lo hunde:** sin contrato de encargo
escrito, el negocio queda expuesto, y después demanda civilmente al desarrollador. **El contrato
protege a los dos.**

**Qué debe contener el contrato de encargo (mínimo):**
1. Que el encargado trata datos **solo bajo instrucciones** del responsable
2. Medidas de seguridad concretas
3. Deber de confidencialidad
4. Obligación de asistir en solicitudes de derechos
5. Obligación de notificar brechas, y en qué plazo
6. Régimen de subencargados (Anthropic, Vercel, base de datos) y autorización
7. Qué pasa al terminar: devolución o eliminación de datos
8. Derecho de auditoría

🔴 **Acción crítica: no entregues un bot sin este contrato firmado.** Lo debe redactar o revisar
un abogado.

**Matiz que cambia todo:** si el desarrollador **solo construye y entrega** (el negocio opera todo
con sus propias cuentas), es **proveedor de desarrollo**, no encargado — no trata datos. Si
**hostea, opera o accede** a las conversaciones, **sí es encargado**. Definirlo desde el día uno
cambia completamente la exposición. Conecta con la regla de `entrega-cliente.md`: **las cuentas a
nombre del cliente**.

## 3.5 Derechos del titular y plazos

Seis derechos: acceso, rectificación, supresión, oposición, portabilidad y bloqueo.

| Obligación | Plazo |
|---|---|
| Responder una solicitud | **30 días corridos**, prorrogable una vez por 30 más |
| **Bloqueo temporal** al recibir solicitud de rectificación/supresión/oposición | **2 días hábiles** |

⚠️ **El bloqueo en 2 días hábiles es el que pilla desprevenido.** Si el sistema no tiene un
indicador de "bloqueado" que corte el procesamiento, no se puede cumplir. **Es diseño técnico —
hay que preverlo en `/bot-probar`.**

⚠️ Circulan fuentes que dicen "15 días hábiles". La lectura mejor sustentada es 30 días corridos.
**Confírmalo con abogado antes de escribirlo en un contrato.**

## 3.6 Multas

UTM a agosto de 2026: **$71.649**.

| Gravedad | Tope | En pesos |
|---|---|---|
| Leve | 5.000 UTM | ~$358 millones |
| Grave | 10.000 UTM | ~$716 millones |
| **Gravísima** | **20.000 UTM** | **~$1.433 millones** |

Reincidencia: la multa puede **triplicarse**. Hay **Registro Nacional de Sanciones público**, con
las sanciones visibles 5 años — para un negocio local, el daño reputacional puede pesar más que
la multa.

⚠️ **Atenuante PYME:** la Ley 20.416 establece que las empresas de menor tamaño reciben
**amonestación escrita, no multa, en su primera infracción**. **No confirmado en fuente primaria
para este régimen — punto de abogado.**

## 3.7 Registro ante autoridades

**No hay que inscribirse.** No existe obligación general de registrar la empresa ni sus bases de
datos ante la Agencia.

Lo que sí: un **registro interno de actividades de tratamiento** (una planilla documentando qué
datos, para qué, con quién se comparten, cuánto se guardan). Se documenta, no se presenta.

**DPO:** obligatorio solo para organismos públicos y empresas cuya actividad principal sea
tratamiento a gran escala de datos sensibles. Un negocio local no califica.

## 3.8 Datos fuera de Chile

Los proveedores están en EEUU. La vía practicable son las **cláusulas contractuales tipo**.

✅ **El Ministerio de Economía ya aprobó las Cláusulas Contractuales Modelo** (resolución del
11-dic-2025, publicada el 19-dic-2025). Vigentes de forma transitoria hasta que la Agencia ejerza
su facultad.

⚠️ Existe crítica jurídica pública que cuestiona su legalidad por haberse dictado antes de que
exista la Agencia. **Punto de abogado.**

**En la práctica es más fácil de lo que suena** — los proveedores ya traen su acuerdo de
tratamiento de datos:

| Proveedor | Acuerdo |
|---|---|
| **Anthropic** | Se acepta automáticamente con los Commercial Terms. **No hay que firmar nada aparte.** |
| **Vercel** | Cláusulas contractuales tipo, módulos 1/2/3 |
| **Supabase** | Sí, **y ofrece región São Paulo** |
| **Meta / WhatsApp** | Meta actúa como encargado para Cloud API |

💡 **Decisión de arquitectura gratis: desplegar la base de datos en São Paulo (`sa-east-1`), no en
EEUU.** No elimina la transferencia internacional, pero Brasil tiene ley integral de protección de
datos —mucho mejor candidato a "nivel adecuado" que EEUU— y baja la latencia para Chile.

⚠️ **Se decide al crear el proyecto y no se puede cambiar después.** Va en `/bot-probar`.

## 3.9 Si hay una filtración

La ley exige notificar **"sin dilaciones indebidas"**. **No fija el plazo de 72 horas** del
reglamento europeo — muchas guías lo repiten mal.

- **A la Agencia:** por los medios más expeditos, cuando exista riesgo razonable para los
  titulares.
- **A los titulares:** obligatorio cuando involucra **datos sensibles**, datos de menores, o datos
  económicos. **Un negocio de salud o estética cae acá.**
- Postergar el reporte mientras "se recopila información completa" es en sí mismo sancionable.

---

# 4. TEXTOS LISTOS PARA COPIAR

⚠️ **Son borradores de trabajo, no documentos legales validados.** Deben ser revisados por un
abogado antes de publicarse.

### A) Primer mensaje del bot — obligatorio por Anthropic

```
¡Hola! 👋 Soy el asistente virtual de [NEGOCIO]. Te atiendo con
inteligencia artificial, disponible 24/7.

Puedo ayudarte con horarios, servicios, precios y agendar tu hora.
Si prefieres hablar con una persona del equipo, escribe HUMANO y
te derivo.

Al continuar, tus mensajes se procesan según nuestra política de
privacidad: [URL]
```

### B) Consentimiento para datos de salud — antes de cualquier consulta sobre tratamientos

```
Para orientarte mejor necesito hacerte algunas preguntas sobre tu
piel y tu salud. Esa información es un dato sensible y solo la
usamos para atenderte en [NEGOCIO].

¿Autorizas que la registremos? Responde SÍ para continuar, o
escribe HUMANO si prefieres conversarlo con nuestro equipo.
```

**Guardar siempre:** fecha y hora, el texto exacto que se mostró, la respuesta literal, y el
número de teléfono.

### C) Aviso de privacidad — perfil de WhatsApp Business y pie del sitio

```
POLÍTICA DE PRIVACIDAD — [NOMBRE], RUT [XX.XXX.XXX-X]

Quién trata tus datos: [Razón social], RUT [XXX], [dirección].
Contacto: [email].

Qué datos guardamos: tu número de WhatsApp, tu nombre y el
contenido de nuestras conversaciones. Si nos consultas por
tratamientos, también información de salud (dato sensible).

Para qué: responder tus consultas, agendar horas y llevar tu
historial de atención.

Base legal: la ejecución de nuestra relación comercial y, para
datos de salud, tu consentimiento expreso.

Con quién los compartimos: WhatsApp/Meta (mensajería), Anthropic
(procesamiento con IA), y nuestros proveedores de infraestructura.
Algunos operan fuera de Chile, con cláusulas contractuales que
garantizan tu protección.

Cuánto los guardamos: 24 meses desde tu última interacción.
Después se eliminan.

Tus derechos: puedes pedir acceso, rectificación, supresión,
oposición, portabilidad y bloqueo de tus datos escribiendo a
[email]. Respondemos en máximo 30 días.

Usamos inteligencia artificial para responderte. Puedes pedir
atención humana en cualquier momento.
```

### D) Pie de plantillas de marketing — obligatorio HOY por el art. 28 B

```
Responde BAJA para no recibir más promociones.
```

### E) Confirmación de baja

```
Listo. No recibirás más promociones de [NEGOCIO]. Igual puedes
escribirnos cuando necesites agendar. 👍
```

## Dónde va cada texto

| Texto | Dónde |
|---|---|
| Primer mensaje | Primera respuesta de cada conversación nueva, y tras 30+ días de inactividad |
| Consentimiento de salud | Antes de la primera pregunta sobre tratamientos |
| Política completa | Sitio web, URL fija. Enlazada desde el perfil y el primer mensaje |
| Aviso corto | Perfil de WhatsApp Business (campo Descripción), formularios web, pie del sitio |
| Línea de BAJA | Todas las plantillas de **marketing**. No en utility ni service |

---

# 5. QUÉ GUARDAR Y QUÉ NO

## Guardar sí o sí — es la defensa

- ✅ **Registro de opt-in:** teléfono, fecha y hora, canal, texto mostrado, respuesta literal
- ✅ **Registro de consentimiento para datos sensibles**, por separado
- ✅ **Registro de bajas** con fecha — es la evidencia frente al SERNAC
- ✅ **Registro de actividades de tratamiento** (la planilla)
- ✅ **Log de solicitudes de derechos** y cuándo se respondieron
- ✅ Contrato de encargo firmado

## No guardar — esto reduce el riesgo más que cualquier cláusula

- ❌ **RUT**, salvo que sea imprescindible para facturar
- ❌ **Datos de tarjeta o medios de pago.** Nunca. Que lo maneje la pasarela.
- ❌ **Fotos de tratamientos, "antes y después", imágenes de la piel** — sin consentimiento
  expreso, específico y separado. Es lo más sensible que puede pasar por ese canal.
- ❌ Datos de terceros que el cliente mencione
- ❌ Conversaciones de gente que nunca se convirtió en cliente, más allá de unas semanas

💡 **La mitigación más barata y efectiva de todas: enmascarar los datos personales antes de armar
el prompt.** Que RUT, teléfonos, direcciones y correos no salgan del servidor hacia la API. Se
sustituyen por marcadores. Eso reduce el problema en origen mucho más que cualquier contrato.

## Cuánto retener

La ley no fija plazos — dice "solo el tiempo necesario". Esto es buena práctica:

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
- [ ] Definido por escrito si el desarrollador **opera** o **solo entrega** — determina si es
      encargado
- [ ] **Contrato de encargo** redactado o revisado por abogado
- [ ] Cuentas a nombre del **negocio**: Meta Business Portfolio, Anthropic, base de datos,
      alojamiento
- [ ] Número de WhatsApp **dedicado**, nunca el personal del dueño

**En la construcción (`/bot-probar`):**
- [ ] Base de datos en **São Paulo** — irreversible, se decide al crear
- [ ] Seguridad a nivel de fila activada en todas las tablas
- [ ] Credenciales solo en el servidor
- [ ] **Campo de bloqueo** que corte el procesamiento (para los 2 días hábiles)
- [ ] Campo de baja de marketing con fecha
- [ ] Borrado automático según la tabla de retención
- [ ] **Enmascarado de datos personales** antes de mandar el prompt

**En el guion (`/bot-planificar`):**
- [ ] System prompt **acotado al dominio** — exigencia de Meta
- [ ] **Declaración de IA** en el primer mensaje — exigencia de Anthropic
- [ ] Palabra HUMANO que derive a persona real — exigencia de Meta
- [ ] **El bot no da consejo de salud ni recomienda tratamientos** — exigencia de Anthropic
- [ ] **Sin botones de feedback** — evita la retención de 5 años

**Documentos:**
- [ ] Política de privacidad publicada en URL fija — revisada por abogado
- [ ] Aviso corto en el perfil de WhatsApp Business
- [ ] Registro de actividades de tratamiento
- [ ] Procedimiento escrito ante filtraciones

**Operación:**
- [ ] Verificación del negocio en Meta con documentos consistentes
- [ ] Plantillas con categoría honesta
- [ ] Línea de BAJA en toda plantilla de marketing
- [ ] Monitoreo semanal del quality rating

---

# 7. DÓNDE SE NECESITA ABOGADO

No improvises en estos puntos:

| Tema | Por qué |
|---|---|
| 🔴 **Contrato de encargo** | Define quién responde. Es el blindaje del desarrollador |
| 🔴 **Política de privacidad definitiva** | Los borradores de arriba son punto de partida |
| 🔴 **Si los datos del negocio califican como "de salud"** | Determina si es infracción gravísima |
| 🟡 Si aplica Evaluación de Impacto o DPO obligatorio | "Gran escala" no está definido numéricamente |
| 🟡 Si el art. 28 B del SERNAC cubre WhatsApp | Interpretación. Prudente asumir que sí |
| 🟡 Si aplica la atenuante PYME | Interacción entre dos leyes, no confirmada |
| 🟡 Validez de las cláusulas modelo del Min. de Economía | Hay crítica jurídica pública |
| 🟡 Plazo exacto de respuesta a derechos | Fuentes en conflicto (30 corridos vs 15 hábiles) |

---

# 8. LO QUE HAY QUE MONITOREAR

Cosas que pueden cambiar y que conviene revisar antes de cada proyecto nuevo:

1. **Si el Gobierno posterga la Ley 21.719.** Cambiaría todo el calendario. Sin anuncio oficial a
   agosto de 2026.
2. **Las tarifas de Chile publicadas por Meta** tras el cambio del 1-oct-2026.
3. **Si el estado "Flagged" sigue existiendo** en WhatsApp — fuentes contradictorias.
4. **El proyecto de ley de IA chileno**, en tramitación en el Senado con urgencia suma desde enero
   de 2026. Su artículo 12 contempla la obligación de informar que se interactúa con un sistema de
   IA. **Todavía no es ley**, pero la dirección es inequívoca — e implementarlo hoy es gratis,
   porque Anthropic ya lo exige.
