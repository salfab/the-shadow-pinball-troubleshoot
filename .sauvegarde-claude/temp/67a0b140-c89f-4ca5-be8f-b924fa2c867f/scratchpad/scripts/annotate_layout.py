"""Annotate the A-12697-3 layout drawing, rotated to the mounted orientation (J130 at the bottom).

usage: annotate_layout.py layout.jpg out_full.png out_zoom.png
Coordinates below are in the rotated drawing (1396 x 1084 px) before upscaling.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_full, out_zoom = sys.argv[1], sys.argv[2], sys.argv[3]
S = 2  # upscale factor for readability
im = Image.open(src).convert("RGB").rotate(-90, expand=True)
im = im.resize((im.size[0] * S, im.size[1] * S), Image.LANCZOS)
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 24 * S // 2)
small = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 19 * S // 2)
RED, BLUE, GREEN = (220, 0, 0), (0, 90, 220), (0, 150, 60)
W = 3 * S


def s(*v):
    return [int(x * S) for x in v]


def label(x, y, text, color, f=font):
    x, y = int(x * S), int(y * S)
    l, t, r, b = d.textbbox((x, y), text, font=f)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=2)
    d.text((x, y), text, font=f, fill=color)


# F104 and F105 (vertical fuses, side by side)
d.rectangle(s(632, 336, 668, 434), outline=RED, width=W)
d.rectangle(s(668, 336, 704, 434), outline=RED, width=W)
label(598, 446, "F104", RED)
d.line(s(625, 446, 640, 434), fill=RED, width=W)
label(676, 446, "F105", RED)
# clip sides
d.line(s(704, 345, 760, 345), fill=RED, width=W)
label(762, 333, "clip du HAUT = côté bobines", RED, small)
d.line(s(704, 425, 760, 470), fill=RED, width=W)
label(762, 462, "clip du BAS = côté 50 V (TP6)", RED, small)

# J107 with pin numbers
d.rectangle(s(633, 286, 697, 322), outline=RED, width=W)
label(470, 175, "J107 : broches 1 à 6 de gauche à droite, détrompeur en 4", RED, small)
d.line(s(640, 192, 655, 286), fill=RED, width=W)
for i, x in enumerate([641, 651, 661, 671, 681, 691], start=1):
    d.text((x * S - 4, 326 * S), str(i), font=small, fill=RED)

# TP6
d.ellipse(s(860, 412, 890, 442), outline=BLUE, width=W)
label(895, 405, "TP6 (+50 V)", BLUE, small)

# J130 for orientation
d.rectangle(s(826, 842, 920, 872), outline=GREEN, width=W)
label(800, 890, "J130 (débranché)", GREEN, small)

label(150, 140, "Power Driver vue comme dans le fronton (J130 en bas)", (0, 0, 0))

im.save(out_full)
im.crop(s(380, 120, 1100, 560)).save(out_zoom)
print(out_full, im.size)
