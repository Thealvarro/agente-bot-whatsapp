# Entrega al cliente

**Aplica solo si el bot es para un tercero.** Si el usuario lo construyó para su propio negocio,
salta esta fase completa.

**Objetivo:** que el cliente pueda operar su asistente sin llamar al desarrollador por cualquier
cosa, y que la relación comercial quede clara antes del primer problema.

---

## Lo que se entrega

Cinco cosas. Ni una menos.

### 1. El asistente andando

Obvio, pero con una condición: **andando en el número del cliente**, no en uno de prueba. Si
todavía está en un número temporal, no está entregado.

### 2. El manual de una página

Una sola página. Si son tres, no la va a leer nadie. Contenido exacto:

```
TU ASISTENTE DE WHATSAPP — [Negocio]

CÓMO LO APAGAS
[instrucción de 1 línea, con el link o el botón exacto]

CÓMO LO PRENDES DE NUEVO
[instrucción de 1 línea]

DÓNDE VES LAS CONVERSACIONES
[link o app]

DÓNDE TE LLEGAN LOS AVISOS CUANDO PIDE AYUDA
[canal]

QUÉ HACE SOLO
· [3 cosas]

QUÉ NO HACE NUNCA
· [3 cosas]

SI ALGO SALE MAL
1. Apágalo (arriba dice cómo)
2. Escríbeme a [contacto]
3. Contesta tú los mensajes mientras tanto

QUÉ ESTÁ INCLUIDO EN TU PLAN
[lista corta]

QUÉ SE COBRA APARTE
[lista corta]
```

### 3. Los accesos

Las cuentas tienen que quedar **a nombre del cliente**, con el desarrollador como invitado.

⚠️ **Esto es innegociable y va en contra de lo que muchos hacen.** Si las cuentas quedan a tu
nombre:
- El cliente depende de ti para siempre, lo que suena bien hasta que se pelean
- Si te pasa algo, el negocio se queda sin su WhatsApp
- Legalmente quedas tú como responsable de datos que no son tuyos

Ponlo como argumento de venta, no como concesión: *"las cuentas quedan a tu nombre, esto es tuyo.
Yo tengo acceso mientras trabajemos juntos"*.

### 4. La Ficha del Bot

La misma de `/bot-planificar`, actualizada. Es el documento que dice qué hace y qué no hace. Cuando en 6
meses el cliente diga "pero yo pensé que también hacía X", la ficha responde por ti.

### 5. Los avisos legales instalados

Ver `legal-chile.md`. El aviso de privacidad y la mención de que es un asistente tienen que estar
puestos, no entregados como archivo para que el cliente los ponga después.

### 6. El contrato de encargo, firmado

🔴 **Sin esto no se entrega.** Define quién responde por los datos de los clientes finales. Ver
`legal-chile.md` sección 3.4 para el contenido mínimo, y hazlo revisar por un abogado.

No es un trámite: es el documento que decide si un problema de datos lo paga el negocio o lo pagas
tú.

---

## Cómo le enseñas

**Una sesión en vivo, con el cliente frente a su teléfono.** No un video, no un
PDF. En vivo.

Guion de la sesión:

1. **Que lo apague y lo prenda él.** Primero de todo. Que lo haga con sus manos, dos veces.
2. **Que le escriba al asistente** desde su teléfono y vea una conversación completa.
3. **Que provoque una derivación** — que escriba "quiero hablar con una persona" y vea llegar el
   aviso a su canal.
4. **Muéstrale dónde ve las conversaciones** del día.
5. **Cuéntale qué va a pasar la primera semana:** que va a haber ajustes, que es normal, y cómo
   pedírtelos.

**Cierre de la sesión:** *"apágalo tú una última vez, sin que yo te diga cómo"*. Si lo logra, la
capacitación terminó. Si no, se repite el punto 1.

---

## Qué cobrar

No hay un número correcto, pero sí una estructura correcta: **instalación + mensualidad**. Nunca
solo instalación.

**Por qué nunca solo un pago único:** el asistente tiene costos que corren todos los meses
(mensajería, modelo, alojamiento) y va a necesitar ajustes. Si cobras una sola vez, en el mes 3
estás trabajando gratis y pagando de tu bolsillo.

### 🚨 La mensualidad tiene que llevar tope de conversaciones

**Esto cambió el 1 de octubre de 2026.** Antes, responder por WhatsApp era gratis y una tarifa
plana funcionaba. Ahora **cada respuesta del asistente cuesta ~$19 pesos**, así que el costo sube
con el uso del cliente.

**Una tarifa plana sin tope es una trampa:** el cliente al que le va bien te deja pagando de tu
bolsillo. Es exactamente el cliente que no quieres perder.

### Estructura sugerida para negocios locales chilenos

| Concepto | Rango referencial | Qué cubre |
|---|---|---|
| **Instalación** | $150.000 – $400.000 | Descubrimiento, guion, conexión, pruebas, capacitación |
| **Mensualidad** | $50.000 – $120.000 | Operación, monitoreo, ajustes menores, soporte — **con tope de conversaciones** |
| **Excedente** | ~$300 por conversación sobre el tope | Se cobra aparte, avisando antes |

**El tope que funciona:** **150 conversaciones al mes** cubre cómodo a una peluquería, una dental
chica o una estética de barrio. Con ese tope, la mensualidad de $50.000 deja margen sano.

