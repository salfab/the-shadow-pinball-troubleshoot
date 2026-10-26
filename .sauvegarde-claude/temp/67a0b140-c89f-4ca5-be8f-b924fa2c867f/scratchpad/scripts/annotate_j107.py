import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
k = im.size[0] / 1506  # coordinates below are in 1506-px-wide display units
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(34 * k))
small = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(28 * k))
RED, BLUE, YEL = (230, 0, 0), (0, 80, 230), (255, 210, 0)
W = int(5 * k)


def s(*v):
    return [int(x * k) for x in v]


def label(x, y, text, color, f=font, bg=(255, 255, 255)):
    x, y = int(x * k), int(y * k)
    l, t, r, b = d.textbbox((x, y), text, font=f)
    pad = int(5 * k)
    d.rectangle([l - pad, t - pad, r + pad, b + pad], fill=bg, outline=color, width=int(2 * k))
    d.text((x, y), text, font=f, fill=color)


# J107 plug positions 1..6
for i, x in enumerate([791, 874, 948, 1028, 1097, 1188], start=1):
    label(x - 10, 1018, str(i), RED, small)
label(560, 1060, "J107 : positions 1 à 6", RED, small)

# F104 / F105 top clips
d.rectangle(s(785, 1085, 945, 1245), outline=YEL, width=W)
d.rectangle(s(1005, 1105, 1185, 1255), outline=YEL, width=W)
label(700, 1265, "F104 : clip du haut", YEL, small, bg=(0, 0, 0))
label(1000, 1290, "F105 : clip du haut", YEL, small, bg=(0, 0, 0))

# Fuse names along the bottom of the holders
for name, x in [("F101", 170), ("F102", 380), ("F103", 600), ("F104", 830), ("F105", 1050)]:
    label(x, 1700, name, BLUE, small)

im.save(dst, quality=90)
print(dst, im.size)
