from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Remote

class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = Options()
            options.add_experimental_option('detach', True)
            options.add_argument("start-maximized")
            #return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            options.set_capability("browserName","chrome")
            return webdriver.Remote('http://192.168.33.2:4444',options=options)
        elif browser =="firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        raise Exception("Provide valid driver name / Podaj poprawną nazwę przeglądarki")