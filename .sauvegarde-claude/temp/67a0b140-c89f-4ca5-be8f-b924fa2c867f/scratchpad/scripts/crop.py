import sys, fitz
# usage: crop.py pdf page(1-based) x0 y0 x1 y1 (fractions 0..1) zoom out.png
pdf, page, x0, y0, x1, y1, zoom, out = sys.argv[1], int(sys.argv[2]), *map(float, sys.argv[3:8]), sys.argv[8]
doc = fitz.open(pdf)
p = doc[page-1]
r = p.rect
clip = fitz.Rect(r.x0 + x0*r.width, r.y0 + y0*r.height, r.x0 + x1*r.width, r.y0 + y1*r.height)
pix = p.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip)
pix.save(out)
print(out, pix.width, pix.height, "page rect", r)
