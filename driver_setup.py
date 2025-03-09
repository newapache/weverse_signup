from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), options=options)
    return driver
