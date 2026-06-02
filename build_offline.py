# -*- coding: utf-8 -*-
"""Genera una version 100% offline del CV: GSAP y fuentes embebidos en el HTML."""
import urllib.request, re, base64

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
SRC = "cv_juan_ortiz.html"
OUT = "cv_juan_ortiz_offline.html"

CSS_URL = ("https://fonts.googleapis.com/css2?"
           "family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700"
           "&family=JetBrains+Mono:wght@400;500;700"
           "&family=Manrope:wght@400;500;600;700;800&display=swap")
GSAP = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"
SCRT = "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"

def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read() if binary else r.read().decode("utf-8")

print("Descargando CSS de Google Fonts...")
css = fetch(CSS_URL)

# capturar bloques: /* subset */ @font-face { ... }
blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
print("  bloques totales:", len(blocks))

font_css = []
embedded = 0
for subset, block in blocks:
    if subset != "latin":           # solo latino (cubre acentos y ñ del espanol)
        continue
    m = re.search(r"url\((https://[^)]+\.woff2)\)", block)
    if not m:
        continue
    woff2 = fetch(m.group(1), binary=True)
    b64 = base64.b64encode(woff2).decode()
    datauri = "url(data:font/woff2;base64,%s) format('woff2')" % b64
    block = block[:m.start()] + datauri + block[m.end():]
    # quitar el resto del src si quedara (solo dejamos el woff2)
    font_css.append(block.strip())
    embedded += 1
print("  fuentes latinas embebidas:", embedded)

print("Descargando GSAP...")
gsap_js = fetch(GSAP)
print("Descargando ScrollTrigger...")
st_js = fetch(SCRT)

with open(SRC, encoding="utf-8") as f:
    html = f.read()

# 1) reemplazar <link> de Google Fonts por <style> con @font-face embebidos
link_re = re.compile(r'<link[^>]+fonts\.googleapis\.com/css2[^>]*>')
font_style = "<style>\n" + "\n".join(font_css) + "\n</style>"
html, n1 = link_re.subn(font_style, html)

# quitar preconnect (ya no hacen falta)
html = re.sub(r'\s*<link rel="preconnect"[^>]*>', "", html)

# 2) reemplazar los <script src=...gsap...> por scripts inline (reemplazo literal)
def safe(js):  # evitar que un </script> dentro del JS rompa el documento
    return js.replace("</script>", "<\\/script>")

tag_gsap = '<script src="' + GSAP + '"></script>'
tag_scrt = '<script src="' + SCRT + '"></script>'
n2 = 1 if tag_gsap in html else 0
n3 = 1 if tag_scrt in html else 0
html = html.replace(tag_gsap, "<script>" + safe(gsap_js) + "</script>")
html = html.replace(tag_scrt, "<script>" + safe(st_js) + "</script>")

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("Reemplazos -> fonts-link:%d gsap:%d scrolltrigger:%d" % (n1, n2, n3))
print("Generado %s (%d KB)" % (OUT, round(len(html.encode('utf-8'))/1024)))
