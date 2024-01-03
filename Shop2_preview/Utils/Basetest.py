from selenium import webdriver
import pytest
class BaseTestDriver:
    driver = None
    @classmethod
    @pytest.fixture()
    def setup_class(cls):
        cls.driver = webdriver.Chrome(executable_path=r'C:\Users\ST\PycharmProjects\chromedriver\chromedriver.exe')
        # (executable_path=r'C:\Users\ST\PycharmProjects\chromedriver\chromedriver.exe', options=options)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(6)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()