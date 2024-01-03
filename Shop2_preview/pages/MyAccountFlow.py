import logging
from random import randint
import names
import time
from Utils import Basetest
from selenium.webdriver.common.by import By
from locators.LocatorsMyAccountFlow import LocatorsMyAccount
from locators.LocatorsRegistrationFlow import LocatorsRegistration

class MyAccountScripts:  # Tutaj sa łączone lokatory w metodzie init, bo je bedziemy przekazywac do log in
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.MyAccountButton = LocatorsMyAccount.MyAccountButton
        self.MyAccountLoginInput = LocatorsMyAccount.MyAccountLoginInput
        self.MyAccountLoginPassword = LocatorsMyAccount.MyAccountLoginPasswordInput
        self.MyAccountLoginButton = LocatorsMyAccount.MyAccountLoginButton
        self.MyAccountRemembermecheckbox = LocatorsMyAccount.MyAccountRemembermecheckbox
        self.MyAccountLostyourPasswordButton = LocatorsMyAccount.MyAccountLostyourPasswordButton

        # LostPassword
        self.MyAccountRecorveryUsernameInput = LocatorsMyAccount.MyAccountRecorveryUsernameInput
        self.MyAccountRecorveryResetPasswordButton = LocatorsMyAccount.MyAccountRecorveryResetPasswordButton
        self.MyAccountRecorveryErrorTextEnterUsername = LocatorsMyAccount.MyAccountRecorveryErrorTextEnterUsername
        self.MyAccountRecorveryErrorTextInvalidUsername = LocatorsMyAccount.MyAccountRecorveryErrorTextInvalidUsername
        self.MyAccountRecorveryPositiveTextEmailResetText = LocatorsMyAccount.MyAccountRecorveryPositiveTextEmailResetText



        self.MyAccountErrorIncorectPasswordtext = LocatorsMyAccount.MyAccountErrorIncorectPasswordtext
        self.MyAccountErrorIncorectEmailtext =LocatorsMyAccount.MyAccountErrorIncorectEmailtext
        #Dashboard for logged users

        self.MyAccountDashboardbutton  = LocatorsMyAccount.MyAccountDashboardTab
        self.MyAccountOrdersbutton = LocatorsMyAccount.MyAccountOrdersTab
        self.MyAccountDownloadsbutton = LocatorsMyAccount.MyAccountDownloadsTab
        self.MyAccountAddressesbutton = LocatorsMyAccount.MyAccountAddressesTab
        self.MyAccountAccountDetailsbutton = LocatorsMyAccount.MyAccountAccountDetailsTab
        self.MyAccountAccountLogoutbutton = LocatorsMyAccount.MyAccountAccountLogoutTab

        #DasboardTab
        self.MyAccountDashboardRecentOrderdslinktext = LocatorsMyAccount.MyAccountDashboardTabRecentOrderdslinktext
        self.MyAccountDashboardShippingadresslinktext = LocatorsMyAccount.MyAccountDashboardTabShippingadresslinktext
        self.MyAccountDashboardEditPasswordlinktext = LocatorsMyAccount.MyAccountDashboardTabEditPasswordlinktext
        self.MyAccountLogoutTabConfirmandLogoutlinktext = LocatorsMyAccount.MyAccountLogoutTabConfirmandLogoutlinktext
        #Orders
        self.MyAccountOrdersTab1Productviewbutton =LocatorsMyAccount.MyAccountOrdersTab1Productviewbutton
        self.MyAccountOrdersTab2Productviewbutton = LocatorsMyAccount.MyAccountOrdersTab2Productviewbutton
        self.MyAccountOrdersTabOrderDetailsText =LocatorsMyAccount.MyAccountOrdersTabOrderDetailstext
        self.MyAccountOrdersTabOrderDetailsPrint = LocatorsMyAccount.MyAccountOrdersTabOrderDetailsPrint



    #Tutaj rejestruje nowego uzytkownika i potem nie wylogowujac sie z konta sprawdzam zakładki
    def open_page(self):
        self.logger.info(" Navigate to url 'https://skleptest.pl'")
        self.driver.get('https://skleptest.pl/my-account/')

    def VerifyDashboardtab(self):
        self.logger.info(" Navigate to Dashboard tab'")
        self.driver.find_element(By.XPATH, self.MyAccountDashboardbutton).click()
        self.driver.find_element(By.LINK_TEXT, self.MyAccountDashboardRecentOrderdslinktext).click()
        self.driver.back()
        self.driver.find_element(By.LINK_TEXT, self.MyAccountDashboardShippingadresslinktext).click()
        self.driver.back()
        self.driver.find_element(By.LINK_TEXT, self.MyAccountDashboardEditPasswordlinktext).click()
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MyAccountAccountLogoutbutton).click()
        self.driver.find_element(By.XPATH,self.MyAccountLogoutTabConfirmandLogoutlinktext).click()
    def VerifyOrdersTab(self):
        self.logger.info(" Navigate to Orders tab'")
        self.driver.find_element(By.XPATH, self.MyAccountOrdersbutton).click()
        time.sleep(3)
        #text = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.MyAccountOrdersTabOrderDetailsText)
        self.driver.find_element(By.XPATH, self.MyAccountOrdersTab1Productviewbutton).click()
        self.driver.back()

        #self.driver.find_element(By.XPATH, self.MyAccountOrdersTab1Productviewbutton).click()
       # if text.is_displayed():
           # self.driver.find_element(By.XPATH,self.MyAccountOrdersbutton).click()

    def create_account(self):
        self.logger.info("New User Registration")
        email = str(randint(0, 1000)) + 'test@test.com'
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female')+ str('!@#'))
        self.driver.find_element(By.XPATH, LocatorsRegistration.RegistrationEmailInput).click()
        self.driver.find_element(By.XPATH, LocatorsRegistration.RegistrationEmailInput).send_keys(email)
        self.driver.find_element(By.XPATH, LocatorsRegistration.RegistrationPassowordinput).click()
        self.driver.find_element(By.XPATH, LocatorsRegistration.RegistrationPassowordinput).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.NAME, LocatorsRegistration.RegistrationRegisterButton).click()

    def LogintoAccountWithWrongPassword(self):
        self.driver.find_element(By.XPATH, self.MyAccountLoginInput).click()
        self.driver.find_element(By.XPATH, self.MyAccountLoginInput).send_keys('slonagrafika@gmail.com')
        self.driver.find_element(By.XPATH, self.MyAccountLoginPassword).click()
        self.driver.find_element(By.XPATH, self.MyAccountLoginPassword).send_keys('#!@#!@')
        self.driver.find_element(By.XPATH, self.MyAccountRemembermecheckbox).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.MyAccountLoginButton).click()
    def LogintoAccountWithWrongEmail(self):
        self.driver.find_element(By.XPATH, self.MyAccountLoginInput).click()
        self.driver.find_element(By.XPATH, self.MyAccountLoginInput).send_keys('slonagrat43t23fika@gmail.com')
        self.driver.find_element(By.XPATH, self.MyAccountLoginPassword).click()
        self.driver.find_element(By.XPATH, self.MyAccountLoginPassword).send_keys('#!@#!@')
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.MyAccountRemembermecheckbox).click()
        self.driver.find_element(By.XPATH, self.MyAccountLoginButton).click()

    def RecorveryyourAccount(self):
        email ='slonagrafika132@gmail.com'
        self.logger.info("Recorvery Passwrod process")
        self.driver.find_element(By.XPATH, self.MyAccountLostyourPasswordButton).click()
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryUsernameInput).click()
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryResetPasswordButton).click()

        assert self.driver.find_element(By.XPATH, self.MyAccountRecorveryErrorTextEnterUsername).is_displayed()

        self.driver.find_element(By.XPATH, self.MyAccountRecorveryUsernameInput).click()
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryUsernameInput).send_keys(email)
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryResetPasswordButton).click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, self.MyAccountRecorveryErrorTextInvalidUsername).is_displayed()
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryUsernameInput).click()
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryUsernameInput).send_keys('slonagrafika@gmail.com')
        self.driver.find_element(By.XPATH, self.MyAccountRecorveryResetPasswordButton).click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH, self.MyAccountRecorveryPositiveTextEmailResetText).is_displayed()

    def is_ErrorIncorectPasswordtext_inMyAccount_displayed(self):
        self.logger.info("is Error Password text is displayed")
        return self.driver.find_element(By.XPATH, self.MyAccountErrorIncorectPasswordtext).is_displayed()
    def is_ErrorIncorecteEmailtext_inMyAccount_displayed(self):
        self.logger.info("is Errort Email text is displayed")
        return self.driver.find_element(By.XPATH, self.MyAccountErrorIncorectEmailtext).is_displayed()






