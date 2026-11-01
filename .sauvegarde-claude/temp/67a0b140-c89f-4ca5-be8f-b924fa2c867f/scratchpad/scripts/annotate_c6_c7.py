"""Annotate C6/C7 (+18 V lamp column filter caps) and the J138 header, to explain the L1 first attempt."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_zoom = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
ORANGE, BLUE = (230, 110, 0), (0, 80, 220)


def label(x, y, text, color):
    l, t, r, b = d.textbbox((x, y), text, font=font)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=font, fill=color)


# C7 and C6 (x2 coords), 15 000 uF each on the +18 V lamp column supply
d.ellipse([1932, 973, 2108, 1149], outline=ORANGE, width=6)
d.ellipse([2120, 973, 2296, 1149], outline=ORANGE, width=6)
label(1650, 895, "C7, C6 : +18 V des colonnes (2 × 15 000 µF)", ORANGE)
d.line([2020, 930, 2020, 973], fill=ORANGE, width=3)
d.line([2208, 930, 2208, 973], fill=ORANGE, width=3)
# J138 header on the board (not the harness plug)
d.rectangle([2135, 1793, 2332, 1862], outline=BLUE, width=5)
label(1700, 1895, "J138 : broches de l'embase (côté carte)", BLUE)
d.line([2233, 1862, 2233, 1893], fill=BLUE, width=3)

im.crop((1600, 860, 2420, 1960)).save(out_zoom)
print("ok")
