
from pages.mypage_page import MyPage
from pages.login_page import LoginPage
from signup_page import SignupPage
from main_page import MainPage
from driver_setup import get_driver
import unittest
import config


class WeverseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.implicitly_wait(10)

    def setUp(self):
        print(f"테스트 시작: {self._testMethodName}")

    def tearDown(self):
        if self._outcome.success:
            print(f"[성공]: {self._testMethodName}")
        else:
            print(f"[실패]:{self._testMethodName}")

    def test_01_open_main_page(self):
        """ 1. 위버스 홈페이지 진입 확인 """
        try:
            main_page = MainPage(self.driver)
            main_page.open_main_page(config.BASE_URL)
            self.assertIn("Weverse", self.driver.title)
            print("홈페이지 접속 성공")
        except Exception as e:
            print(f"홈페이지 접속 실패: {e}")
            raise

    def test_02_signup(self):
        """ 2. 회원 가입 진행 """
        raise Exception
        # try:
        #     main_page = MainPage(self.driver)
        #     main_page.go_to_signup_page()
        #     signup_page = SignupPage(self.driver)
        #     signup_page.enter_email(config.EMAIL)
        #     signup_page.validate_email()
        #     signup_page.enter_password(config.PASSWORD)
        #     signup_page.enter_nickname(config.NICKNAME)
        #     signup_page.agree_terms()
        #     print("회원가입 진행 완료")
        # except Exception as e:
        #     print(f"회원가입 실패: {e}")
        #     raise

    def test_03_login(self):
        """ 3. 로그인 진행 """
        try:
            main_page = MainPage(self.driver)
            main_page.go_to_signup_page()

            print("로그인 완료")
        except Exception as e:
            print(f"로그인 실패: {e}")
            raise

    def test_04_check_mypage(self):
        """ 4. 마이페이지 확인 """

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
