#!/usr/bin/env python3
"""
Verificación estructural del sistema bot-whatsapp.

Revisa que el sistema sea internamente consistente: que las referencias apunten
a archivos que existen, que la cadena de etapas esté completa, y sobre todo que
los números declarados en la documentación coincidan con los reales.

Ese último chequeo es el que más rinde. Si agregas un control de seguridad, el
blindaje pasa de 53 a 54 — y hay seis archivos que declaran ese número. A mano
no se ve; acá sí.

    python verificar.py

Sale con código 1 si hay fallas. No verifica la experiencia de uso, solo la
estructura: que la conversación fluya con una persona real solo se sabe
corriéndola.
"""
import io
import os
import re
import glob
import sys

RAIZ = os.path.dirname(os.path.abspath(__file__))
os.chdir(RAIZ)

# La bandeja es la única etapa que no se cierra: se usa a diario mientras el
# asistente está en modo borrador. Por eso no tiene gate.
SIN_GATE = {"bot-whatsapp", "bot-bandeja"}

# Frases que contienen un número seguido de una palabra clave, pero que se
# refieren a otra cosa. Sin esto el chequeo de conteos reporta ruido.
EXCEPCIONES = [
    "3 preguntas de la rutina",   # las de la revisión diaria, no las del descubrimiento
]

fallas, avisos = [], []


def leer(p):
    return io.open(p, encoding="utf-8").read()


def limpiar(s):
    for e in EXCEPCIONES:
        s = s.replace(e, "")
    return s


CMDS = sorted(d for d in os.listdir(".")
              if d.startswith("bot-") and os.path.isdir(d))
REFS = sorted(os.path.basename(p)
              for p in glob.glob("bot-whatsapp/references/*.md"))
DOCS = glob.glob("bot-*/SKILL.md") + glob.glob("bot-whatsapp/references/*.md")

print("=" * 68)
print("VERIFICACION DEL SISTEMA bot-whatsapp")
print("=" * 68)
print("Comandos: %d   Referencias: %d" % (len(CMDS), len(REFS)))

# --------------------------------------------------------------- 1
print("\n[1] Frontmatter de cada comando")
for d in CMDS:
    p = os.path.join(d, "SKILL.md")
    s = leer(p)
    if not s.startswith("---"):
        fallas.append("%s: sin frontmatter" % p)
        continue
    m = re.search(r"^name:\s*(\S+)", s, re.M)
    if not m:
        fallas.append("%s: sin name" % p)
    elif m.group(1) != d:
        fallas.append("%s: name '%s' no coincide con la carpeta" % (p, m.group(1)))
    if not re.search(r"^description:", s, re.M):
        fallas.append("%s: sin description" % p)
print("    revisados: %d" % len(CMDS))

# --------------------------------------------------------------- 2
print("\n[2] Referencias a archivos")
rotas = 0
for p in DOCS:
    s = leer(p)
    citadas = set(re.findall(r"references/([a-z-]+\.md)", s))
    citadas |= set(re.findall(r"`([a-z-]+\.md)`", s))
    for ref in citadas:
        if ref not in REFS:
            fallas.append("%s cita %s (no existe)" % (p, ref))
            rotas += 1
print("    rotas: %d" % rotas)

# --------------------------------------------------------------- 3
print("\n[3] Comandos citados")
validos = {"/" + c for c in CMDS}
malos = 0
for p in DOCS + ["README.md"]:
    for c in set(re.findall(r"(/bot-[a-z]+)", leer(p))):
        if c not in validos:
            fallas.append("%s cita %s (no existe)" % (p, c))
            malos += 1
print("    inexistentes: %d" % malos)

# --------------------------------------------------------------- 4
print("\n[4] Todos cargan las reglas de oro")
for d in CMDS:
    if "reglas.md" not in leer(os.path.join(d, "SKILL.md")):
        fallas.append("%s no carga reglas.md" % d)
print("    revisados: %d" % len(CMDS))

# --------------------------------------------------------------- 5
print("\n[5] Cadena de etapas")
CADENA = ["bot-planificar", "bot-costos", "bot-probar", "bot-conectar",
          "bot-revisar", "bot-publicar", "bot-bandeja", "bot-soltar"]
