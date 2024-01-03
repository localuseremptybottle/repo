import logging
from random import randint
import time
from selenium.webdriver.common.by import By
from locators.LocatorsBlogFlow import LocatorsBlogFlow

class BlogPageScripts:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.MainPageBlogButton = LocatorsBlogFlow.MainPageBlogButton
        self.BlogPage_url = LocatorsBlogFlow.BlogPage_url
        self.BlogPageSearchbarinput = LocatorsBlogFlow.BlogPageSearchbarinput
        self.BlogPageSearchbarbutton = LocatorsBlogFlow.BlogPageSearchbarbutton
        self.BlogPageResultPostTitleText = LocatorsBlogFlow.BlogPageResultPostTitleText
        self.BlogPagePostReplySectionCommentInput = LocatorsBlogFlow.BlogPagePostReplySectionCommentInput
        self.BlogPagePostReplySectionNameInput = LocatorsBlogFlow.BlogPagePostReplySectionNameInput
        self.BlogPagePostReplySectionEmailInput = LocatorsBlogFlow.BlogPagePostReplySectionEmailInput
        self.BlogPagePostReplySectionWebsiteInput = LocatorsBlogFlow.BlogPagePostReplySectionWebsiteInput
        self.BlogPagePostReplySectionSaveFilledDataCheckbox = LocatorsBlogFlow.BlogPagePostReplySectionSaveFilledDataCheckbox
        self.BlogPagePostCommentButton = LocatorsBlogFlow.BlogPagePostCommentButton
        self.BlogPagePostAwaitingComunicat = LocatorsBlogFlow.BlogPagePostAwaitingComunicat
    def Open_Main_Page(self):
        self.logger.info(" Navigate to url 'https://skleptest.pl'")
        self.driver.get('https://skleptest.pl')
    def Click_on_BlogTab_button(self):
        self.logger.info(" Click on Blog tab button'")
        self.driver.find_element(By.XPATH,self.MainPageBlogButton).click()
    def Find_Post_and_open(self):
        self.logger.info("Find Post and open'")
        self.driver.find_element(By.XPATH, self.BlogPageSearchbarinput).click()
        self.driver.find_element(By.XPATH, self.BlogPageSearchbarinput).send_keys('Jackets For The Soul. What Color Is Yours?')
        self.driver.find_element(By.XPATH, self.BlogPageSearchbarbutton).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.BlogPageResultPostTitleText).click()
    def CommentPostwithoutLoggedUser(self):
        self.logger.info("Comment Post without Loged User")
        comment = 'Test Comment'+ str(randint(0, 1000))
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionCommentInput).click()
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionCommentInput).send_keys(comment)
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionNameInput).click()
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionNameInput).send_keys('!@#!!@#')
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionEmailInput).click()
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionEmailInput).send_keys('slonagrafik@gmai.com')
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionWebsiteInput).click()
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionWebsiteInput).send_keys('slonagrafik@gmai.com')
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionSaveFilledDataCheckbox).click()
        self.driver.find_element(By.XPATH, self.BlogPagePostCommentButton).click()
        assert self.driver.find_element(By.XPATH, self.BlogPagePostAwaitingComunicat).is_displayed()

    def CommentPostwithLoggedUser(self):
        comment = 'Test Comment' + str(randint(0, 1000))
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionCommentInput).click()
        self.driver.find_element(By.XPATH, self.BlogPagePostReplySectionCommentInput).send_keys(comment)
        self.driver.find_element(By.XPATH, self.BlogPagePostCommentButton).click()
        assert self.driver.find_element(By.XPATH, self.BlogPagePostAwaitingComunicat).is_displayed()

    def is_Blog_Address_Correct(self):
        self.logger.info("is 'Blog url' is correct")
        current_url_address = self.driver.current_url
        return current_url_address == self.BlogPage_url