**Cómo elegir dentro del rango:**
- Negocio chico, un servicio, sin agenda conectada → parte baja
- Varios servicios, agenda conectada, varias sucursales → parte alta
- Si el bot le va a ahorrar contratar a alguien → parte alta, sin culpa
- Si el cliente tiene mucho volumen → **sube el tope y sube el precio**, no regales el excedente

⚠️ **Si vendiste bots con tarifa plana antes de octubre de 2026, hay que repactar.** Es mejor una
conversación incómoda ahora que una pérdida silenciosa cada mes.

**El costo real que estás cubriendo:** con 5 clientes de 150 conversaciones, cada uno te cuesta
~$19.000 al mes entre mensajería, modelo y alojamiento. El detalle está en
`herramientas-costos.md`.

### El argumento de venta, en su idioma

No vendas "un bot con inteligencia artificial". Vende la cuenta:

> *"¿Cuánto te deja un cliente promedio? ¿Y cuántos se te pierden al mes porque no alcanzas a
> contestar, o porque escribieron un domingo? Si el asistente te rescata dos al mes, ya se pagó
> solo."*

Para eso sirve la métrica de la pregunta 12 de la Ficha del Bot. Si la mediste, al mes 2 tienes
el número real y la conversación de renovación se gana sola.

### Lo que va aparte — dilo antes, no después

- Cambios grandes al guion (no un ajuste de texto: un servicio nuevo, un flujo nuevo)
- Conectar sistemas nuevos (agenda, sistema de ventas, otro canal)
- Un segundo número o una segunda sucursal
- Soporte fuera de horario hábil

Ponlo por escrito en el manual. El 90% de los conflictos con clientes son por expectativas de
soporte que nunca se conversaron.

---

## Qué pasa si se cae

Sé honesto y específico. Nada de "soporte 24/7" si eres una persona.

Compromiso realista para un freelance:

| Situación | Respuesta |
|---|---|
| El asistente responde raro | Mismo día hábil |
| El asistente no responde | Dentro de 4 horas hábiles |
| El asistente dice algo grave a un cliente | Lo apagas tú al tiro, yo respondo apenas pueda |
| Se cae un proveedor externo | Depende de ellos. Te aviso y contestas tú mientras tanto |

⚠️ **La última fila importa.** El asistente depende de servicios de terceros. Si se cae el
proveedor de mensajería, no hay nada que hacer más que esperar y atender a mano. Que el cliente
lo sepa **antes**, no el día que pasa.

---

## Quién responde por los datos

Esto no es burocracia: define quién paga si hay un problema.

**Ante la ley, el responsable es el negocio**, no el desarrollador. El negocio decide para qué se
usan los datos; el desarrollador los procesa por encargo. El negocio no puede escudarse en "me lo
hizo un freelance".

**Pero ojo — acá está lo que protege al desarrollador, o lo hunde:** si no hay contrato escrito,
el negocio queda expuesto ante la autoridad… y después demanda civilmente al desarrollador. **El
contrato protege a los dos.**

### La distinción que cambia toda la exposición

| Si el desarrollador… | Su rol legal | Su exposición |
|---|---|---|
| **Solo construye y entrega**, y el negocio opera todo con sus propias cuentas | Proveedor de desarrollo — **no trata datos** | Baja |
| **Hostea, opera o accede** a las conversaciones | **Encargado del tratamiento** | Alta, y necesita contrato sí o sí |

**Defínelo el día uno, por escrito.** Es la decisión con más impacto legal de todo el proyecto, y
se toma antes de escribir una línea.

Es también la razón de fondo de la regla de más arriba: **cuentas a nombre del cliente**. No es
solo buena onda comercial — te saca de encima la responsabilidad de custodiar datos que no son
tuyos.

🔴 **No entregues un bot sin contrato de encargo firmado.** Lo debe redactar o revisar un abogado.
El contenido mínimo está en `legal-chile.md`, sección 3.4.

⚠️ **Si el negocio maneja datos de salud** (estética, dental, consulta), esto sube de categoría:
tratarlos sin autorización es la infracción más grave de la ley. Ver `legal-chile.md`, sección
3.3.

---

## Cuándo termina la relación

Define el traspaso **antes** de empezar, no cuando el cliente se quiera ir:

- Las cuentas ya están a su nombre — solo se quita al desarrollador de los accesos
- Se le entrega una copia de sus conversaciones y contactos
- Se le dice con qué se queda funcionando y con qué no
- Se borran los datos del lado del desarrollador

**Un traspaso limpio es publicidad.** Un cliente que se fue bien recomienda; uno al que le
retuviste sus cuentas habla mal de ti en el mismo barrio donde vendes.

---

## Checklist de entrega

Antes de dar por cerrada `/bot-entregar`:

- [ ] 🔴 **Contrato de encargo firmado** por ambas partes
- [ ] 🚨 **Método de pago registrado** en la cuenta de WhatsApp Business del cliente
- [ ] El asistente corre en el número definitivo del cliente
- [ ] El manual de una página, entregado y leído
- [ ] Las cuentas están a nombre del cliente
- [ ] El cliente apagó y prendió el asistente él solo, sin ayuda
- [ ] El cliente vio llegar un aviso de derivación a su canal real
- [ ] La Ficha del Bot, entregada y aceptada
- [ ] Los avisos legales, instalados
- [ ] Precio, alcance y soporte por escrito
- [ ] Acordado qué pasa con los datos si termina la relación
