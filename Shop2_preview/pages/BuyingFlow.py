import logging
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Utils import Basetest

from locators.LocatorsBuyingFlow import LocatorsBuyingflow
class BuyingFLowScripts:
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        #Additionalfortest
        self.MainPageMyAccountButton = LocatorsBuyingflow.MainPageMyAccountButton
        self.MainPageMostwantedCattegorybutton = LocatorsBuyingflow.MainPageMostwantedCattegorybutton
        self.MainPageBlackTopsProduct1AddtoCartButton  = LocatorsBuyingflow.MainPageBlackTopsProduct1AddtoCartButton
        self.MainPageBlackTopsProduct2AddtoCartButton = LocatorsBuyingflow.MainPageBlackTopsProduct2AddtoCartButton
        self.MainPageMyCartButton = LocatorsBuyingflow.MainPageMyCartButton
        self.MainpageTrendsCategory1ProductAddtocart = LocatorsBuyingflow.MainpageTrendsCategory1ProductAddtocart
        self.MainpageTrendsCategory2ProductAddtocart = LocatorsBuyingflow.MainpageTrendsCategory2ProductAddtocart
        self.MainpageTrendsCategory3ProductAddtocart = LocatorsBuyingflow.MainpageTrendsCategory3ProductAddtocart
        self.MainpageTrendsCategory4ProductAddtocart = LocatorsBuyingflow.MainpageTrendsCategory4ProductAddtocart
        self.MainPageCategoriesCategorylist =LocatorsBuyingflow.MainPageCategoriesCategorylist
        self.MainPageCategoriesCategorylistShoes =LocatorsBuyingflow.MainPageCategoriesCategorylistShoes
        self.ShoesCattegoryProduct1AddtocartButton = LocatorsBuyingflow.ShoesCattegoryProduct1AddtocartButton

        self.MostwantedCategory1Product1Photo = LocatorsBuyingflow.MostwantedCategory1Product1Photo
        self.ProductPageReviewButton = LocatorsBuyingflow.ProductPageReviewButton
        self.ProductPageDescriptionButton = LocatorsBuyingflow.ProductPageDescriptionButton
        self.ProductPageAddtocartButton = LocatorsBuyingflow.ProductPageAddtocartButton
        self.BracketReturnToShopButton = LocatorsBuyingflow.BracketReturnToShopButton
        self.BracketProduct1Quantityplusbutton = LocatorsBuyingflow.BracketProduct1Quantityplusbutton
        self.BracketProduct2Quantityplusbutton = LocatorsBuyingflow.BracketProduct2Quantityplusbutton
        self.BracketProduct1Quantityminusbutton = LocatorsBuyingflow.BracketProduct1Quantityminusbutton
        self.BracketProduct2Quantityminusbutton = LocatorsBuyingflow.BracketProduct2Quantityminusbutton
        self.BracketProduct2DeleteButton = LocatorsBuyingflow.BracketProduct2DeleteButton
        self.BracketProduct4DeleteButton = LocatorsBuyingflow.BracketProduct4DeleteButton
        self.BracketProduct6DeleteButton = LocatorsBuyingflow.BracketProduct6DeleteButton
        self.BracketProceedtoCheckoutButton = LocatorsBuyingflow.BracketProceedtoCheckoutButton
        self.BracketFirstnameinput = LocatorsBuyingflow.BracketFirstnameinput
        self.BracketLastnameInput = LocatorsBuyingflow.BracketLastnameInput
        self.BracketLastnameInput = LocatorsBuyingflow.BracketLastnameInput
        self.BracketCountryListbutton = LocatorsBuyingflow.BracketCountryListbutton
        self.BracketCountryListSearchbar = LocatorsBuyingflow.BracketCountryListSearchbar
        self.BracketCompanyInput = LocatorsBuyingflow.BracketCompanyInput
        self.BracketUpdatecartbutton =  LocatorsBuyingflow.BracketUpdatecartbutton
        self.BracketStreetaddressInput = LocatorsBuyingflow.BracketStreetaddressInput
        self.BracketStreetAddressOptionalInput = LocatorsBuyingflow.BracketStreetAddressOptionalInput
        self.BracketStateListbutton = LocatorsBuyingflow.BracketStateListbutton
        self.BracketStateListSearchBar = LocatorsBuyingflow.BracketStateListSearchBar
        self.BracketZipCodeInput = LocatorsBuyingflow.BracketZipCodeInput
        self.BracketTownInput = LocatorsBuyingflow.BracketTownInput
        self.BracketPhoneInput = LocatorsBuyingflow.BracketPhoneInput
        self.BracketEmailInput = LocatorsBuyingflow.BracketEmailInput
        self.BracketCreateAnAccountcheckbox = LocatorsBuyingflow.BracketCreateAnAccountcheckbox
        self.BracketCreateAnAccountPasswordInput  = LocatorsBuyingflow.BracketCreateAnAccountPasswordInput

        self.BracketShippingtoaDiffrentadresCheckbox = LocatorsBuyingflow.BracketShippingtoaDiffrentadresCheckbox
        self.BracketDiffrentAddressFistNameInput = LocatorsBuyingflow.BracketDiffrentAddressFistNameInput
        self.BracketDiffrentAddressLastNameInput = LocatorsBuyingflow.BracketDiffrentAddressLastNameInput
        self.BracketDiffrentCompanyNameinput = LocatorsBuyingflow.BracketDiffrentCompanyNameinput
        self.BracketDiffrentCountryListbutton = LocatorsBuyingflow.BracketDiffrentCountryListbutton
        self.BracketDiffrentCountryListSearchbar = LocatorsBuyingflow.BracketDiffrentCountryListSearchbar
        self.BracketDiffrentStreetAddres = LocatorsBuyingflow.BracketDiffrentStreetAddres
        self.BracketDiffrentStreetAddress2 = LocatorsBuyingflow.BracketDiffrentStreetAddress2
        self.BracketDiffrentTownInput = LocatorsBuyingflow.BracketDiffrentTownInput
        self.BracketDiffrentStateListButton = LocatorsBuyingflow.BracketDiffrentStateButton
        self.BracketDiffrentStateSearchBar = LocatorsBuyingflow.BracketDiffrentStateSearchBar
        self.BracketDiffrentPostCodeinput = LocatorsBuyingflow.BracketDiffrentPostCodeinput
        self.BracketDiffrentOrderNotes = LocatorsBuyingflow.BracketDiffrentOrderNotes

        self.BracketDirectbanktransferCheckbox = LocatorsBuyingflow.BracketDirectbanktransferCheckbox
        self.BracketCheckPaymentsCheckbox = LocatorsBuyingflow.BracketCheckPaymentsCheckbox
        self.BracketCashOnDeliveryCheckbox = LocatorsBuyingflow.BracketCashOnDeliveryCheckbox
        self.BracketPaypalCheckbox = LocatorsBuyingflow.BracketPaypalCheckbox
        self.BracketPlaceOrderButton = LocatorsBuyingflow.BracketPlaceOrderButton
        self.BracketShippingtoaDiffrentadresCheckbox = LocatorsBuyingflow.BracketShippingtoaDiffrentadresCheckbox
        self.BracketOrderNotesInput = LocatorsBuyingflow.BracketOrderNotesInput
        self.BracketThankyoutext = LocatorsBuyingflow.BracketThankyoutext
        self.BracketPrintButton = LocatorsBuyingflow.BracketPrintButton
        self.BracketCouponInput = LocatorsBuyingflow.BracketCouponInput

        self.MainPageGenericShopbutton = LocatorsBuyingflow.MainPageGenericShopbutton

    def open_page(self):
        self.logger.info(" Navigate to url 'https://skleptest.pl'")
        self.driver.get('https://skleptest.pl/')
    def OrderingProcess(self):
        self.driver.find_element(By.XPATH, self.MainPageMyCartButton).click()
        #Bracket1
        self.driver.find_element(By.XPATH, self.BracketProduct1Quantityplusbutton).click()
        self.driver.find_element(By.XPATH, self.BracketProduct2Quantityplusbutton).click()
        self.driver.find_element(By.XPATH, self.BracketProduct1Quantityminusbutton).click()
        self.driver.find_element(By.XPATH, self.BracketProduct2Quantityminusbutton).click()
        self.driver.find_element(By.XPATH, self.BracketProduct2Quantityminusbutton).click()
        time.sleep(3)
        self.driver.find_element(By.NAME, self.BracketUpdatecartbutton).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.BracketProceedtoCheckoutButton).click()
        # Bracket2
        self.driver.find_element(By.XPATH, self.BracketFirstnameinput).click()
        self.driver.find_element(By.XPATH, self.BracketFirstnameinput).send_keys('Pedro Palo')
        self.driver.find_element(By.XPATH, self.BracketLastnameInput).click()
        self.driver.find_element(By.XPATH, self.BracketLastnameInput).send_keys('Palo Berło')
        self.driver.find_element(By.XPATH, self.BracketCompanyInput).click()
        self.driver.find_element(By.XPATH, self.BracketCompanyInput).send_keys('Pao Pao')
        self.driver.find_element(By.XPATH, self.BracketCountryListbutton).click()
        self.driver.find_element(By.XPATH, self.BracketCountryListSearchbar).click()
        self.driver.find_element(By.XPATH, self.BracketCountryListSearchbar).send_keys('United States')
        self.driver.find_element(By.XPATH, self.BracketCountryListSearchbar).send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.BracketStreetaddressInput).click()
        self.driver.find_element(By.XPATH, self.BracketStreetaddressInput).send_keys('Pao Pao')
        self.driver.find_element(By.XPATH, self.BracketStreetAddressOptionalInput).click()
        self.driver.find_element(By.XPATH, self.BracketStreetAddressOptionalInput).send_keys('Palo Belto')
        self.driver.find_element(By.XPATH, self.BracketTownInput).click()
        self.driver.find_element(By.XPATH, self.BracketTownInput).send_keys('Arizona')
        self.driver.find_element(By.XPATH, self.BracketStateListbutton).click()
        self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).click()
        self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).send_keys('Arizona')
        self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.BracketPhoneInput).click()
        self.driver.find_element(By.XPATH, self.BracketPhoneInput).send_keys('12312312')
        self.driver.find_element(By.XPATH, self.BracketZipCodeInput).click()
        self.driver.find_element(By.XPATH, self.BracketZipCodeInput).send_keys('86556')
        self.driver.find_element(By.XPATH, self.BracketPhoneInput).send_keys('12312312')
        self.driver.find_element(By.XPATH, self.BracketEmailInput).click()
        self.driver.find_element(By.XPATH, self.BracketEmailInput).send_keys('Fuenghini@Bengi.pl')
        self.driver.find_element(By.XPATH, self.BracketCreateAnAccountcheckbox).click()
        self.driver.find_element(By.XPATH, self.BracketCreateAnAccountPasswordInput).click()
        self.driver.find_element(By.XPATH, self.BracketCreateAnAccountPasswordInput).send_keys('1@#a!@#ABA')

        #self.driver.find_element(By.XPATH, self.BracketShippingtoaDiffrentadresCheckbox).click()
        #time.sleep(4)
        #self.driver.find_element(By.XPATH, self.BracketDiffrentAddressFistNameInput).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentAddressFistNameInput).send_keys('Bolo')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentAddressLastNameInput).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentAddressLastNameInput).send_keys('Boltno')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentAddressLastNameInput).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentAddressLastNameInput).send_keys('Boltno')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentCompanyNameinput).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentCompanyNameinput).send_keys('Boltno')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentCountryListbutton).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentCountryListSearchbar).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentCountryListSearchbar).send_keys('United States')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentCountryListSearchbar).send_keys(Keys.ENTER)
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStreetAddres).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStreetAddres).send_keys('Boltno')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStreetAddress2).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStreetAddress2).send_keys('Boltno')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentTownInput).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentTownInput).send_keys('chupa')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStateListButton).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).send_keys('Arizona')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).send_keys(Keys.ENTER)
        #self.driver.find_element(By.XPATH, self.BracketDiffrentPostCodeinput).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentPostCodeinput).send_keys('5465')
        #self.driver.find_element(By.XPATH, self.BracketDiffrentOrderNotes).click()
        #self.driver.find_element(By.XPATH, self.BracketDiffrentOrderNotes).send_keys('5465')


        self.driver.find_element(By.XPATH, self.BracketOrderNotesInput).click()
        self.driver.find_element(By.XPATH, self.BracketOrderNotesInput).send_keys('12312312')
        self.driver.find_element(By.XPATH, self.BracketCashOnDeliveryCheckbox).click()
        self.driver.find_element(By.XPATH, self.BracketPlaceOrderButton).click()
        element = self.driver.find_element(By.XPATH, self.BracketThankyoutext)
        if element.is_displayed():
            self.driver.find_element(By.XPATH, self.MainPageGenericShopbutton).click()
        #BacktoMainFunkcjazewnętrznadodostawienia


    def AddingProductsToBracket(self):
        self.logger.info(" Adding Products to bracket")
        self.driver.find_element(By.XPATH, self.MainPageBlackTopsProduct1AddtoCartButton).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.MainPageBlackTopsProduct2AddtoCartButton).click()
        time.sleep(3)

    def AddingProducttoBracketfromProductPage(self):
        self.logger.info(" Adding Products to bracket from Product Page")
        self.driver.find_element(By.XPATH, self.MainPageMostwantedCattegorybutton).click()
        self.driver.find_element(By.XPATH, self.MostwantedCategory1Product1Photo).click()
        self.driver.find_element(By.XPATH, self.ProductPageReviewButton).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.ProductPageDescriptionButton).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.ProductPageAddtocartButton).click()

    def AddProductfromTrendsCategoryMainpagetoBracket(self):
        self.logger.info(" Adding Products to bracket from Trends Category on Main Page")
        self.driver.find_element(By.XPATH, self.MainpageTrendsCategory1ProductAddtocart).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.MainpageTrendsCategory2ProductAddtocart).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.MainpageTrendsCategory3ProductAddtocart).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.MainpageTrendsCategory4ProductAddtocart).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.MainPageMyCartButton).click()
        assert self.driver.find_element(By.XPATH, self.BracketProduct4DeleteButton).is_displayed()
    def AddProductfromListMenuCategoryMainpagetoBracket(self):
        self.logger.info(" Adding Products to bracket from Trends Category on Main Page")
        actions = ActionChains(self.driver)
        Menubutton = self.driver.find_element(By.XPATH, self.MainPageCategoriesCategorylist)
        ShoesButton = self.driver.find_element(By.XPATH, self.MainPageCategoriesCategorylistShoes)
        actions.move_to_element(Menubutton).click(ShoesButton).perform()
        self.driver.find_element(By.XPATH, self.ShoesCattegoryProduct1AddtocartButton).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.MainPageMyCartButton).click()
        if self.driver.find_element(By.XPATH, self.BracketProduct2Quantityminusbutton).is_not_displayed():
            return True






    def OrderingwithLoggedUser(self):
        self.driver.find_element(By.XPATH, self.MainPageMyCartButton).click()
        # Bracket1
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.BracketProceedtoCheckoutButton).click()
        # Bracket2
        self.driver.find_element(By.XPATH, self.BracketFirstnameinput).click()
        self.driver.find_element(By.XPATH, self.BracketFirstnameinput).send_keys('Pedro Palo')
        self.driver.find_element(By.XPATH, self.BracketLastnameInput).click()
        self.driver.find_element(By.XPATH, self.BracketLastnameInput).send_keys('Palo Berło')
        self.driver.find_element(By.XPATH, self.BracketCompanyInput).click()
        self.driver.find_element(By.XPATH, self.BracketCompanyInput).send_keys('Pao Pao')
        self.driver.find_element(By.XPATH, self.BracketCountryListbutton).click()
        self.driver.find_element(By.XPATH, self.BracketCountryListSearchbar).click()
        self.driver.find_element(By.XPATH, self.BracketCountryListSearchbar).send_keys('United States')
        self.driver.find_element(By.XPATH, self.BracketCountryListSearchbar).send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.BracketStreetaddressInput).click()
        self.driver.find_element(By.XPATH, self.BracketStreetaddressInput).send_keys('Pao Pao')
        self.driver.find_element(By.XPATH, self.BracketStreetAddressOptionalInput).click()
        self.driver.find_element(By.XPATH, self.BracketStreetAddressOptionalInput).send_keys('Palo Belto')
        self.driver.find_element(By.XPATH, self.BracketTownInput).click()
        self.driver.find_element(By.XPATH, self.BracketTownInput).send_keys('Arizona')
        self.driver.find_element(By.XPATH, self.BracketStateListbutton).click()
        self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).click()
        self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).send_keys('Arizona')
        self.driver.find_element(By.XPATH, self.BracketDiffrentStateSearchBar).send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.BracketPhoneInput).click()
        self.driver.find_element(By.XPATH, self.BracketPhoneInput).send_keys('12312312')

        self.driver.find_element(By.XPATH, self.BracketZipCodeInput).click()
        input_element = self.driver.find_element(By.XPATH, self.BracketZipCodeInput)
        cell_value = input_element.get_attribute('value')
        if not cell_value:
            input_element.send_keys('86556')
        self.driver.find_element(By.XPATH, self.BracketPhoneInput).send_keys('1')
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.BracketCashOnDeliveryCheckbox).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.BracketPlaceOrderButton).click()
        time.sleep(6)
        element = self.driver.find_element(By.XPATH, self.BracketThankyoutext)
        if element.is_displayed():
            self.driver.find_element(By.XPATH, self.MainPageGenericShopbutton).click()










