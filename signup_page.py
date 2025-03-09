from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as lc
import time


class SignupPage(BasePage):
    EMAIL_INPUT = (By.NAME, lc.email_input_name)
    CONTINUE_BUTTON = (By.CLASS_NAME, lc.continue_button_class)
    VALIDATE_EMAIL = (By.XPATH, lc.email_validate_xpath)
    PASSWORD_INPUT = (By.NAME, lc.password_input_name)
    NEW_PASSWORD_INPUT = (By.NAME, lc.new_password_input_name)
    NEW_PASSWORD_CONFIRM_INPUT = (By.NAME, lc.new_password_confirm_input_name)
    NICKNAME_INPUT = (By.NAME, lc.nickname_input_name)
    TERMS_CHECKBOX = (By.CLASS_NAME, lc.terms_checkbox_class)
    TERMS_POPUP_BUTTON = (By.CLASS_NAME, lc.terms_popup_button_class)

    def __init__(self, driver):
        super().__init__(driver)

    # 이메일 입력
    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)
        self.click_element(self.CONTINUE_BUTTON)

    def validate_email_status(self, status: int):
        # 가입 이력이 없는 경우 
        if status == 0:
            signup_validate = self.find_element(self.VALIDATE_EMAIL)
            if signup_validate:
                self.click_element(self.CONTINUE_BUTTON)
                return True
            else:
                return False  
        # 가입 이력이 있는 경우
        elif status == 1:
            login_validate = self.find_element(self.PASSWORD_INPUT)
            if login_validate:
                return True
            else:
                return False 


    # 가입 패스워드 입력
    def enter_new_password(self, password):
        self.enter_text(self.NEW_PASSWORD_INPUT, password)
        # 첫 번째 패스워드 입력 확인 후 진행
        WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element(
            *self.NEW_PASSWORD_INPUT).get_attribute("value") == password)
        self.enter_text(self.NEW_PASSWORD_CONFIRM_INPUT, password)
        self.click_element(self.CONTINUE_BUTTON)


    # 로그인 패스워드 입력 
    def enter_login_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.CONTINUE_BUTTON)
        time.sleep(3)


    # 닉네임 입력
    def enter_nickname(self, nickname):
        self.enter_text(self.NICKNAME_INPUT, nickname)
        self.click_element(self.CONTINUE_BUTTON)

    # 약관 동의
    def agree_terms(self):
        self.check_checkbox(self.TERMS_CHECKBOX)
        self.click_element(self.CONTINUE_BUTTON)
        self.click_element(self.TERMS_POPUP_BUTTON)
