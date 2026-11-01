"""Rebuild The Shadow manual as a PDF from the Planetary Pinball flipbook (full-page mobile images)."""
import sys, urllib.request
import fitz

BASE = "https://www.planetarypinball.com/reference/gamemanuals/The_Shadow_Bly/files/assets/mobile/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
out, count = sys.argv[1], int(sys.argv[2])


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


doc, missing = fitz.open(), []
for n in range(1, count + 1):
    data = None
    for name in (f"page{n:04d}_i2.png", f"page{n:04d}_i2.jpg", f"page{n:04d}_i1.jpg", f"page{n:04d}_i1.png"):
        try:
            data = get(BASE + name)
            break
        except Exception:
            pass
    if data is None:
        missing.append(n)
        continue
    pix = fitz.Pixmap(data)
    page = doc.new_page(width=612, height=612 * pix.height / pix.width)
    page.insert_image(page.rect, stream=data)
doc.save(out, deflate=True)
print(f"{doc.page_count} pages sur {count} ; manquantes : {missing}")
