"""Annotate the rotated layout (x2 image) with F103/F104/F105 top clips and TP7 for M13."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_full, out_zoom = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
RED, BLUE, GREEN = (220, 0, 0), (0, 80, 220), (0, 140, 60)


def label(x, y, text, color):
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=font, fill=color)


# fuse top clips (x2 coords): F103 1196-1260, F104 1264-1336, F105 1336-1408 ; y 672-720
for name, x0, x1, ly in [("A = F103 haut", 1196, 1262, 560), ("B = F104 haut", 1264, 1336, 605), ("C = F105 haut", 1336, 1408, 650)]:
    d.rectangle([x0, 672, x1, 722], outline=RED, width=5)
    label(1450, ly, name, RED)
    d.line([x1, 690, 1450, ly + 14], fill=RED, width=3)
label(980, 900, "F103 : à retirer", BLUE)
d.line([1228, 868, 1150, 900], fill=BLUE, width=3)
# TP7 (20 V)
d.ellipse([1440, 998, 1480, 1038], outline=GREEN, width=5)
label(1500, 1000, "TP7 (+20 V flashers)", GREEN)

im.save(out_full)
im.crop((900, 480, 2000, 1120)).save(out_zoom)
print("ok")
