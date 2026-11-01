"""Annotate J124/J125 (insert flashers, to unplug), J106 (backbox +20 V, keep plugged) and TP7 on the rotated layout (x2 coords)."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
RED, GREEN = (220, 0, 0), (0, 140, 60)


def label(x, y, text, color):
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=font, fill=color)


d.rectangle([984, 1690, 1094, 1748], outline=RED, width=5)
d.rectangle([1164, 1690, 1356, 1748], outline=RED, width=5)
label(820, 1600, "J124 et J125 : flashers de la tête (fiches à débrancher)", RED)
d.line([1040, 1690, 1040, 1636], fill=RED, width=3)
d.line([1260, 1690, 1260, 1636], fill=RED, width=3)
d.rectangle([1293, 465, 1405, 520], outline=GREEN, width=5)
label(1180, 400, "J106 : +20 V de la tête (laisser branché)", GREEN)
d.ellipse([1437, 1000, 1481, 1044], outline=RED, width=5)
label(1500, 1000, "TP7 (+20 V) : pointe noire", RED)

im.crop((780, 380, 2000, 1780)).save(out)
print("ok")
