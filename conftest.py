import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_user():
    with sync_playwright() as p:
        browser_user = p.chromium.launch(headless=False)
        yield browser_user
        browser_user.close()

@pytest.fixture
def page_user(browser_user):
    page_user = browser_user.new_page()
    yield page_user
    page_user.close()