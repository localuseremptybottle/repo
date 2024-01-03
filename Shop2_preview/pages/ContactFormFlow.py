import logging
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.LocatorsContactForm import LocatorsContactForm

from Utils import Basetest

class ContactFormScripts:  # Tutaj sa łączone lokatory w metodzie init, bo je bedziemy przekazywac do log in
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.MainPageContactButton = LocatorsContactForm.MainPageContactButton
        self.ContactformNameInput = LocatorsContactForm.ContactformNameInput
        self.ContactFormEmailInput = LocatorsContactForm.ContactFormEmailInput
        self.ContactFormSubcjectInput = LocatorsContactForm.ContactFormSubcjectInput
        self.ContactFormMessageInput = LocatorsContactForm.ContactFormMessageInput
        self.ContactFormSendButton = LocatorsContactForm.ContactFormSendButton
        self.ContactFormErrorText = LocatorsContactForm.ContactFormErrorText

    def open_page(self):
        self.logger.info(" Navigate to url 'https://skleptest.pl'")
        self.driver.get('https://skleptest.pl')

    def click_on_ContactButton(self):
        self.logger.info("click on ,,Contact''")
        wait = WebDriverWait(self.driver, 10)
        element = self.driver.find_element(By.XPATH, self.MainPageContactButton)
        if element.is_displayed():
            element.click()

    def FillContactForm(self):
        self.logger.info("Fill Contact Form")
        name = 'User'
        email = 'Test@test.pl'
        subject = 'test'
        self.driver.find_element(By.XPATH, self.ContactformNameInput).click()
        self.driver.find_element(By.XPATH, self.ContactformNameInput).send_keys(name)
        self.driver.find_element(By.XPATH, self.ContactFormEmailInput).click()
        self.driver.find_element(By.XPATH, self.ContactFormEmailInput).send_keys(email)
        self.driver.find_element(By.XPATH, self.ContactFormSubcjectInput).click()
        self.driver.find_element(By.XPATH, self.ContactFormSubcjectInput).send_keys(subject)
        self.driver.find_element(By.XPATH, self.ContactFormMessageInput).click()
        self.driver.find_element(By.XPATH, self.ContactFormMessageInput).send_keys(subject)
        self.driver.find_element(By.XPATH, self.ContactFormSendButton).click()

        # self.driver.find_element(By.XPATH, self.RegistrationPassowordinput).send_keys(Keys.ENTER)

    def is_ErrorText_displayed(self):
        self.logger.info("Is Error Message displayed")
        time.sleep(5)
        wait = WebDriverWait(self.driver, 6)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ContactFormErrorText)))
        if element.is_displayed():
            return True
