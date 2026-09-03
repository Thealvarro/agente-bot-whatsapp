---
name: bot-revisar
description: >
  Etapa 5 del sistema de bot de WhatsApp. La compuerta de seguridad antes de encender: recorre los
  53 ítems de blindaje contra el sistema real y entrega un veredicto en lenguaje humano. Verifica
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
4. Carga `~/.claude/skills/bot-whatsapp/references/legal.md`, sección 6.

---

## Cómo se corre

**Dos partes, y la primera no es opinable.**

### Parte 1 — Corres la auditoría

Ejecutas el script de auditoría que se generó en `/bot-probar` (12 chequeos) y los **3 tests
innegociables**. Detalle en `verificacion.md`.

Esto no se lee ni se interpreta: **se corre**. Si algo falla, lo arreglas y vuelves a correr
**todo**, no solo lo que falló.

⚠️ **Si el script no existe** porque `/bot-probar` se hizo sin él, genéralo ahora antes de seguir.
Una compuerta sin verificación ejecutable es una compuerta decorativa.

### Parte 2 — Revisas a mano lo que no se automatiza

Los ítems que dependen de mirar: avisos legales publicados, contrato firmado, humano de respaldo
avisado, calidad del guion.

⚠️ **Regla dura:** si un ítem no se cumple, no está "casi listo": está **sin hacer**.

🚫 **Y nunca reportes como verificado algo que solo miraste.** En el reporte van separados: lo que
se probó corriendo y lo que se revisó a mano. Confundir "lo leí" con "lo probé" es exactamente el
problema que esta etapa existe para evitar.

Al usuario **no le muestras la checklist técnica.** Le muestras el resultado por bloques, en su
idioma:

```
REVISIÓN DE SEGURIDAD — [negocio]

PROBADO (se corrió de verdad)
  La puerta de entrada        ✓  Solo entran mensajes de WhatsApp de verdad
  El comportamiento del bot   ✓  No se deja manipular, no inventa precios
  Protección de tu cuenta     ✓  El tope de gasto corta, no solo avisa
  Tus llaves                  ✓  Guardadas donde corresponde
  Datos de tus clientes       ✓  Un cliente no puede ver los de otro

REVISADO A MANO
  Avisos legales              ✓  Publicados y enlazados
  Tu humano de respaldo       ✓  Avisado y recibiendo las derivaciones

Tu asistente está listo para atender clientes reales.
```

**La separación importa y es honesta:** lo de arriba se comprobó corriendo pruebas; lo de abajo lo
revisó una persona. Si algún día algo falla, saber cuál era cuál ahorra medio día de búsqueda.

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

- [ ] Los 53 ítems verificados contra el sistema real
- [ ] Los 3 críticos, en verde
- [ ] El usuario vio el reporte de los 7 bloques

---

## Si algo no aparece

| Debería ver | Si no pasa |
|---|---|
| El reporte separado: probado y revisado a mano | Si no corriste la auditoría, no hay reporte que mostrar. Córrela |
| Todo en verde | Si algo falla, lo arreglas y corres **todo** de nuevo. No solo lo que falló |
| El script no existe | Se hizo `/bot-probar` sin él. Genéralo ahora: sin auditoría esta etapa es decorativa |

Si pasa algo que no está en esta tabla, **no le pases el problema al usuario**: arréglalo y
cuéntale solo lo que necesita saber.

---

## Al cerrar

1. Actualiza `ESTADO.md`: revisión pasada con fecha. Si quedó algo pendiente aceptado por el
   usuario, va a RIESGOS ACEPTADOS.
2. Manda al siguiente paso:

> *"Todo en orden. Vamos a encenderlo — pero con ruedas de apoyo: los primeros días tú apruebas
> las respuestas antes de que salgan. Escribe **`/bot-publicar`**."*
