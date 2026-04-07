from playwright.sync_api import Page
import pytest 
# To skip one browser 
# @pytest.mark.skip_browser("chromium")
@pytest.mark.only_browser("chromium")
def test_title(page:Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"

def test_inventory(page:Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."
# ### write in terminal commands
# To run in both the browser -> pytest --headed --base-url https://www.saucedemo.com --browser chromium --browser firefox
# def test_inventory(page: Page):
#     page.goto("https://www.saucedemo.com/inventory.html")
#     error = page.locator("h3")
#     assert error.inner_text() == "Epic sadface: You can only access '/inventory.html' when you are logged in."
# To trace the browser how it working -> playwright show-trace .\test-results\test-saucedemo-py-test-inventory-chromium\trace.zip