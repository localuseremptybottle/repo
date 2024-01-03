import logging
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators.LocatorsFooter import LocatorsFooter
from Utils import Basetest

class FooterScripts:  # Tutaj sa łączone lokatory w metodzie init, bo je bedziemy przekazywac do log in
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        #Tags
        self.MainPageTag1Button = LocatorsFooter.MainPageTag1Button
        self.MainPageTag2Button = LocatorsFooter.MainPageTag2Button
        self.MainPageTag3Button = LocatorsFooter.MainPageTag3Button
        self.MainPageTag4Button = LocatorsFooter.MainPageTag4button
        self.MainPageTag5Button = LocatorsFooter.MainPageTag5button
        self.MainPageTag6Button = LocatorsFooter.MainPageTag6button
        #RecentsPosts
        self.MainpageRecentPosts1Title = LocatorsFooter.MainpageRecentPosts1Title
        self.MainpageRecentPosts2Title = LocatorsFooter.MainpageRecentPosts2Title
        self.MainpageRecentPosts3Title = LocatorsFooter.MainpageRecentPosts3Title
        self.MainpageRecentPosts4Title = LocatorsFooter.MainpageRecentPosts4Title
        #About
        self.MainpageAboutText1 = LocatorsFooter.MainpageAboutText1
        self.MainpageAboutText2 = LocatorsFooter.MainpageAboutText2
        #Newsletter
        self.MainpageNewsletterNameInput = LocatorsFooter.MainpageNewsletterNameInput
        self.MainpageNewsletterNameEmail = LocatorsFooter.MainpageNewsletterNameEmail
        self.MainpageNewsletterSubscribeButton  = LocatorsFooter.MainpageNewsletterSubscribeButton
        self.MainpageNewsletterSuccessfullytext = LocatorsFooter.MainpageNewsletterSuccessfullyText
        self.MainpageNewsletterPleaseTrylaterText = LocatorsFooter.MainpageNewsletterPleaseTrylaterText

    def try_open_all_tags(self):
        self.logger.info("is Are all tags openable")
        self.driver.find_element(By.XPATH, self.MainPageTag1Button).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainPageTag2Button).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainPageTag3Button).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainPageTag4Button).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainPageTag5Button).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainPageTag6Button).click()
        time.sleep(1)
        self.driver.back()
    def try_open_all_RecentPost(self):
        self.logger.info("is Are all Recent Posts openable")
        self.driver.find_element(By.XPATH, self.MainpageRecentPosts1Title).click()
        time.sleep(2)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainpageRecentPosts2Title).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainpageRecentPosts3Title).click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.XPATH, self.MainpageRecentPosts4Title).click()
        time.sleep(1)
        self.driver.back()
    def is_About_Text_visible_on_footer(self):
        self.logger.info("is About text is visible on footer")
        return self.driver.find_element(By.XPATH, self.MainpageAboutText1).is_displayed()
    def Verify_Subscription_in_home_page_Passed(self):
        self.logger.info("Verify Subscription is passed")
        self.driver.find_element(By.XPATH, self.MainpageNewsletterNameInput).click()
        self.driver.find_element(By.XPATH, self.MainpageNewsletterNameInput).send_keys('Duszan')
        self.driver.find_element(By.XPATH, self.MainpageNewsletterNameEmail).click()
        self.driver.find_element(By.XPATH, self.MainpageNewsletterNameEmail).send_keys('DandoPra@pra.pl')
        self.driver.find_element(By.XPATH, self.MainpageNewsletterSubscribeButton).click()
        time.sleep(2)
        return self.driver.find_element(By.XPATH, self.MainpageNewsletterSuccessfullytext).is_displayed()


