# El estado — cómo el sistema sabe dónde va el usuario

Este proceso se corta muchas veces — es normal y está diseñado así. **El estado es lo único que
hace que retomar no signifique repetir.**

---

## Dónde vive

Un solo archivo, en la carpeta del proyecto del bot:

```
ESTADO.md
```

**Léelo al empezar CUALQUIER comando.** Si no existe, el usuario está partiendo: mándalo a
`/bot-planificar`.

**Actualízalo al cerrar cualquier etapa**, y también cuando el usuario decida algo que cambie el
plan. Un estado desactualizado es peor que no tenerlo.

---

## Qué contiene

```markdown
# ASISTENTE DE WHATSAPP — [Nombre del negocio]

## DÓNDE VAMOS
Etapa actual: [nombre]
Siguiente comando: /bot-[el que corresponda]
Última sesión: [fecha]
Esperando de [nombre del usuario]: [lo que él tiene que hacer, o "nada"]

## ETAPAS
- [x] Planificar — cerrada el [fecha]
- [x] Costos — cerrada el [fecha]
- [ ] Probar en demo — EN CURSO, falta [qué]
- [ ] Conectar WhatsApp
- [ ] Revisar
- [ ] Publicar
- [ ] Operar (bandeja)
- [ ] Soltar
- [ ] Entregar

## FICHA DEL BOT

QUÉ ES EL NEGOCIO
[una o dos frases]

DÓNDE ESTÁ
[ciudad, país] — moneda: [X] — anexo legal: [archivo o "sin anexo"]

A QUIÉN ATIENDE
[tipo de cliente]

LO QUE EL ASISTENTE RESUELVE SOLO
· [cosa 1]
· [cosa 2]

LO QUE EL ASISTENTE NUNCA HACE SOLO
· [límite 1]
· [límite 2]

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

¿PARA QUIÉN ES?
[negocio propio / cliente de [nombre]]

## DECISIONES TOMADAS
- [fecha] [qué se decidió y por qué]

## RIESGOS ACEPTADOS
- [fecha] [qué se saltó el usuario y qué le advertiste]

## PENDIENTES
- [ ] [cosa que quedó colgando]
```

---

## Cómo se usa al retomar

Cuando el usuario vuelve después de días:

1. **Lee el estado.**
2. **Resume en dos frases** dónde quedaron y qué sigue.
3. **No vuelvas a preguntar lo que ya está en la ficha.** Nada mata más rápido la confianza que
   un mentor que se olvidó de lo que le contaste el martes.
4. Si estaba esperando algo de él, pregúntale por eso primero.

Ejemplo de un buen retome:

> *"Hola de nuevo. Quedamos en que tu asistente ya pasó las 14 pruebas en modo demo y estábamos
> por conectar tu WhatsApp de verdad. Quedaste de conseguir un número dedicado — ¿lo tienes?"*

---

## Cuando pasó mucho tiempo

Si volvió después de **más de dos semanas**, antes de seguir revisa dos cosas:

- Que las cuentas conectadas sigan vivas
- Que no haya cambiado nada en `legal.md` ni en el anexo del país — tienen fechas que se mueven

Díselo en una frase, sin alarmarlo: *"pasó un tiempo, déjame revisar que todo siga en pie antes
de seguir"*.

---

## Las etapas y sus gates

Ninguna etapa se cierra sin su gate. **El gate es siempre algo que el usuario vio**, no algo que
tú verificaste.

| Etapa | Comando | Se cierra cuando… |
|---|---|---|
| Planificar | `/bot-planificar` | Existe la Ficha del Bot aprobada y el guion leído |
| Costos | `/bot-costos` | El usuario aceptó la tabla de costos explícitamente |
| Probar en demo | `/bot-probar` | **Las 14 pruebas pasan, sin haber tocado WhatsApp todavía** |
| Conectar | `/bot-conectar` | Un mensaje real del usuario llega al sistema |
| Revisar | `/bot-revisar` | La compuerta pasa entera |
| Publicar | `/bot-publicar` | El bot atendió a un cliente real y el usuario sabe apagarlo |
| Operar | `/bot-bandeja` | Se usa a diario, no se "cierra" |
| Soltar | `/bot-soltar` | El bot responde solo, con las métricas cumplidas |
| Entregar | `/bot-entregar` | El cliente sabe operarlo y las cuentas son suyas |

---

## Regla sobre el orden

Las etapas van en orden, **con una excepción deliberada**: `/bot-probar` va **antes** de
`/bot-conectar`.

**Por qué importa:** conectar WhatsApp es el paso más frágil —depende de Meta, puede demorar
días, y un error quema el número para siempre. Meter a alguien en ese trámite antes de que haya
visto su asistente funcionar es la mejor forma de que abandone.

Con el orden correcto, cuando llega al trámite ya vio su bot conversando y sabe que sirve.

**Si el usuario quiere saltarse una etapa:** dile qué se está saltando y qué pasa si eso falla
después. Si insiste, es su decisión — anótalo en RIESGOS ACEPTADOS y sigue. No pelees dos veces.
