from base.base_page import BasePage
from data_config.json_utility import JsonUtility
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    PAGE_URL = JsonUtility.value_from_json("links.main")
    ABOUT = (
        "xpath", "//*[@class='supernav_container']//*[contains(text(), 'About')]")

    def click_about_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ABOUT)).click()