for i, d in enumerate(CADENA[:-1]):
    sig = "/" + CADENA[i + 1]
    if sig not in leer(os.path.join(d, "SKILL.md")):
        fallas.append("%s no manda a %s" % (d, sig))
print("    eslabones: %d" % (len(CADENA) - 1))

# --------------------------------------------------------------- 6
print("\n[6] Gate por comando")
for d in CMDS:
    if d in SIN_GATE:
        continue
    if "gate" not in leer(os.path.join(d, "SKILL.md")).lower():
        avisos.append("%s sin gate explicito" % d)
print("    revisados: %d" % (len(CMDS) - len(SIN_GATE)))

# --------------------------------------------------------------- 7
print("\n[7] Bloque 'Si algo no aparece'")
faltan = [d for d in CMDS
          if "## Si algo no aparece" not in leer(os.path.join(d, "SKILL.md"))]
for d in faltan:
    fallas.append("%s sin bloque de recuperacion" % d)
print("    con bloque: %d/%d" % (len(CMDS) - len(faltan), len(CMDS)))

# --------------------------------------------------------------- 8
print("\n[8] Numeros declarados vs reales")
reales = {
    "pruebas": len(re.findall(r"^### Prueba \d", leer("bot-whatsapp/references/pruebas.md"), re.M)),
    "preguntas": len(re.findall(r"^### \d+\.", leer("bot-whatsapp/references/descubrimiento.md"), re.M)),
    "blindaje": len(re.findall(r"^- \[ \]", leer("bot-whatsapp/references/seguridad.md").split("# PARTE B")[1], re.M)),
    "chequeos": len(re.findall(r"^\d+\. \*\*", leer("bot-whatsapp/references/verificacion.md"), re.M)),
}
print("    reales -> %s" % reales)

PATRONES = {
    "pruebas": r"(\d+) pruebas",
    "preguntas": r"(\d+) preguntas",
    "blindaje": r"(\d+) [ií]tems|(\d+) controles",
    "chequeos": r"(\d+) chequeos",
}
declarados = {}
for p in DOCS + ["README.md"]:
    s = limpiar(leer(p))
    for clave, pat in PATRONES.items():
        for m in re.findall(pat, s):
            n = m if isinstance(m, str) else next(x for x in m if x)
            declarados.setdefault((clave, n), []).append(p)

for (clave, n), archivos in sorted(declarados.items()):
    if int(n) != reales[clave]:
        fallas.append("dice '%s %s' pero hay %d -> %s"
                      % (n, clave, reales[clave], ", ".join(sorted(set(archivos)))))

# --------------------------------------------------------------- 9
print("\n[9] Referencias que nadie carga")
todo = "".join(leer(p) for p in DOCS)
for r in REFS:
    if todo.count(r) <= 1:
        avisos.append("%s casi no se referencia" % r)
print("    revisadas: %d" % len(REFS))

# --------------------------------------------------------------- 10
print("\n[10] Instalado vs repositorio")
skills = os.path.join(os.path.expanduser("~"), ".claude", "skills")
if not os.path.isdir(skills):
    print("    sin instalar (se omite)")
else:
    desinc = 0
    for d in CMDS:
        for p in glob.glob(os.path.join(d, "**", "*.md"), recursive=True):
            inst = os.path.join(skills, p)
            if not os.path.exists(inst):
                fallas.append("no instalado: %s" % p)
                desinc += 1
            elif leer(inst) != leer(p):
                fallas.append("desincronizado: %s" % p)
                desinc += 1
    print("    desincronizados: %d" % desinc)

# ---------------------------------------------------------------
print("\n" + "=" * 68)
if fallas:
    print("FALLAS (%d)" % len(fallas))
    for f in fallas:
        print("  X  " + f)
else:
    print("SIN FALLAS")
if avisos:
    print("\nAVISOS (%d)" % len(avisos))
    for a in avisos:
        print("  !  " + a)
print("=" * 68)

sys.exit(1 if fallas else 0)
