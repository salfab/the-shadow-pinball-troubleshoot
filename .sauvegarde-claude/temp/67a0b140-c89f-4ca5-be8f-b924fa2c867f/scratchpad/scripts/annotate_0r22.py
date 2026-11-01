"""Mark the eight blue 0.22 ohm row sense resistors on the session-1 lamp-driver photo (original pixel coords)."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

src, out = sys.argv[1], sys.argv[2]
im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
d = ImageDraw.Draw(im)
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 50)
ORANGE = (255, 120, 0)

pairs = [(2340, 1585, 2505, 1810), (2340, 1900, 2505, 2180), (3085, 1605, 3260, 1830), (3075, 1995, 3250, 2220)]
for box in pairs:
    d.rectangle(box, outline=ORANGE, width=9)
text = "Résistances 0,22 Ω des rangées (R150–R153, R172–R175)"
x, y = 2290, 1345
l, t, r, b = d.textbbox((x, y), text, font=font)
d.rectangle([l - 10, t - 8, r + 10, b + 8], fill=(255, 255, 255), outline=ORANGE, width=6)
d.text((x, y), text, font=font, fill=ORANGE)
for x0, y0, x1, _ in []:
    d.line([(x0 + x1) // 2, b + 8, (x0 + x1) // 2, y0], fill=ORANGE, width=5)

im.crop((2200, 1300, 4000, 2330)).save(out, quality=90)
print("ok")
