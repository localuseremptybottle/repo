import time
from selenium.webdriver.common.by import By
import logging
from locators.LocatorsRegistrationFlow import LocatorsRegistration
from Utils.Basetest import BaseTestDriver

class BacktoMainclass:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.Mainpagebutton = LocatorsRegistration.MainPageGenericshoptext
    def BackToMain(self):
        self.logger.info("Returning to MainPage")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Mainpagebutton).click()
