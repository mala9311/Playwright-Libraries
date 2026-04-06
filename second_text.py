import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright as p:
        browser = await p.chromium.launch(headless=False, slow_mo=2000)
        page = await page.new_page()
        page.goto('https://unsplash.com')
        image_text=page.get_by_alt_text("a group of people sitting around a table with food")
        image_text.highlight()
        print(page.title())
        print(browser.close())



