from selenium.webdriver.common.by import By
from base_page import BasePage


class MyPage(BasePage):
    ACCOUNT_INFO = (By.XPATH, "//div[@class='account-info']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_account_info(self):
        return self.find_element(self.ACCOUNT_INFO).text
