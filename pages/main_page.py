from selenium.webdriver.common.by import By
from base_page import BasePage
import locators as lc


class MainPage(BasePage):
    SIGN_IN_BUTTON = (By.CLASS_NAME, lc.sign_up_btn_class)
    PROFILE_BUTTON = (By.CLASS_NAME, lc.mypage_btn_class)
    MYPAGE_BUTTON = (By.LINK_TEXT, "계정 설정")

    def __init__(self, driver):
        super().__init__(driver)

    def open_main_page(self, url):
        self.open_url(url)

    def go_to_signup_page(self):
        self.click_element(self.SIGN_IN_BUTTON)

    def go_to_profile_page(self):
        self.click_element(self.PROFILE_BUTTON)
        self.click_element(self.MYPAGE_BUTTON)

