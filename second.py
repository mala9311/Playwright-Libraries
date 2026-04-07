import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=10000)
        page = await browser.new_page()
        await page.goto('https://unsplash.com')
        image_text=page.get_by_alt_text("a group of people sitting around a table with food")
        await image_text.highlight()
        print(await page.title())
        await browser.close()

asyncio.run(main())  



