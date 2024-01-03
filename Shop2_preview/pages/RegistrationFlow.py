import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utils.Basetest import BaseTestDriver
from locators.LocatorsRegistrationFlow import LocatorsRegistration


class RegistrationScripts(BaseTestDriver):    #Tutaj sa łączone lokatory w metodzie init, bo je bedziemy przekazywac do log in
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.MainPageAccountButton = LocatorsRegistration.MainPageAccountButton
        self.RegistrationEmailInput = LocatorsRegistration.RegistrationEmailInput
        self.RegistrationPassowordinput = LocatorsRegistration.RegistrationPassowordinput
        self.RegistrationRegisterButton = LocatorsRegistration.RegistrationRegisterButton
        self.Registrationtext = LocatorsRegistration.RegistrationRegistrationtext
        self.RegistrationDashboardLoginText = LocatorsRegistration.RegistrationDashboardLoginText
        self.Advertelement = LocatorsRegistration.AdvertText

    def open_page(self):
        self.logger.info(" Navigate to url 'https://skleptest.pl'")
        self.driver.get('https://skleptest.pl')


    def click_on_MyAccountButton(self):
        self.logger.info("click on ,,MyAccount''")
        wait = WebDriverWait(self.driver, 10)
        element =self.driver.find_element(By.XPATH, self.MainPageAccountButton)
        if element.is_displayed():
           element.click()



    def create_account_first_step(self,email,password):

        self.logger.info("6. Enter Email and password")
        self.driver.find_element(By.XPATH, self.MainPageAccountButton).click()

        self.driver.find_element(By.XPATH, self.RegistrationEmailInput).click()
        self.driver.find_element(By.XPATH, self.RegistrationEmailInput).send_keys(email)
        self.driver.find_element(By.XPATH, self.RegistrationPassowordinput).click()
        self.driver.find_element(By.XPATH, self.RegistrationPassowordinput).send_keys(password)
        self.driver.find_element(By.NAME, self.RegistrationRegisterButton).click()
        #self.driver.find_element(By.XPATH, self.RegistrationPassowordinput).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)

    def is_user_loged(self):
        self.logger.info("Is client see My Account Dashboard")
        return self.driver.find_element(By.LINK_TEXT,self.RegistrationDashboardLoginText).is_displayed()

