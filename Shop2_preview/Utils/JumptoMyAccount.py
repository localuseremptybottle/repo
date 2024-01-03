from selenium.webdriver.common.by import By
import logging
from Utils import Basetest
from locators.LocatorsRegistrationFlow import LocatorsRegistration

class JumptoMyAccountClass:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.MainpageAccountButton = LocatorsRegistration.MainPageAccountButton
    def JumptoMyAccount(self):
        self.logger.info("JumpToMyAccount")
        self.driver.find_element(By.XPATH, self.MainpageAccountButton).click()