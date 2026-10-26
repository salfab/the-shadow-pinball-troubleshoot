import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
k = im.size[0] / 2000  # coordinates in 2000-px-wide display units
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(32 * k))
RED, GREEN = (230, 0, 0), (0, 150, 60)
W = int(5 * k)


def s(*v):
    return [int(x * k) for x in v]


def label(x, y, text, color):
    x, y = int(x * k), int(y * k)
    l, t, r, b = d.textbbox((x, y), text, font=font)
    pad = int(6 * k)
    d.rectangle([l - pad, t - pad, r + pad, b + pad], fill=(255, 255, 255), outline=color, width=int(3 * k))
    d.text((x, y), text, font=font, fill=color)


d.rectangle(s(462, 1082, 778, 1238), outline=RED, width=W)
label(430, 1000, "J127 (fils marron) : Sol 9 à 16 — à débrancher", RED)
d.rectangle(s(858, 1105, 1125, 1195), outline=GREEN, width=W)
label(870, 1205, "J130 (déjà débranché)", GREEN)

im.save(dst, quality=90)
print(dst)
