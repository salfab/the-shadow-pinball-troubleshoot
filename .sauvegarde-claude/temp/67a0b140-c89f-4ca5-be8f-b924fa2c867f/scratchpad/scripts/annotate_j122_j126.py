"""Annotate the rotated layout (x2 image, 2792x2168) with J122, J126 and F104's bottom clip."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_full, out_zoom = sys.argv[1], sys.argv[2], sys.argv[3]
im = Image.open(src).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
small = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
RED, BLUE, GREEN = (220, 0, 0), (0, 80, 220), (0, 140, 60)


def label(x, y, text, color, f=font):
    l, t, r, b = d.textbbox((x, y), text, font=f)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=f, fill=color)


def mark(x, y, text, color, lx, ly):
    d.ellipse([x - 12, y - 12, x + 12, y + 12], outline=color, width=4)
    d.line([x, y + 12, lx + 20, ly - 6], fill=color, width=3)
    label(lx, ly, text, color, small)


# J122 (outer row, 9 positions: 9 at left, 1 at right, key at 7)
d.rectangle([818, 1790, 1020, 1862], outline=BLUE, width=5)
label(940, 1866, "J122", BLUE)
mark(918, 1825, "5 = tieback", RED, 700, 1920)
mark(998, 1825, "1 = Sol 25 (Bleu-Marron)", RED, 930, 1965)
# J126 (outer row, 13 positions: 13 at left, 1 at right, key at 9)
d.rectangle([1104, 1790, 1388, 1862], outline=BLUE, width=5)
label(1300, 1866, "J126", BLUE)
mark(1162, 1825, "11 = tieback", RED, 1140, 1920)
mark(1222, 1825, "8 = Sol 24 (Bleu-Gris)", RED, 1290, 1965)
# F104 bottom clip
d.rectangle([1264, 820, 1336, 870], outline=GREEN, width=5)
label(1360, 860, "pointe noire : clip du BAS de F104 (50 V, comme TP6)", GREEN, small)
label(300, 270, "Power Driver vue comme dans le fronton (J130 en bas)", (0, 0, 0))

im.save(out_full)
im.crop((600, 1600, 1900, 2050)).save(out_zoom)
print("ok")
