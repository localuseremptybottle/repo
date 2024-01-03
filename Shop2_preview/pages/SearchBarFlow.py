import logging
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utils import Basetest
from locators.LocatorsSearchBar import LocatorsSearchBar


class SearchbarScripts:  # Tutaj sa łączone lokatory w metodzie init, bo je bedziemy przekazywac do log in
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.MainPageSearchbarInput = LocatorsSearchBar.MainPageSearchbarInput
        self.MainPageSearchbarButton = LocatorsSearchBar.MainPageSearchbarButton
        self.SearchBarNothingFoundtext = LocatorsSearchBar.SearchBarNothingFoundtext
        self.SearchBarHomeBreadcrumbButton = LocatorsSearchBar.SearchBarHomeBreadcrumbButton
        self.SearchBarResultText = LocatorsSearchBar.SearchBarResultText
        self.SearchBarFirstResultText  = LocatorsSearchBar.SearchBarFirstResultText
        self.SearchbarReturntoshopbutton = LocatorsSearchBar.SearchbarReturntoshopbutton


    def open_page(self):
        self.logger.info(" Navigate to url 'https://skleptest.pl'")
        self.driver.get('https://skleptest.pl')

    def click_on_SearchbarInput_and_find_denied_result(self):
        self.logger.info("click on ,,Searchbar'' input")
        text = 'r23r2'
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, self.MainPageSearchbarInput).click()
        self.driver.find_element(By.XPATH, self.MainPageSearchbarInput).send_keys(text)
        self.driver.find_element(By.XPATH, self.MainPageSearchbarButton).click()
    def click_on_SearchbarInputand_find_positive_result(self):
        self.logger.info("click on ,,Searchbar'' input")
        text = 'FITT Belts'
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element(By.XPATH, self.MainPageSearchbarInput).click()
        self.driver.find_element(By.XPATH, self.MainPageSearchbarInput).send_keys(text)
        self.driver.find_element(By.XPATH, self.MainPageSearchbarButton).click()
    def click_on_Searchbar_Icon(self):
        self.logger.info("click on ,,Searchbar icon'' to see results")
        self.driver.find_element(By.XPATH, self.MainPageSearchbarButton).click()
        self.driver.find_element(By.XPATH, self.SearchBarFirstResultText).click()
        self.driver.find_element(By.XPATH, self.SearchbarReturntoshopbutton).click()



    def is_NothingFound_displayed(self):
        self.logger.info("is ,,Nothing Found'' text displayed")
        time.sleep(5)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.SearchBarNothingFoundtext)))
        if element.is_displayed():
            return True

    def is_SearchResults_displayed(self):
        self.logger.info("is ,,SEARCH RESULTS FOR'' text displayed")
        time.sleep(5)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.SearchBarResultText)))
        if element.is_displayed():
            return True

