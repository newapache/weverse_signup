from selenium.webdriver.common.by import By
from base_page import BasePage
import locators as lc

class MyPage(BasePage):
    EMAIL = (By.XPATH, lc.email_xpath)
    NICKNAME = (By.XPATH, lc.nickname_xpath)
    NAME = (By.XPATH, lc.name_xpath)

    def __init__(self, driver):
        super().__init__(driver)

    def open_my_page(self, url):
        self.open_url(url)

    def get_email(self):
        """ 이메일 정보 가져오기 """
        return self.get_text(self.EMAIL)

    def get_nickname(self):
        """ 닉네임 정보 가져오기 """
        return self.get_text(self.NICKNAME)

    def get_name(self):
        """ 이름 정보 가져오기 """
        return self.get_text(self.NAME)
