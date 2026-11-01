"""Annotate the GI fuses F106-F110, TP5 and the GI connectors on the rotated layout (x2 coords)."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_zoom = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
ORANGE, BLACK, GREEN = (230, 110, 0), (0, 0, 0), (0, 140, 60)


def label(x, y, text, color):
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=font, fill=color)


# GI fuses (G1: red probe on one clip of each)
for box in [(377, 1452, 558, 1515), (377, 1533, 558, 1596), (377, 1608, 558, 1672),
            (593, 1533, 775, 1596), (593, 1608, 775, 1672)]:
    d.rectangle(box, outline=ORANGE, width=5)
label(600, 1415, "F106 à F110 : fusibles de la GI (pointe rouge)", ORANGE)
# TP5 (black probe)
d.ellipse([1436, 1042, 1480, 1086], outline=BLACK, width=5)
label(1060, 1110, "TP5 (masse) : pointe noire", BLACK)
d.line([1446, 1084, 1420, 1108], fill=BLACK, width=3)
# GI connectors (G2, visual check later)
for box in [(296, 1462, 334, 1722), (628, 1696, 852, 1748), (572, 1798, 803, 1852), (480, 1798, 547, 1852)]:
    d.rectangle(box, outline=GREEN, width=4)
label(270, 1880, "Connecteurs de la GI : J115 (transformateur), J120, J121, J119", GREEN)

im.crop((250, 1000, 1560, 1930)).save(out_zoom)
print("ok")
