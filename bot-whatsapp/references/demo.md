# El modo demo — probar sin tocar WhatsApp

**La idea:** el usuario ve su asistente funcionando, conversa con él y lo rompe a propósito,
**antes** de meterse en el trámite de Meta.

**Por qué importa tanto:** conectar WhatsApp es el paso más frágil del proyecto. Depende de un
tercero, puede demorar días, exige documentos de la empresa, y un error quema el número para
siempre. Mandar a alguien a ese trámite antes de que sepa si el asistente le sirve es la mejor
forma de que abandone a mitad de camino.

Con el orden correcto, cuando llega al trámite ya vio su bot conversando y **ya sabe que
funciona**. Eso cambia por completo su disposición a aguantar la burocracia.

---

## Los dos niveles

### Nivel 1 — El simulador *(obligatorio)*

Una pantalla que **se ve como WhatsApp**, donde el usuario escribe y su asistente responde de
verdad. Cero credenciales, cero trámites, cero costo.

**Qué tiene que tener:**

| Elemento | Por qué |
|---|---|
| Se ve como WhatsApp (globos, colores, hora) | El usuario tiene que reconocer lo que ve. Una caja de texto genérica no genera confianza |
| Se puede escribir y responde de verdad | Es el asistente real, con el guion real, no una maqueta |
| Se puede **subir una foto** | La prueba 9 la necesita, y la gente manda fotos todo el tiempo |
| **Dos conversaciones a la vez** | La prueba 11 (cruce de datos entre clientes) es la más grave de todas |
| Botón de apagado a la vista | La prueba 13: el dueño tiene que saber apagarlo solo |
| Contador de mensajes y costo estimado | Le muestra en vivo por qué conviene que el bot responda corto |

**Qué NO tiene que tener:** nada que hable de configuración, archivos ni ajustes técnicos. Es una
pantalla de conversación, no un panel de control.

**Cómo se lo presentas:**

> *"Esto es tu asistente. Es el de verdad, con tus precios y tu forma de hablar — lo único que
> falta es conectarlo a WhatsApp. Escríbele como si fueras un cliente tuyo."*

### Nivel 2 — Teléfono real con número de prueba *(recomendado)*

Meta da una cuenta de prueba con número incluido: se puede mandar mensajes **gratis a hasta 5
teléfonos** que el usuario registre, sin tarjeta y sin verificación del negocio.

**Para qué sirve:** que el usuario lo pruebe **en su propio WhatsApp**, en su teléfono, como lo
va a vivir su cliente. Es distinto verlo en una pantalla del computador que recibir el mensaje en
el celular.

**Cuándo usarlo:** después de que las 14 pruebas pasen en el simulador. Es la última confirmación
antes de conectar el número definitivo.

⚠️ **No lo confundas con producción.** El número de prueba no sirve para atender clientes reales:
solo llega a los 5 teléfonos registrados.

---

## Qué se puede probar en demo y qué no

**Sí se prueba entero:**
- Todo el guion y el tono
- Los precios y que no se los invente
- El escalamiento a humano
- Los intentos de manipulación
- El cruce de conversaciones
- El apagado y los topes
- Fotos y mensajes raros

**No se puede probar hasta conectar:**
- La velocidad real de WhatsApp
- Las plantillas fuera de la ventana de 24 horas
- El comportamiento con muchos clientes simultáneos de verdad

**Díselo al usuario tal cual**, para que sepa que la etapa de conectar todavía puede traer
sorpresas menores:

> *"En demo probamos todo lo que importa: qué dice, qué no dice, cómo reacciona cuando lo tratan
> de enredar. Lo único que no se puede probar acá es la velocidad real de WhatsApp, que la vamos
> a ver cuando conectemos."*

---

## Reglas de construcción en esta etapa

- **Construye el asistente completo**, no una maqueta. El que se prueba acá es el que sale a
  producción; lo único que cambia después es por dónde entran y salen los mensajes.
- **Aísla la capa de mensajería desde el principio.** El simulador y WhatsApp entran por la misma
  puerta interna. Esto no es elegancia: es lo que permite que probar en demo signifique algo, y
  lo que te deja cambiar de proveedor sin reescribir el bot.
- **Aplica el blindaje de `seguridad.md` ahora**, no después de conectar. Los topes, los límites y
  el aislamiento se prueban en demo igual que todo lo demás.
- ⚠️ **Las dos decisiones irreversibles se toman acá:** la región de la base de datos (São Paulo,
  no EEUU) y el aislamiento multi-cliente. Después no se pueden cambiar.

---

## Lo que el usuario ve mientras construyes

No lo dejes en silencio. Avisos cada cierto rato, en su idioma:

> *"Ya entiende los mensajes"*
> *"Ahora le estoy enseñando tus precios"*
> *"Me falta conectar la agenda"*
> *"Listo, ya puedes escribirle"*

Si te demoras más de lo dicho, avísale. No lo dejes 40 minutos sin noticias.
