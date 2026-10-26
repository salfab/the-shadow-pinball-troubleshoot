import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
k = im.size[0] / 1506  # coordinates in 1506-px-wide display units
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(40 * k))
small = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(30 * k))
RED, BLUE = (230, 0, 0), (0, 70, 220)
W = int(5 * k)


def label(x, y, text, color, f=font):
    x, y = int(x * k), int(y * k)
    l, t, r, b = d.textbbox((x, y), text, font=f)
    pad = int(6 * k)
    d.rectangle([l - pad, t - pad, r + pad, b + pad], fill=(255, 255, 255), outline=color, width=int(3 * k))
    d.text((x, y), text, font=f, fill=color)


# slot centres (left to right in the photo) -> position numbers
slots = [(486, "6"), (560, "5"), (641, "4"), (726, "3"), (822, "2"), (915, "1")]
for x, n in slots:
    color = RED if n in ("2", "3") else BLUE
    label(x - 14, 1545, n, color)

legend = [
    ("Fiche J107 du faisceau (débranchée), vue côté fils", BLUE),
    ("2 = Rouge-Marron (F104) : pointe ici pour la 1re colonne", RED),
    ("3 = Rouge-Noir (F105) : pointe ici pour la 2e colonne", RED),
    ("1 = Rouge-Orange (F103)   6 = Rouge-Blanc (20 V)   4, 5 = vides", BLUE),
]
y = 1640
for text, color in legend:
    label(60, y, text, color, small)
    y += 70

im.save(dst, quality=90)
print(dst)
