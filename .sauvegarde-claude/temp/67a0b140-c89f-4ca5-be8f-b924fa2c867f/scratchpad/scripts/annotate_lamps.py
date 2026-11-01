"""Annotate the lamp connectors J133-J138 and TP5 for the lamp matrix checks (L1/L2)."""
import sys
from PIL import Image, ImageDraw, ImageFont

src, out_full, out_zoom = sys.argv[1], sys.argv[2], sys.argv[3]
font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 26)
small = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 22)
RED, BLUE, BLACK, GREEN, GREY = (220, 0, 0), (0, 80, 220), (0, 0, 0), (0, 140, 60), (110, 110, 110)


def label(d, x, y, text, color, f=font):
    l, t, r, b = d.textbbox((x, y), text, font=f)
    d.rectangle([l - 6, t - 4, r + 6, b + 4], fill=(255, 255, 255), outline=color, width=3)
    d.text((x, y), text, font=f, fill=color)


base = Image.open(src).convert("RGB")

# Full board (x2 coords): J135 (rows), J138 (columns), TP5 (ground)
im = base.copy()
d = ImageDraw.Draw(im)
d.rectangle([1933, 1815, 2070, 1862], outline=RED, width=5)
label(d, 1500, 1935, "J135 : rangées (fiche à débrancher)", RED)
d.line([1990, 1862, 1900, 1932], fill=RED, width=3)
d.rectangle([2135, 1793, 2332, 1862], outline=BLUE, width=5)
label(d, 1900, 2000, "J138 : colonnes (fiche à débrancher)", BLUE)
d.line([2230, 1862, 2230, 1997], fill=BLUE, width=3)
d.ellipse([1436, 1042, 1480, 1086], outline=BLACK, width=5)
label(d, 1150, 1110, "TP5 (masse) : pointe noire", BLACK)
d.line([1446, 1084, 1420, 1108], fill=BLACK, width=3)
im.save(out_full)

# Zoom on J133-J138 (x2 again), with white margins for the labels
TOP, BOTTOM = 110, 230
z = base.crop((1880, 1650, 2360, 1900)).resize((960, 500))
zm = Image.new("RGB", (960, TOP + 500 + BOTTOM), "white")
zm.paste(z, (0, TOP))
d = ImageDraw.Draw(zm)


def box(x0, y0, x1, y1, color, w=5):
    d.rectangle([x0, y0 + TOP, x1, y1 + TOP], outline=color, width=w)


box(110, 75, 375, 150, GREY, 3)
box(510, 80, 905, 200, GREY, 3)
label(d, 20, 15, "J133 et J137 : vides sur The Shadow (ne rien y brancher)", GREY, small)
d.line([240, 48, 240, TOP + 75], fill=GREY, width=2)
d.line([700, 48, 700, TOP + 80], fill=GREY, width=2)
box(110, 210, 375, 285, GREEN, 3)
box(377, 288, 508, 420, GREEN, 3)
box(110, 333, 375, 420, RED)
box(510, 286, 905, 420, BLUE)
label(d, 20, TOP + 520, "J135 rangées : 1 à droite, 9 à gauche, détrompeur en 3", RED, small)
label(d, 20, TOP + 565, "J138 colonnes : 1 à droite, 9 à gauche, détrompeur en 8", BLUE, small)
label(d, 20, TOP + 610, "J134 et J136 (lampes de la caisse) : laisser branchées", GREEN, small)
zm.save(out_zoom)
print("ok")
