import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()

        await page.set_viewport_size({"width": 1200,"height": 800})
        await page.goto("https://demoqa.com/checkbox")
        
        # -Actions
        # await page.check('#tree-node-home')
        # await page.wait_for_selector('label[for="tree-node-home"]')

        # await page.click('label[for="tree-node-home"]', force=True)
        await page.click('text=Home')
        await page.screenshot(path="screenshots/checkboxes.png")
        #-Assertion
        await page.locator('text=Home')
        await expect(page.locator("#result")).to_have_text("You have selected :homedesktopdocumentsdownloadsnotescommandsworkspaceofficewordFileexcelFilereactangularveupublicprivateclassifiedgeneral")
        #-Stoping Tracing
        await context.tracing.stop(path = "logs/trace.zip")
        await context.close()
        await browser.close()
asyncio.run(main())




