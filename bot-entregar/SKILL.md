---
name: bot-entregar
description: >
  Etapa 9 y última del sistema de bot de WhatsApp, solo cuando el bot es para un cliente de
  terceros. Cubre el manual de una página, la capacitación en vivo, el traspaso de cuentas a
  nombre del cliente, la estructura de precios con tope de conversaciones, el contrato de encargo
  de datos y qué pasa cuando termina la relación. Úsalo cuando el usuario escriba /bot-entregar, o
  cuando tenga que entregarle un bot de WhatsApp a un cliente que le paga.
---

# Etapa 9 de 9 — Entregar al cliente

**Solo si el bot es para un tercero.** Si es para el negocio propio del usuario, esta etapa no
existe: ya terminó.


---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md` y verifica dos cosas: que en la ficha diga que **el bot es para un cliente**
   (si es para el negocio propio del usuario, esta etapa no aplica — díselo y termina), y que el
   asistente **esté publicado y funcionando**. No se entrega algo que todavía no atiende.
3. Carga `~/.claude/skills/bot-whatsapp/references/entrega-cliente.md`.

---

## Lo que se entrega — 6 cosas

Detalle completo en la referencia:

1. **El asistente andando en el número definitivo del cliente**
2. **El manual de una página** — una sola. Si son tres, no la lee nadie
3. **Los accesos, a nombre del cliente** — con el desarrollador como invitado
4. **La Ficha del Bot** actualizada
5. **Los avisos legales instalados**, no entregados como archivo para que los ponga después
6. 🔴 **El contrato de encargo, firmado**

---

## Las tres conversaciones que hay que tener

### 1. Las cuentas quedan a nombre del cliente

⚠️ **Va en contra de lo que muchos hacen, y es innegociable.** Si quedan a nombre del
desarrollador: el cliente depende de él para siempre, si le pasa algo el negocio se queda sin su
WhatsApp, y legalmente queda respondiendo por datos que no son suyos.

Preséntalo como argumento de venta, no como concesión:

> *"Las cuentas quedan a tu nombre. Esto es tuyo. Yo tengo acceso mientras trabajemos juntos."*

### 2. El precio, con tope de conversaciones

🚨 **Desde octubre de 2026, la tarifa plana sin tope es una trampa.** Cada respuesta cuesta, así
que el cliente al que le va bien deja al desarrollador pagando de su bolsillo.

La estructura y los rangos están en la referencia. Lo esencial: instalación + mensualidad **con
tope**, y excedente cobrado aparte.

Y el argumento de venta en su idioma:

> *"¿Cuánto te deja un cliente promedio? ¿Cuántos se te pierden al mes porque no alcanzas a
> contestar? Si el asistente te rescata dos al mes, ya se pagó solo."*

### 3. Quién responde por los datos

Define **por escrito** si el desarrollador **solo entrega** (proveedor de desarrollo, exposición
baja) o si **hostea y opera** (encargado del tratamiento, exposición alta y contrato obligatorio).

Es la decisión con más impacto legal del proyecto y se toma el día uno.

---

## La capacitación — en vivo

No un video, no un PDF. En vivo, con el cliente frente a su teléfono:

1. **Que lo apague y lo prenda él.** Primero de todo, dos veces
2. Que le escriba y vea una conversación completa
3. Que provoque una derivación y vea llegar el aviso
4. Muéstrale dónde ve las conversaciones del día
5. Cuéntale qué pasa la primera semana y cómo pedirte ajustes

**Cierre:** *"apágalo tú una última vez, sin que yo te diga cómo"*. Si lo logra, terminó. Si no,
se repite el punto 1.

---

## Qué pasa si se cae

Sé específico. **Nada de "soporte 24/7" si eres una persona.** La tabla de compromisos realistas
está en la referencia.

⚠️ Lo que más importa que el cliente sepa **antes**: si se cae un proveedor externo, no hay nada
que hacer más que esperar y atender a mano.

---

## El gate de la etapa

La checklist completa está en la referencia. Los que no se saltan:

- [ ] 🔴 Contrato de encargo firmado por ambas partes
- [ ] 🚨 Método de pago registrado en la cuenta del cliente
- [ ] Las cuentas están a nombre del cliente
- [ ] **El cliente apagó y prendió el asistente él solo, sin ayuda**
- [ ] Precio, alcance y soporte por escrito
- [ ] Acordado qué pasa con los datos si termina la relación

---

## Al cerrar

1. Actualiza `ESTADO.md`: entregado, con fecha y condiciones.
2. Cierra el proceso:

> *"Listo, entregado. El cliente puede operarlo solo y tú tienes el respaldo por escrito. Si más
> adelante hay que ajustar el guion o agregar un servicio, se entra por **`/bot-bandeja`** y de
> ahí vemos."*

**Y una última cosa para el desarrollador:** un traspaso limpio el día que el cliente se vaya es
publicidad. Uno al que le retuviste sus cuentas habla mal de ti en el mismo barrio donde vendes.
