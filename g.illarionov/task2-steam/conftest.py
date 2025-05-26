import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage


class SingletonWebDriver:
    _instance = None

    @classmethod
    def get_instance(cls, options=None):
        if not cls._instance:
            cls._instance = webdriver.Chrome(options=options)
        return cls._instance

    @classmethod
    def close_instance(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None


@pytest.fixture(autouse=True)
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--lang=en")
    driver = SingletonWebDriver.get_instance(options=options)
    yield driver
    SingletonWebDriver.close_instance()
