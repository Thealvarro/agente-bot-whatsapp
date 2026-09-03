---
name: bot-revisar
description: >
  Etapa 5 del sistema de bot de WhatsApp. La compuerta de seguridad antes de encender: recorre los
  51 ítems de blindaje contra el sistema real y entrega un veredicto en lenguaje humano. Verifica
  entrada, control del modelo, abuso y costo, secretos, datos personales, control humano y
  cumplimiento legal. Úsalo cuando el usuario escriba /bot-revisar, o antes de poner un bot de
  WhatsApp en producción.
---

# Etapa 5 de 9 — La revisión

**La última red antes de que un cliente real le escriba.** Es la etapa que
más problemas evita por minuto invertido.

---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md`. **El número tiene que estar conectado** (`/bot-conectar` cerrado). Si no,
   mándalo ahí primero: media compuerta revisa cosas que no existen todavía y da un falso
   aprobado.
3. Carga `~/.claude/skills/bot-whatsapp/references/seguridad.md`, **Parte B**.
4. Carga `~/.claude/skills/bot-whatsapp/references/legal-chile.md`, sección 6.

---

## Cómo se corre

**Recorres los 51 ítems tú, contra el sistema real.** No contra tu recuerdo de haberlos hecho.

⚠️ **Regla dura:** si un ítem no se cumple, no está "casi listo": está **sin hacer**. Vuelve y
hazlo antes de seguir.

Al usuario **no le muestras la checklist técnica.** Le muestras el resultado por bloques, en su
idioma:

```
REVISIÓN DE SEGURIDAD — [negocio]

La puerta de entrada        ✓  Solo entran mensajes de WhatsApp de verdad
El comportamiento del bot   ✓  No se deja manipular, no inventa precios
Protección de tu cuenta     ✓  Topes y frenos activos
Tus llaves                  ✓  Guardadas donde corresponde
Datos de tus clientes       ✓  Aislados y con borrado automático
Tus controles               ✓  Apagado y bandeja funcionando
Reglas de Meta y la ley     ✓  Avisos puestos, método de pago registrado

Tu asistente está listo para atender clientes reales.
```

Si algo falla, sé concreto sobre **qué** falta y **qué significa**, sin tecnicismos:

> *"Falta una cosa: el asistente todavía puede seguir respondiendo si alguien manda cientos de
> mensajes seguidos. Lo arreglo ahora mismo."*

---

## Los 7 bloques que verificas

Detalle completo en `seguridad.md`, Parte B.

| Bloque | Qué revisas |
|---|---|
| **B1 · Entrada** | Firma verificada, comparación segura, respuesta inmediata, idempotencia, límite de tamaño, tipos no soportados |
| **B2 · El modelo** | Separación de instrucciones y contenido, ninguna acción irreversible en manos del modelo, precios desde fuente de verdad, salida saneada, dominio acotado, declaración de IA, nada de consejo de salud |
| **B3 · Abuso y costo** | Límite por teléfono, tope de gasto que **corta**, tope por conversación, detección de bucle bot-a-bot |
| **B4 · Secretos** | Todo server-side, nada commiteado, nada en logs |
| **B5 · Datos** | Aislamiento por negocio, logs sin contenido sensible, retención automática, indicador de bloqueo, enmascarado antes del prompt, región São Paulo |
| **B6 · Control humano** | Bandeja activa, apagado que el dueño usa solo, escalamiento automático, respuesta segura ante falla |
| **B7 · Cumplimiento** | Ventana calculada, nada de mensajes no solicitados, vía al humano, línea de baja, **método de pago registrado** |

---

## Los 3 que no pasan nunca por alto

Si alguno de estos falla, **no se enciende**, sin discusión y sin importar cuánto insista:

1. **Cruce de conversaciones entre clientes** — es una filtración de datos personales, con
   consecuencias legales reales.
2. **El tope de gasto no corta** (solo avisa) — no es un tope, es una notificación de que ya
   gastaste.
3. **Método de pago sin registrar** — el bot va a dejar de responder y nadie se va a enterar.

---

## El gate de la etapa

- [ ] Los 51 ítems verificados contra el sistema real
- [ ] Los 3 críticos, en verde
- [ ] El usuario vio el reporte de los 7 bloques

---

## Al cerrar

1. Actualiza `ESTADO.md`: revisión pasada con fecha. Si quedó algo pendiente aceptado por el
   usuario, va a RIESGOS ACEPTADOS.
2. Manda al siguiente paso:

> *"Todo en orden. Vamos a encenderlo — pero con ruedas de apoyo: los primeros días tú apruebas
> las respuestas antes de que salgan. Escribe **`/bot-publicar`**."*
