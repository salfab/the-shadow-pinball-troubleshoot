"""Annotate the rotated layout (x2 image) with TP7 (+20 V), TP5 (ground) and C11 (20 V filter cap)."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_full, out_zoom = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
RED, BLACK, BLUE = (220, 0, 0), (0, 0, 0), (0, 80, 220)


def label(x, y, text, color):
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=font, fill=color)


# TP7 (+20 V) and TP5 (ground), one above the other between U4 and U5 (x2 coords)
d.ellipse([1437, 1000, 1481, 1044], outline=RED, width=5)
label(1600, 950, "TP7 (+20 V) : pointe rouge", RED)
d.line([1481, 1015, 1600, 965], fill=RED, width=3)
d.ellipse([1436, 1042, 1480, 1086], outline=BLACK, width=5)
label(1600, 1085, "TP5 (masse) : pointe noire", BLACK)
d.line([1480, 1072, 1600, 1100], fill=BLACK, width=3)
# C11, 15 000 uF filter cap of the 20 V supply
d.ellipse([1742, 462, 1918, 638], outline=BLUE, width=6)
label(1560, 385, "C11 : 15 000 µF (filtre du +20 V)", BLUE)
d.line([1790, 420, 1800, 470], fill=BLUE, width=3)

im.save(out_full)
im.crop((1250, 340, 2150, 1160)).save(out_zoom)
print("ok")
