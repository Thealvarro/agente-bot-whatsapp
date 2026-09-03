# Anexo — Chile

**Se carga solo si el negocio está en Chile.** Complementa `legal.md`, que tiene lo que aplica en
todos los países (Meta, Anthropic y los principios de datos personales).

⚠️ **Investigación, no asesoría legal.** Datos al 31 de agosto de 2026.

---

# 1. Ley 21.719 — todavía no rige

- Publicada el 13-dic-2024. **Entrada en vigencia: 1 de diciembre de 2026.**
- **La Agencia de Protección de Datos no está operativa.** El Consejo Directivo debía constituirse
  a fines de mayo de 2026; el Senado rechazó la terna propuesta y a agosto de 2026 sigue sin
  nombrarse.
- **El Gobierno está evaluando postergar la entrada en vigencia.** Sin anuncio oficial.

**Qué rige hoy: la Ley 19.628**, de 1999. Mucho más laxa. Multas de 2 a 50 UTM (~$143.000 a
~$3.582.000). **Sin autoridad fiscalizadora** — hay que ir a tribunales civiles.

**Cómo leerlo sin equivocarse:** el riesgo regulatorio **hoy** es bajo; desde diciembre es alto.
Diseñar bien ahora cuesta casi lo mismo que diseñar mal, y adaptarlo después cuesta mucho más.
**Pero no le vendas urgencia falsa al usuario: la fecha se puede mover.**

⚠️ **Verificar antes de cada proyecto nuevo si el Gobierno postergó la vigencia.** Cambiaría todo
el calendario.

---

# 2. Bases legales para tratar datos

El artículo 13 establece cinco bases sin consentimiento: ejecución de contrato o medidas
precontractuales, obligación legal, **interés legítimo**, ejercicio de derechos ante tribunales, y
obligaciones económicas.

Aplicado a un bot:

| Situación | Base |
|---|---|
| Cliente escribe pidiendo hora | Medidas precontractuales — **no necesita consentimiento aparte** |
| Guardar historial para dar mejor servicio | Interés legítimo, con test de balanceo documentado |
| Mandarle promociones después | **Consentimiento** |
| Conversar sobre tratamientos, piel, alergias | 🔴 **Consentimiento expreso obligatorio** |

---

# 3. 🚨 Datos sensibles — el riesgo más grande

En Chile son **datos sensibles**: salud, perfil biológico y biométrico, origen racial, afiliación
sindical o política, convicciones religiosas, vida y orientación sexual, y —particularidad
chilena— **situación socioeconómica**.

Una estética, dental o peluquería conversa de tratamientos, condiciones de piel y alergias. **Eso
es dato de salud.**

- Requiere **consentimiento expreso**. El interés legítimo **no sirve** como base.
- **Tratarlos sin autorización es infracción gravísima** → hasta 20.000 UTM.
- Puede gatillar Evaluación de Impacto si es "a gran escala" (zona gris para un negocio chico).

---

# 4. Derechos del titular y plazos

Seis derechos: acceso, rectificación, supresión, oposición, portabilidad y bloqueo.

| Obligación | Plazo |
|---|---|
| Responder una solicitud | **30 días corridos**, prorrogable una vez por 30 más |
| **Bloqueo temporal** al recibir solicitud de rectificación, supresión u oposición | **2 días hábiles** |

⚠️ **El bloqueo en 2 días hábiles es el que pilla desprevenido.** Sin un indicador en la base de
datos que corte el procesamiento, no se puede cumplir. **Se prevé al construir.**

⚠️ Circulan fuentes que dicen "15 días hábiles". La lectura mejor sustentada es 30 días corridos.
**Confírmalo con abogado antes de escribirlo en un contrato.**

---

# 5. Multas

UTM a agosto de 2026: **$71.649**.

| Gravedad | Tope | En pesos |
|---|---|---|
| Leve | 5.000 UTM | ~$358 millones |
| Grave | 10.000 UTM | ~$716 millones |
| **Gravísima** | **20.000 UTM** | **~$1.433 millones** |

Reincidencia: la multa puede **triplicarse**. Hay **Registro Nacional de Sanciones público**, con
las sanciones visibles 5 años — para un negocio local, el daño reputacional puede pesar más que la
multa.

⚠️ **Atenuante PYME:** la Ley 20.416 establece que las empresas de menor tamaño reciben
amonestación escrita, no multa, en su primera infracción. **No confirmado en fuente primaria para
este régimen — punto de abogado.**

---

# 6. Registro ante autoridades

**No hay que inscribirse.** No existe obligación general de registrar la empresa ni sus bases de
datos ante la Agencia.

Lo que sí: un **registro interno de actividades de tratamiento** (una planilla). Se documenta, no
se presenta.

**Delegado de protección de datos:** obligatorio solo para organismos públicos y empresas cuya
actividad principal sea tratamiento a gran escala de datos sensibles. Un negocio local no
califica.

