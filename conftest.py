import pytest
from selene import browser

@pytest.fixture(scope="function")
def browser_config():
    browser.config.window_width = 1920 #ширина
    browser.config.window_height = 1080 #высота

    browser.config.base_url = "https://demoqa.com"

    yield
    browser.quit()