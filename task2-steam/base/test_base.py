import pytest
from pages.main_page import MainPage
from pages.about_page import AboutPage


class TestBase:

    main_page: MainPage
    about_page: AboutPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.main_page = MainPage(driver)
        request.cls.about_page = AboutPage(driver)
        self.main_page.open()
