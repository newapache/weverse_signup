from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    # 요소 탐색
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # 요소 클릭
    def click_element(self, locator, retries=3):
        for i in range(retries):
            try:
                element = self.wait.until(
                    EC.presence_of_element_located(locator))
                # 요소가 화면에 보이지 않으면 스크롤 이동
                self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(0.5)
                element = self.wait.until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                print(f"재시도 {i+1}/{retries}")
                time.sleep(1)
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", element)
                return
        raise Exception("요소를 클릭할 수 없습니다.")

    # 텍스트 입력
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # 체크박스 선택
    def check_checkbox(self, locator):
        checkbox = self.wait.until(EC.presence_of_element_located(locator))
        # 체크박스가 체크되지 않은 경우 클릭
        if not checkbox.is_selected():
            checkbox.click()
