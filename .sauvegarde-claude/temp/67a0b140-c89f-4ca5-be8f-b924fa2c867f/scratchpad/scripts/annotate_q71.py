import sys
from PIL import Image, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
k = im.size[0] / 2000  # coordinates below are in 2000-px-wide display units
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", int(30 * k))


def box(x0, y0, x1, y1):
    return [int(v * k) for v in (x0, y0, x1, y1)]


def label(x, y, text, color):
    x, y = int(x * k), int(y * k)
    l, t, r, b = draw.textbbox((x, y), text, font=font)
    pad = int(6 * k)
    draw.rectangle([l - pad, t - pad, r + pad, b + pad], fill=(0, 0, 0))
    draw.text((x, y), text, font=font, fill=color)


yellow, red, cyan, orange = (255, 220, 0), (255, 40, 40), (0, 230, 255), (255, 150, 0)
w = int(4 * k)

# Cluster of the four 2N5401 pre-drivers of Sol 01-04 (Q71-Q74)
draw.rectangle(box(918, 228, 1048, 350), outline=yellow, width=w)
label(1060, 160, "Q71 à Q74 : 2N5401", yellow)
# Probable Q71 (upper-left of the cluster, by analogy with Q59-Q62)
draw.ellipse(box(925, 236, 977, 310), outline=red, width=w)
label(700, 180, "Q71 (probable)", red)
draw.line(box(880, 215, 930, 255), fill=red, width=w)

# TIP102 pre-drivers to compare, and the shorted output
draw.rectangle(box(985, 758, 1080, 815), outline=cyan, width=w)
label(1140, 760, "Q79 (TIP102, Sol 02)", cyan)
draw.rectangle(box(1020, 934, 1115, 1006), outline=cyan, width=w)
label(1140, 935, "Q81 (TIP102, Sol 01)", cyan)
draw.rectangle(box(1000, 1018, 1130, 1104), outline=orange, width=w)
label(1140, 1030, "Q82 (en court-circuit)", orange)

im = im.resize((2000, int(im.size[1] / k)))
im.save(dst, quality=90)
print(dst, im.size)
