위버스 웹 페이지에서 회원 가입 및 로그인을 수행하는 자동화 테스트 스크립트 

### 1.테스트 실행 
- tests/test_weverse.py
- 반복 테스트: tests/test_weverse_repeat.py

### 2.페이지 객체 
- 회원가입/로그인 페이지: pages/signup_page.py
- 마이페이지: pages/my_page.py
- 메인페이지: pages/main_page.py
- 공통페이지: pages/base_page.py

### 3. 기타
- 데이터 파일(계정 정보 등): config.py
- 웹 드라이버 설정: driver_setup.py
- 로케이터 정보: locators.py
