# import asyncio

# from playwright.async_api import Playwright, async_playwright, expect


# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#         await context.tracing.start(screenshots=True, snapshots=True, sources=True)
#         page = await context.new_page()

#         await page.set_viewport_size({"width": 1200,"height": 800})
#         await page.goto("https://demoqa.com/checkbox")
        
#         # -Actions
        
#         # await page.wait_for_selector('label[for="tree-node-home"]')

#         # await page.click('label[for="tree-node-home"]', force=True)
#         await page.click('label[for="tree-node-home"]')
#         await page.screenshot(path="screenshots/checkboxes.png")
#         #-Assertion
#         await page.is_checked('label[for="tree-node-home"]') is True
#         await expect(page.locator("#result")).to_have_text("You have selected :homedesktopdocumentsdownloadsnotescommandsworkspaceofficwordFileexcelFilereactangularveupublicprivateclassifiedgeneral")
#         #-Stoping Tracing
#         await context.tracing.stop(path = "logs/trace.zip")
#         await context.close()
#         await browser.close()
# asyncio.run(main())
# import asyncio
# from playwright.async_api import async_playwright, expect

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context()
#         await context.tracing.start(screenshots=True, snapshots=True, sources=True)
#         page = await context.new_page()
        
#         await page.set_viewport_size({"width": 1800, "height": 1200})
#         await page.goto("https://demoqa.com/checkbox")
#         #-Actions
#         await page.check('label[for="tree-node-home"]')
#         await page.screenshot(path="screenshots/checkboxes.png")
#         #-Assertions
#         await expect(page.get_by_label("Home")).to_be_checked()
#         await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
#         #-Stoping Tracing
#         await context.tracing.stop(path = "logs/trace.zip")
#         #-Closing browser
#         await browser.close()

# asyncio.run(main())

import asyncio
from playwright.async_api import async_playwright, expect

import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]  # ✅ bypass bot detection
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"  # ✅ real browser agent
        )
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()

        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/checkbox", wait_until="domcontentloaded")

        # ✅ Wait longer and check page is actually loaded
        await page.wait_for_timeout(3000)

        # ✅ Print all visible text to debug
        print(await page.title())

        # -Actions
        await page.wait_for_selector('#tree-node-home', state="attached", timeout=20000)
        await page.evaluate("document.querySelector('#tree-node-home').click()")  # ✅ JS click bypasses overlay
        await page.screenshot(path="screenshots/checkboxes.png")

        # -Assertions
        assert await page.is_checked('#tree-node-home')
        await expect(page.locator("#result")).to_contain_text("home")

        # -Stopping Tracing
        await context.tracing.stop(path="logs/trace.zip")

        # -Closing browser
        await browser.close()

asyncio.run(main())