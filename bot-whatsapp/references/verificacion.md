# Verificación ejecutable — que las reglas se cumplan, no que se digan

**Para ti, el agente. El usuario nunca ve este archivo.**

Se usa en `/bot-probar` (para generar) y en `/bot-revisar` (para correr).

---

## El problema que resuelve

El sistema tiene 51 controles de seguridad bien pensados. Y hasta acá, **cero garantía de que se
cumplan**: `/bot-revisar` depende de que tú los recorras y seas honesto contigo mismo. Puedes
marcar *"✓ tope de gasto configurado"* porque **recuerdas** haberlo hecho, o porque el código
*parece* hacerlo.

Un script no recuerda ni interpreta: ejecuta y falla.

**La regla:** todo control que se pueda verificar corriendo algo, **se verifica corriendo algo**.
Lo que quede como lectura tuya, se marca explícitamente como tal para que nadie confunda "lo miré"
con "lo probé".

---

## Qué se automatiza y qué no

| Se verifica corriendo | Queda como revisión tuya |
|---|---|
| La firma rechaza lo que no viene del proveedor | Que los avisos legales estén publicados |
| El mismo evento dos veces produce una sola respuesta | Que el contrato esté firmado |
| El tope de gasto **corta**, no solo avisa | Que el dueño sepa apagarlo solo *(es humano, va en la prueba 13)* |
| Dos conversaciones no se cruzan | Que el humano de respaldo esté avisado |
| El borrador no se puede saltar | La calidad del guion |
| No hay credenciales en el código | |
| El bot no inventa precios | |
| La base está en la región correcta | |

**Nunca reportes como verificado un ítem de la columna derecha.** Se presentan aparte, como
"revisado a mano".

---

# 1. El script de auditoría

En `/bot-probar`, junto con el bot, **generas un script de auditoría dentro del proyecto**. No es
un extra: es parte de la construcción.

Debe poder correrse con un comando y devolver código de salida distinto de cero si algo falla.

## Los 12 chequeos que corre

### Entrada
1. **Sin firma → rechazado.** Un request sin el header de firma devuelve 401 y **no** llega al
   modelo.
2. **Firma inválida → rechazado.** Firma mal calculada, mismo resultado.
3. **Comparación en tiempo constante.** Busca en el código que la validación no use comparación
   directa de strings.
4. **Evento repetido → una sola respuesta.** El mismo identificador dos veces produce **una**
   llamada al modelo.
5. **Respuesta rápida.** El endpoint confirma en menos de 2 segundos aunque el modelo demore.

### Comportamiento
6. **No inventa precios.** Pregunta por un servicio que no está en la lista; la respuesta no
   contiene una cifra.
7. **Dominio acotado.** Pregunta algo fuera del negocio; la respuesta redirige y no responde.
8. **Declaración de IA.** El primer mensaje de una conversación nueva la contiene.

### Protección
9. **El tope de gasto corta.** Se fija un tope mínimo, se fuerza a alcanzarlo, y el siguiente
   mensaje **no** genera llamada al modelo.
10. **Límite por teléfono.** N mensajes seguidos del mismo número no producen N respuestas.

### Datos y secretos
11. **Sin credenciales en el código.** Busca patrones de llaves en todo el proyecto y verifica que
    el archivo de variables esté excluido del control de versiones.
12. **Aislamiento.** Dos negocios distintos en la misma base: uno no puede leer los datos del
    otro, ni con una consulta hecha a propósito.

## Cómo se reporta

**Al usuario nunca le muestras la salida del script.** Le muestras el resultado por bloques, en su
idioma — el formato está en `/bot-revisar`.

Si algo falla, **no lo interpretes ni lo minimices**: arréglalo y vuelve a correr. Un chequeo que
falla no está "casi bien".

---

# 2. Los tres tests innegociables

Además del script, el proyecto lleva tres pruebas automatizadas. **Son las tres que, si fallan en
producción, no tienen vuelta atrás.**

## Test 1 · El borrador no se puede saltar

Mientras el modo borrador está activo, **nada sale sin aprobación**. El test intenta forzar un
envío por todas las vías que existan en el código y exige que **no ocurra absolutamente nada**.

**Por qué es el más importante:** el modo borrador es la única protección real durante los
primeros días. Si se puede saltar por un camino que nadie previó, la protección no existe — y
nadie se entera hasta que un cliente recibe algo que no debía.

## Test 2 · Las conversaciones no se cruzan

Dos conversaciones simultáneas de personas distintas. El test verifica que el contexto de una
**jamás** aparezca en la otra, incluidas las condiciones de carrera: dos mensajes que llegan en el
mismo instante.

**Por qué:** un cliente viendo datos de otro es una filtración de datos personales con
consecuencias legales, no un error de presentación.

## Test 3 · El tope de gasto corta

Se alcanza el tope y el test exige que el siguiente mensaje **no** genere una llamada al modelo.
No que se registre una advertencia: que **no ocurra la llamada**.

**Por qué:** un tope que avisa pero no corta no es un tope, es una notificación de que ya
gastaste.

---

## Cuándo corren

- **Al terminar cada pieza en `/bot-probar`** — los que apliquen a esa pieza
- **Completos en `/bot-revisar`**, antes de encender
- **Después de cualquier cambio al guion o a las reglas**, en la operación diaria

⚠️ **Si el usuario pide saltarse la auditoría por apuro:** los 12 chequeos corren en segundos, no
hay apuro que lo justifique. Y los tres tests innegociables **no se saltan nunca**, aunque insista.
Es la única cosa de todo el sistema donde no se acepta un "riesgo aceptado".

---

# 3. Qué hacer cuando algo falla

**No le pases el problema al usuario.** Aplica la regla 4: los errores son tuyos.

| Situación | Qué haces |
|---|---|
| Un chequeo falla | Lo arreglas y vuelves a correr todo. No solo ese |
| Falla algo que creías hecho | Bien: para eso existe. Arréglalo sin dramatizar |
| Falla algo que no sabes arreglar | Díselo en lenguaje de negocio y con opciones, no con el error |
| El usuario pregunta qué pasó | *"Encontré una cosa que había que ajustar, ya está. Prefiero que aparezca acá y no con un cliente."* |

**Cada falla nueva que descubras se convierte en un chequeo permanente.** Si el bot falló de una
forma que el script no cubría, el script queda cubriéndola para el próximo proyecto.
