from mypage_page import MyPage
from login_page import LoginPage
from signup_page import SignupPage
from main_page import MainPage
from driver_setup import get_driver
import unittest
import config
import random
import string


class WeverseTest(unittest.TestCase):
    N = 5  # 테스트 계정 개수 설정

    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.implicitly_wait(10)

    def setUp(self):
        print(f"테스트 시작: {self._testMethodName}")

    def tearDown(self):
        print(f"테스트 종료: {self._testMethodName}")


    def generate_random_email(self, index):
        return f"test{index}@benx.com"


    def generate_random_nickname(self, index):
        return f"test{index}"


    def test_01_register_and_login(self):
        """ N개의 랜덤 계정을 생성하여 회원가입 & 로그인 테스트 진행 """
        for i in range(1, self.N + 1):

            # 랜덤 계정 정보 생성
            email = self.generate_random_email(i)
            password = "pqa1212!"
            nickname = self.generate_random_nickname(i)

            try:
                # 회원 가입 진행
                main_page = MainPage(self.driver)
                main_page.open_main_page(config.BASE_URL)
                main_page.go_to_signup_page()

                signup_page = SignupPage(self.driver)
                signup_page.enter_email(email)
                if not signup_page.validate_email_status(0):  # status 0: 미가입 상태
                    self.fail("이메일 가입 가능 상태 검증 실패")

                signup_page.enter_new_password(password)
                signup_page.enter_nickname(nickname)
                signup_page.agree_terms()
                print(f"회원가입 완료 - 이메일: {email}")

                # 로그인 진행
                main_page.open_main_page(config.BASE_URL)
                main_page.go_to_signup_page()
                signup_page.enter_email(email)
                if not signup_page.validate_email_status(1):  # status 1: 가입 상태
                    self.fail("로그인 패스워드 입력창 확인 실패")

                signup_page.enter_login_password(password)
                print(f"로그인 성공 - 이메일: {email}")

                # 마이페이지 정보 확인
                main_page.open_main_page(config.BASE_URL)
                main_page.go_to_profile_page()

                my_page = MyPage(self.driver)
                saved_email = my_page.get_email()
                saved_nickname = my_page.get_nickname()
                saved_name = my_page.get_name()

                if not saved_email or not saved_nickname or not saved_name:
                    self.fail("마이페이지 정보 탐색 실패")
                print(f"마이페이지 정보 확인 - 이메일: {saved_email}, 닉네임: {saved_nickname}, 이름: {saved_name}")

            except Exception as e:
                self.fail(f"테스트 실패 - 오류: {e}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()