import sys, asyncio, re, json, os
from playwright.async_api import async_playwright
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'out')
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"
async def main():
    headless = os.environ.get('HEADED')!='1'
    urls = sys.argv[1:]
    async with async_playwright() as p:
        ctx = await p.chromium.launch_persistent_context(os.path.join(OUT,'..','profile'), headless=headless, executable_path=os.path.join(os.environ['LOCALAPPDATA'],'ms-playwright','chromium-1223','chrome-win64','chrome.exe'), user_agent=UA, locale='fr-CH', viewport={'width':1400,'height':1000})
        page = ctx.pages[0] if ctx.pages else await ctx.new_page()
        import time
        time.sleep(int(os.environ.get('INITIAL','0')))
        for i,u in enumerate(urls):
            if i: await page.wait_for_timeout(int(os.environ.get('GAP','0'))*1000)
            name = re.sub(r'[^A-Za-z0-9]+','_',u)[-90:]
            try:
                r = await page.goto(u, wait_until='domcontentloaded', timeout=60000)
                await page.wait_for_timeout(int(os.environ.get('WAIT','6000')))
                for sel in ['#onetrust-accept-btn-handler','button:has-text("Accepter")','button:has-text("Accept")','button:has-text("Tout accepter")']:
                    try:
                        b=page.locator(sel).first
                        if await b.is_visible(timeout=500): await b.click(); await page.wait_for_timeout(1500); break
                    except Exception: pass
                txt = await page.inner_text('body')
                links = await page.eval_on_selector_all('a[href]', 'els=>els.map(e=>e.href)')
                open(os.path.join(OUT,name+'.txt'),'w',encoding='utf-8').write(f"URL: {page.url}\nSTATUS: {r.status if r else None}\nTITLE: {await page.title()}\n\n{txt}\n\nLINKS:\n"+"\n".join(sorted(set(links))))
                await page.screenshot(path=os.path.join(OUT,name+'.png'))
                if 'perfdrive' in page.url or 'Captcha' in (await page.title()):
                    print('CAPTCHA, stopping at',u); break
                print(f"OK {r.status if r else None} {page.url} -> {name}.txt len={len(txt)}")
            except Exception as e:
                print("ERR",u,e)
        await ctx.close()
asyncio.run(main())
