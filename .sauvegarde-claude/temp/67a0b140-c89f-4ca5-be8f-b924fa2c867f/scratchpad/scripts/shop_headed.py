"""Headed browser walk through Distrelec and Mouser searches; the user solves any CAPTCHA by hand.
Saves, per query, the page text and the product links found, to out_headed/results.json."""
import json, sys, time, urllib.parse
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
QUERIES = {
    "TIP36C": "TIP36C", "TIP102": "TIP102", "TIP107": "TIP107", "2N5401": "2N5401", "1N4004": "1N4004",
    "R68_05W": "68 ohm 0.5W axial resistor", "R220_025W": "220 ohm 0.25W axial resistor",
    "R2k7_025W": "2.7k 0.25W axial resistor", "R0R22_1W": "0.22 ohm 1W axial resistor",
    "F5A_6x32": "6.3x32 5A time lag fuse", "F3A_6x32": "6.3x32 3A time lag fuse",
    "flux": "no clean flux pen", "tresse": "desoldering braid 2.5mm", "soudure": "Sn60Pb40 solder 0.8mm",
    "906": "906 wedge bulb",
}
SITES = {
    "distrelec": ("https://www.distrelec.ch/fr/search?q={}", "/p/"),
    "mouser": ("https://www.mouser.ch/c/?q={}", "/ProductDetail/"),
}
BLOCK_WORDS = ("captcha", "radware", "access denied", "validate", "are you a human", "verify you are")


def blocked(page):
    try:
        txt = (page.title() + " " + page.url + " " + page.inner_text("body")[:2000]).lower()
    except Exception:
        return True
    return any(w in txt for w in BLOCK_WORDS)


def wait_unblocked(page, label):
    if not blocked(page):
        return True
    print(f"[ATTENTE] {label} : CAPTCHA ou blocage, résous-le dans la fenêtre…", flush=True)
    for _ in range(300):  # up to 15 min
        time.sleep(3)
        if not blocked(page):
            print(f"[OK] {label} débloqué", flush=True)
            time.sleep(3)
            return True
    print(f"[ÉCHEC] {label} toujours bloqué", flush=True)
    return False


ONLY = sys.argv[2] if len(sys.argv) > 2 else None
results = {}
with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context(str(OUT / "profil"), channel="msedge", headless=False,
                                               viewport={"width": 1400, "height": 900}, locale="fr-CH")
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    for site, (url, marker) in SITES.items():
        if ONLY and site != ONLY:
            continue
        for key, q in QUERIES.items():
            label = f"{site}/{key}"
            page.goto(url.format(urllib.parse.quote(q)), wait_until="domcontentloaded", timeout=90000)
            ok = wait_unblocked(page, label)
            time.sleep(4)
            links = []
            if ok:
                for a in page.query_selector_all("a[href]"):
                    h = a.get_attribute("href") or ""
                    if marker in h:
                        t = " ".join((a.inner_text() or "").split())
                        links.append({"href": urllib.parse.urljoin(page.url, h), "text": t[:150]})
            uniq = {l["href"]: l for l in links}
            results[label] = {"url": page.url, "ok": ok, "links": list(uniq.values())[:12],
                              "text": " ".join(page.inner_text("body").split())[:5000] if ok else ""}
            print(f"{label} : {len(uniq)} liens produit", flush=True)
            (OUT / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
            time.sleep(6)
    ctx.close()
print("TERMINÉ", flush=True)
