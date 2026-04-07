from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch a browser
    browser = p.chromium.launch(headless=False, slow_mo= 2000)
    # Create a page
    page = browser.new_page()
    # visit the playwright new _page
    page.goto('https://playwright.dev/python')
    #Locate a link element with "Docs" text
    docs_button = page.get_by_role('link',name ="Docs")
    docs_button.click()
    # input field Locator
   #
    # Get the URL
    print("Docs:",page.url)
   # page.wait_for_timeout(2000)    # wait for 2 sec
    print(page.title())
    browser.close()