---

# 7. Datos fuera de Chile

Los artículos 27–29 lo regulan. La vía practicable son las **cláusulas contractuales tipo**.

✅ **El Ministerio de Economía ya aprobó las Cláusulas Contractuales Modelo** (resolución del
11-dic-2025, publicada el 19-dic-2025), vigentes de forma transitoria hasta que la Agencia ejerza
su facultad.

⚠️ Existe crítica jurídica pública que cuestiona su legalidad por haberse dictado antes de que
exista la Agencia. **Punto de abogado.**

💡 **Región recomendada para la base de datos: São Paulo.** Brasil tiene ley integral de
protección de datos —mucho mejor candidato a "nivel adecuado" que Estados Unidos— y baja la
latencia. **Se decide al crear el proyecto y no se puede cambiar después.**

---

# 8. Si hay una filtración

La ley exige notificar **"sin dilaciones indebidas"**. **No fija el plazo de 72 horas** del
reglamento europeo — muchas guías lo repiten mal.

- **A la Agencia:** cuando exista riesgo razonable para los titulares.
- **A los titulares:** obligatorio cuando involucra **datos sensibles**, datos de menores o datos
  económicos. **Un negocio de salud o estética cae acá.**
- Postergar el reporte mientras "se recopila información completa" es en sí mismo sancionable.

---

# 9. Publicidad y bajas

El **artículo 28 B de la Ley 19.496** está **vigente hoy** y exige que toda comunicación
promocional por mensajería incluya una forma expedita de suspenderlas. Una vez pedida la
suspensión, mandar nuevas comunicaciones queda prohibido.

**Multas de hasta 300 UTM (~$21,5 millones) por cada consumidor afectado.**

Existe además el **Sistema "No Molestar"** del SERNAC, donde los consumidores se inscriben.

⚠️ *"Servicios de mensajería telefónica"* se redactó antes de que existiera WhatsApp. Un abogado
podría discutir si aplica. **Lo prudente es asumir que sí** — cumplir cuesta cero.

**Esto solo importa si el negocio manda promociones.** Un bot reactivo no lo toca.

---

# 10. Tarifas de WhatsApp para Chile

**Chile es un mercado propio en el rate card de Meta.** No cae en "Rest of Latin America".

Fila del CSV oficial: `Chile,USD,0.0889,0.0200,0.0200,n/a,n/a`

| Categoría | USD/mensaje | ~CLP | Cuándo se cobra |
|---|---|---|---|
| **Marketing** | $0,0889 | ~$83 | Siempre |
| **Utility** | $0,0200 | ~$19 | Desde el 1-oct-2026, también dentro de la ventana |
| **Authentication** | $0,0200 | ~$19 | Siempre |
| **Service** (respuestas del bot) | $0 hasta 30-sep-2026, después ≈$0,0200 | ~$19 | Cada mensaje del bot |

⚠️ **La tarifa exacta de service para Chile no estaba publicada al cierre de esta investigación.**
Meta se comprometió a publicarla antes del 1-sep-2026. La estimación asume paridad con utility.
**Verifica el rate card antes de cotizar.**

**Marketing en Chile es carísimo:** 3ª tarifa más alta del mundo, detrás de Países Bajos y
Alemania. Es **7× Colombia** y **2,9× México**. Nunca vendas envíos promocionales sin mostrar ese
número primero.

Desde el 1-abr-2026 Meta factura en CLP para Chile.

---

# 11. Verificación del negocio en Chile

- Requiere **RUT de empresa** (no personal): e-RUT, escritura de constitución, comprobante de
  domicilio comercial
- Meta exige **presencia web con dominio propio**
- **Demora 2 a 7 días hábiles**
- **Causa #1 de rechazo:** inconsistencias entre nombre, dirección y RUT en los documentos

💡 **Si el negocio no tiene sitio web**, esto es un bloqueo — y también una oportunidad obvia de
venderle uno.

---

# 12. Lo que hay que monitorear

1. **Si el Gobierno posterga la Ley 21.719.** Sin anuncio oficial a agosto de 2026
2. **Las tarifas de Chile** tras el cambio del 1-oct-2026
3. **El proyecto de ley de IA chileno**, en tramitación en el Senado con urgencia suma desde enero
   de 2026. Su artículo 12 contempla la obligación de informar que se interactúa con un sistema de
   IA. **Todavía no es ley**, pero implementarlo hoy es gratis porque Anthropic ya lo exige

---

# 13. Textos con formato chileno

Los textos base están en `legal.md` sección 4. Para Chile, los ajustes:

- Donde dice `[ID TRIBUTARIO]` va **RUT**, con formato `XX.XXX.XXX-X`
- El plazo de respuesta a solicitudes es **30 días corridos**
- La retención sugerida de conversaciones: **24 meses**
