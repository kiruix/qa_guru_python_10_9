from selene import browser
import pytest


@pytest.fixture(autouse=True)
def browser_config():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
