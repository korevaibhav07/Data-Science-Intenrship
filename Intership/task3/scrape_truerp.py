import asyncio
import pandas as pd
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

async def main():
    url = "https://www.truerp.in/"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

    
        await page.goto(url, wait_until="domcontentloaded", timeout=120000)
        await page.wait_for_timeout(3000) 

        html = await page.content()
        await browser.close()

    soup = BeautifulSoup(html, "html.parser")
    data = []

    for tag in ["h1", "h2", "h3"]:
        for h in soup.find_all(tag):
            text = h.get_text(" ", strip=True)
            if text:
                data.append({"Tag": tag.upper(), "Text": text})

    df = pd.DataFrame(data).drop_duplicates()
    df.to_csv("truerp_headings.csv", index=False)
    print("Saved: truerp_headings.csv")
    print(df.head(10))

if __name__ == "__main__":
    asyncio.run(main())
