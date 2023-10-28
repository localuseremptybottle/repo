import chromedriver_auto
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options = Options()

#Ten plik jest stoworzyn po to, by od razu otwierała sie przeglądarka przed testami,
#to jest wazna kwestia by od razu to ustawiać i sie nie jebać potem z tym
#ODPALANIE NA POCZATKU OZNACZAMY FIXTURE

@pytest.fixture()
def setup(request):
        options = Options()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(executable_path=r'C:\Users\ST\PycharmProjects\chromedriver\chromedriver.exe', options=options)
        driver.maximize_window()
        driver.implicitly_wait(6)
        request.cls.driver = driver
        yield
        driver.quit()