---
name: bot-probar
description: >
  Etapa 3 del sistema de bot de WhatsApp, y la más importante. Construye el asistente completo y
  lo pone a prueba en un simulador que se ve como WhatsApp, SIN conectar el número real ni usar
  credenciales. El usuario corre 14 pruebas desde su teléfono o pantalla, incluidos intentos de
  manipulación y cruce de conversaciones. Úsalo cuando el usuario escriba /bot-probar, o cuando
  quiera ver su bot funcionando antes de hacer el trámite con Meta.
---

# Etapa 3 de 9 — Construir y probar en demo

**El corazón del sistema.** Acá el usuario ve su asistente funcionando por primera vez, y lo
rompe a propósito — todo sin haber tocado WhatsApp.


---

## Antes de empezar

1. Carga `~/.claude/skills/bot-whatsapp/references/reglas.md`.
2. Lee `ESTADO.md`. **Necesitas la Ficha del Bot y el guion aprobados.** Si no están, mándalo de
   vuelta a `/bot-planificar` — no construyas a ciegas.
3. Carga `~/.claude/skills/bot-whatsapp/references/construccion.md` — la guía técnica: stack,
   integración con Zernio, estructura del proyecto y las trampas de su API.
4. Carga `~/.claude/skills/bot-whatsapp/references/demo.md`.

---

## Parte 1 — Construir *(trabajas tú, el usuario espera)*

**Las 6 piezas, y el orden importa.** No construyas el cerebro primero: si los mensajes no llegan
y no se guardan, vas a depurar a ciegas.

| # | Pieza | Qué hace | Verificada cuando… |
|---|---|---|---|
| 1 | **La puerta** | Recibe el mensaje, valida el origen, confirma recepción al tiro y procesa aparte | Un mensaje queda registrado, y uno inválido se rechaza |
| 2 | **La memoria** | Conversaciones, contactos, consentimientos, bajas, indicador de bloqueo | Dos conversaciones simultáneas no se cruzan |
| 3 | **El cerebro** | Las reglas del negocio + el guion aprobado | Responde el precio exacto de la lista, no uno inventado |
| 4 | **Las acciones** | Consultar agenda, agendar, derivar a humano | Solo ofrece horas que existen de verdad |
| 5 | **Los controles** | Apagado, tope de gasto, límite por persona, modo borrador | El dueño lo apaga solo y deja de responder |
| 6 | **El simulador** | La pantalla que se ve como WhatsApp | El usuario conversa con su bot |

**Cada pieza se verifica antes de montar la siguiente.** Es la diferencia entre encontrar un
problema en 5 minutos o al final sin saber cuál de seis piezas lo causó.

### La séptima pieza: la auditoría

Junto con el bot **generas el script de auditoría y los 3 tests innegociables**. Carga
`~/.claude/skills/bot-whatsapp/references/verificacion.md`.

**No es un extra ni algo para después.** Es lo que convierte los 53 controles de una lista que tú
marcas en verificaciones que corren. Sin esto, `/bot-revisar` es una compuerta decorativa.

Los tests van saliendo con cada pieza: cuando termines la memoria, escribes el test de que dos
conversaciones no se cruzan; cuando termines los controles, el de que el tope de gasto corta.

### Obligatorio en esta parte

- **Todo el blindaje de `seguridad.md`, Parte B.** Los 53 ítems. No es opcional ni "lo dejamos
  para cuando conectemos".
- ⚠️ **Las dos decisiones irreversibles:** región de la base de datos en São Paulo (no EEUU) y
  aislamiento multi-cliente. Se deciden al crear, no después.
- **La capa de mensajería aislada.** El simulador y WhatsApp entran por la misma puerta interna.
- **Antes de escribir código con las herramientas de mensajería, lee su documentación oficial.**
  Son recientes y cambian; no te fíes de la memoria.

---

## Parte 2 — Las 14 pruebas *(las hace el usuario)*

Carga `~/.claude/skills/bot-whatsapp/references/pruebas.md`.

Encuádralo así:

> *"Ahora viene la parte entretenida: vas a tratar de romperlo. Son 14 pruebas, te digo
> exactamente qué escribir y qué debería pasar. Si alguna falla, la arreglo y la repetimos."*

**Una prueba por turno.** Le dices qué escribir, espera que lo haga, te cuenta qué pasó, sigue la
siguiente.

**Por qué las hace él y no tú:** porque tiene que confiar en esto antes de soltarlo con clientes
reales. Un informe tuyo diciendo "probé todo y funciona" no genera esa confianza. Verlo en su
pantalla, sí.

### Reglas durante las pruebas

- **Si una falla, no la minimices.** Arréglala y repítela.
- **No arregles una prueba haciéndola más fácil.** Si el asistente cede ante la prueba 6, la
  solución no es cambiar la prueba.
- **Cada falla nueva se convierte en prueba permanente** para la próxima vez.
- **Las pruebas 11 y 13 no se saltan nunca**, aunque insista. Una filtra datos entre clientes y la
  otra lo deja sin control de su propio sistema.

---

## Parte 3 — El teléfono real *(recomendado)*

Cuando las 14 pasen, ofrécele probarlo **en su propio WhatsApp** con el número de prueba de Meta:
gratis, hasta 5 teléfonos registrados, sin tarjeta ni verificación.

Es distinto verlo en el computador que recibir el mensaje en el celular. Es la última
confirmación antes del trámite.

---

## El gate de la etapa

- [ ] Las 14 pruebas pasan
- [ ] El usuario conversó con su asistente y le gustó cómo responde
- [ ] La lista de blindaje de `seguridad.md` está cumplida entera, verificada **contra el sistema
      real**, no contra tu recuerdo de haberla hecho

---

## Si algo no aparece

| Debería ver | Si no pasa |
|---|---|
| Su asistente respondiendo en la pantalla de prueba | Si no responde, no sigas con las pruebas: primero anda la conversación básica |
| El precio exacto de su lista | Si dice otro, está inventando. Es lo más grave: se arregla antes que nada |
| Que se cansa por la prueba 9 | Es normal, son muchos turnos. Ofrece parar y deja las 5 innegociables para una segunda sesión |
| Que dice "ya vi que funciona, sigamos" | Tiene razón en sentirlo. Explícale cuáles faltan y por qué, con el motivo concreto de cada una |

Si pasa algo que no está en esta tabla, **no le pases el problema al usuario**: arréglalo y
cuéntale solo lo que necesita saber.

---

## Al cerrar

1. Actualiza `ESTADO.md`: etapa cerrada, 14 pruebas pasadas con fecha.
2. Manda al siguiente paso, y **prepáralo para lo que viene**:

> *"Tu asistente funciona y ya lo comprobaste tú mismo. Ahora sí viene el trámite: conectar tu
> WhatsApp de verdad. Te aviso que esta es la parte más lenta y la que depende de Meta, no de
> nosotros. Pero ya sabes que lo que estás conectando
> sirve. Escribe **`/bot-conectar`**."*
