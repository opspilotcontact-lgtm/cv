# -*- coding: utf-8 -*-
"""Procesa el retrato: recorta a retrato, mejora calidad y aplica duotono slate/verde."""
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import base64, io, sys

SRC = "WhatsApp Image 2026-06-02 at 20.15.39.jpeg"
OUT = "foto_cv.jpg"

# crop fractions (tuneables) — encuadre retrato cabeza+hombros
LX, RX = 0.175, 0.815   # horizontal
TY, BY = 0.150, 0.815   # vertical

# duotono: sombras -> slate (se funden con el header), luces -> verde-blanco sutil
SHADOW = (23, 23, 44)
MID    = (84, 100, 92)
HIGHL  = (231, 237, 225)

img = Image.open(SRC).convert("RGB")
W, H = img.size
print("origen:", W, "x", H)

box = (int(W*LX), int(H*TY), int(W*RX), int(H*BY))
img = img.crop(box)
print("recorte:", img.size)

# escala de grises con buena luminancia + autocontraste (mejora calidad/rango)
g = ImageOps.grayscale(img)
g = ImageOps.autocontrast(g, cutoff=1)

# --- retoque suave de ojeras (aclarar zona bajo los ojos) ---
from PIL import ImageDraw
cw, ch = g.size
# centros y radios de las dos elipses bajo los ojos (fracciones del recorte)
EYES = [
    (0.375, 0.455, 0.085, 0.052),   # ojo izquierdo (en imagen)
    (0.625, 0.452, 0.085, 0.052),   # ojo derecho
]
LIFT = 42  # cuanto se aclara (0-255)
mask = Image.new("L", (cw, ch), 0)
md = ImageDraw.Draw(mask)
for fx, fy, frx, fry in EYES:
    x, y = fx*cw, fy*ch
    rx, ry = frx*cw, fry*ch
    md.ellipse([x-rx, y-ry, x+rx, y+ry], fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(radius=int(cw*0.035)))
brightened = g.point(lambda p: min(255, int(p + LIFT)))
g = Image.composite(brightened, g, mask)

# nitidez (la foto es de un papel, conviene realzar bordes con cuidado)
g = g.filter(ImageFilter.UnsharpMask(radius=2.2, percent=120, threshold=3))
g = ImageEnhance.Contrast(g).enhance(1.06)

# duotono (tritono real: black/mid/white)
duo = ImageOps.colorize(g, black=SHADOW, mid=MID, white=HIGHL,
                        blackpoint=0, whitepoint=255, midpoint=128).convert("RGB")

# reescalado limpio para retina (ancho objetivo ~520px en pantalla ~170px)
target_w = 560
ratio = target_w / duo.width
duo = duo.resize((target_w, int(duo.height*ratio)), Image.LANCZOS)
print("salida:", duo.size)

duo.save(OUT, "JPEG", quality=88, optimize=True, progressive=True)

# base64 para incrustar (CV portable)
buf = io.BytesIO()
duo.save(buf, "JPEG", quality=86, optimize=True, progressive=True)
b64 = base64.b64encode(buf.getvalue()).decode()
with open("foto_b64.txt", "w") as f:
    f.write("data:image/jpeg;base64," + b64)
print("base64 bytes:", len(b64))
