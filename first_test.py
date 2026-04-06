from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.google.com/')
    page.wait_for_timeout(2000)    # wait for 2 sec
    print(page.title())
    browser.close()