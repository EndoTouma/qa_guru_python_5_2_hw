import pytest
from selene.support.shared import browser, config


@pytest.fixture(scope="function")
def setup_browser():
	browser.open('https://www.google.com/')
	browser.driver.set_window_size(1024, 600)
