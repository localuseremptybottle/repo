#PageObjectPattern

import logging
import os.path
import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import MyAccountPagelocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains





class Myaccountpage:    #Tutaj sa łączone lokatory w metodzie init, bo je bedziemy przekazywac do log in
    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.signin_button = MyAccountPagelocators.sign_up_button
        self.hooveradv = MyAccountPagelocators.button_main_page_adv
        self.iframe = MyAccountPagelocators.iframe_element

        # Mainpage
        self.MainPage_Loggedtext = MyAccountPagelocators.Loggedinastext
        self.MainPage_Deletebutton = MyAccountPagelocators.deleteaccountbutton
        self.MainPage_Deleteaccounttext = MyAccountPagelocators.deleteaccounttext
        self.MainPage_Logoutbutton = MyAccountPagelocators.Logoutbutton
        self.MainPage_Feauturesitemstext = MyAccountPagelocators.Feautersitemstext
        self.MainPage_Contactusbutton = MyAccountPagelocators.contactusbutton
        self.MainPage_Homebutton = MyAccountPagelocators.homebutton
        self.MainPage_TestCasesButton = MyAccountPagelocators.testcasesbutton
        self.MainPage_ProductsButton = MyAccountPagelocators.ProductsButton
        self.MainPage_Footer = MyAccountPagelocators.Footer
        self.MainPage_Subscriptiontext = MyAccountPagelocators.Subsricptiontext
        self.MainPage_SubscriptionEmailInput = MyAccountPagelocators.SubscriptionEmailInput
        self.MainPage_SubscriptionEmailSuccess = MyAccountPagelocators.SubscriptionEmailInputSucces
        self.MainPage_CartButton = MyAccountPagelocators.Cart_Button
        self.MainPage_ViewButton= MyAccountPagelocators.MainPageViewButton
        self.MainPage_CattegoryBardiv = MyAccountPagelocators.CategoryBar
        self.Mainpage_WomanCattegoryButton = MyAccountPagelocators.WomanCategorybutton
        self.Mainpage_SareCategoryButton = MyAccountPagelocators.SareCategoryButton
        self.Mainpage_TopsCategoryButton = MyAccountPagelocators.TopsCategoryButton
        self.Mainpage_WomanTopsproductstext = MyAccountPagelocators.WomanTopsProductsText
        self.Mainpage_Mancattegorybutton = MyAccountPagelocators.MenCategoryButton
        self.Mainpage_MenTshirtsProductstext = MyAccountPagelocators.MenTshirtsProductstext
        self.Mainpage_MansubcattegoryTshirtsbutton = MyAccountPagelocators.MensubcategoryTshirtsbutton
        self.Mainpage_Brandtext= MyAccountPagelocators.Brandstext
        self.Mainpage_BrandSubCattegoryPolo = MyAccountPagelocators.BrandSubCategoryPoloButton
        self.Mainpage_BranSubCategoryPoloUrl = MyAccountPagelocators.BranSubCategoryPoloUrl
        self.Mainpage_BrandSubCattegoryPoloProduct1img = MyAccountPagelocators.BrandSubCategoryPoloProduct1img
        self.Mainpage_BrandSubCategoryMadameButton = MyAccountPagelocators.BrandSubCategoryMadameButton
        self.Mainpage_BrandSubCategoryMadameUrl= MyAccountPagelocators.BrandSubCategoryMadameUrl
        self.Mainpage_BrandSubCategoryMadameProduct1img = MyAccountPagelocators.BrandSubCategoryMadameProduct1img
        self.Mainpage_Recommended_Items_text =MyAccountPagelocators.Recommended_Items_text
        self.Mainpage_Recommended_Items_Add_to_cart = MyAccountPagelocators.Recommended_Items_Add_to_cart
        self.Mainpage_Scrollupbutton = MyAccountPagelocators.Scrollupbutton
        self.Mainpage_FullFledgedPracticewebsiteforAutomationEngineerstext = MyAccountPagelocators.FullFledgedPracticewebsiteforAutomationEngineerstext


        #Signup Panel / Login module
        self.login_input = MyAccountPagelocators.SignupPanel_login_input
        self.password_input = MyAccountPagelocators.SignupPanel_password_login_input
        self.Loginisincorrecttext = MyAccountPagelocators.SignupPanel_Emailisincorrect_text

        #Signup Panel / Registration module
        self.regname = MyAccountPagelocators.reg_name_input
        self.reg_email_input = MyAccountPagelocators.reg_mail_input
        self.radiobuttonmr = MyAccountPagelocators.reg_radio_button_Mr
        self.radiobuttonmrs = MyAccountPagelocators.reg_radio_button_Mrs
        self.regname2 = MyAccountPagelocators.reg_name_input2
        self.regpassword = MyAccountPagelocators.reg_password_input
        self.dateofbirthselect = MyAccountPagelocators.reg_date_of_birth
        self.monthofbirthselect = MyAccountPagelocators.reg_month_of_birth
        self.yearofbirthselect = MyAccountPagelocators.reg_year_of_birth
        self.newslettercheckbox = MyAccountPagelocators.reg_newslettercheckbox
        self.specialofferscheckbox = MyAccountPagelocators.reg_specialoffercheckbox
        self.createbutton = MyAccountPagelocators.create_button
        self.Emailexisttext = MyAccountPagelocators.emailaddressalreadyexist_text

        #2stepregInformations
        self.firstname = MyAccountPagelocators.reg_firstname_input
        self.lastname = MyAccountPagelocators.reg_lastname_input
        self.company = MyAccountPagelocators.reg_company_input
        self.addres1 = MyAccountPagelocators.reg_address_input
        self.addres2 = MyAccountPagelocators.reg_address2_input
        self.countryselect = MyAccountPagelocators.reg_country_list
        self.state = MyAccountPagelocators.reg_state_input
        self.city = MyAccountPagelocators.reg_city_input
        self.zipcode = MyAccountPagelocators.reg_zipcode_input
        self.mobilephone = MyAccountPagelocators.reg_mobilephone_input

        #3stepregComplete
        self.Account_text_created = MyAccountPagelocators.account_text_created
        self.Continuebutton = MyAccountPagelocators.continuebutton

        #Products
        self.Feauturesitemsdiv = MyAccountPagelocators.Products_featueresitemsdiv
        self.ViewProductButton = MyAccountPagelocators.Products_viewproduct
        self.Searchbar = MyAccountPagelocators.Products_Searchbar
        self.SearchbarButton = MyAccountPagelocators.Products_Searchbutton
        self.SearchedProductsText = MyAccountPagelocators.Products_SearchedProductsText
        self.AddToCart1 = MyAccountPagelocators.Products_AddToCart1
        self.AddToCart2 = MyAccountPagelocators.Products_AddToCart2
        self.Products_Searched_Addtocart1 = MyAccountPagelocators.Products_Searched_Addtocart1
        self.Products_Searched_Addtocart2 = MyAccountPagelocators.Products_Searched_Addtocart2
        self.ContinueShoppingButton = MyAccountPagelocators.Products_ContinueShoppingbutton
        self.ViewCart = MyAccountPagelocators.Products_ViewCart
        self.Products_url = MyAccountPagelocators.Products_url

        #ProductCard
        self.Productcard_Name = MyAccountPagelocators.Productcard_productname
        self.Productcard_Category = MyAccountPagelocators.Productcard_categoryname
        self.Productcard_Price = MyAccountPagelocators.Productcard_price
        self.Productcard_Quantity = MyAccountPagelocators.Productcard_quantity
        self.Productcard_Quantitytestinput = MyAccountPagelocators.Productcard_quantity_4
        self.Productcard_Quantityinput = MyAccountPagelocators.Productcard_quantity_input
        self.Productcard_Condition = MyAccountPagelocators.Productcard_condition
        self.Productcard_Brand = MyAccountPagelocators.Productcard_brand
        self.Productcard_Addtocard = MyAccountPagelocators.Productcard_AddtoCartButton
        self.Productcard_ReviewNameInput = MyAccountPagelocators.Productcard_ReviewNameInput
        self.Productcard_ReviewEmailInput = MyAccountPagelocators.Productcard_ReviewEmailInput
        self.Productcard_ReviewTextInput = MyAccountPagelocators.Productcard_ReviewTextInput
        self.Productcard_ReviewSubmitButton = MyAccountPagelocators.Productcard_ReviewSubmitButton
        self.Productcard_ReviewThankyoutext = MyAccountPagelocators.Productcard_ReviewThankyoutext

        #ShoppingCart
        self.ShoppingCart_Secondproduct = MyAccountPagelocators.ShoppingCart_Second_Product
        self.ShoppingCart_Firstprice = MyAccountPagelocators.ShoppingCart_First_Price
        self.ShoppingCart_Secondprice = MyAccountPagelocators.Shoppingcart_Second_Price
        self.ShoppingCart_FirstQuantity= MyAccountPagelocators.Shoppingcart_First_Quantity
        self.ShoppingCart_SecondQuantity = MyAccountPagelocators.Shoppingcart_Second_Quantity
        self.ShoppingCart_FirstTotalPrice = MyAccountPagelocators.Shoppingcart_First_TotalPrice
        self.ShoppingCart_SecondTotalPrice = MyAccountPagelocators.Shoppingcart_Second_TotalPrice
        self.Shoppingcart_ProcceedButton = MyAccountPagelocators.Shoppingcart_ProceedToCheckoutbutton
        self.Shoppingcart_RegisterLoginbutton = MyAccountPagelocators.Shoppingcart_RegisterLoginButton
        self.Shoppingcart_DeleteButton1 = MyAccountPagelocators.Shoppingcart_DeleteButton1
        self.Shoppingcart_DeleteButton2 = MyAccountPagelocators.Shoppingcart_DeleteButton2
        self.Shoppingcart_CartIsEmpty_text = MyAccountPagelocators.Shoppingcart_CartIsEmpty_text
        self.Shoppingcart_url  = MyAccountPagelocators.Shoppingcart_url
        #ShoppingCart#2
        self.Shoppingcart_TextInput =MyAccountPagelocators.Shoppingcart_Textareainput
        self.Shoppingcart_First_name = MyAccountPagelocators.Shoppingcart_First_name
        self.Shoppingcart_LastName= MyAccountPagelocators.Shoppingcart_LastName
        self.Shoppingcart_Address1 = MyAccountPagelocators.Shoppingcart_Address1
        self.Shoppingcart_Address2 = MyAccountPagelocators.Shoppingcart_Address2
        self.Shoppingcart_Address_city = MyAccountPagelocators.Shoppingcart_Address_city
        self.Shoppingcart_State_name = MyAccountPagelocators.Shoppingcart_State_name
        self.Shoppingcart_postcode = MyAccountPagelocators.Shoppingcart_postcode
        self.Shoppingcart_mobilephone = MyAccountPagelocators.Shoppingcart_mobilephone
        self.Shoppingcart_PlaceOrderButton = MyAccountPagelocators.Shoppingcart_PlaceorderButton
        self.Shoppingcart_Billingaddress_First_name =MyAccountPagelocators.Shoppingcart_Billingaddress_First_name
        self.Shoppingcart_Billingaddress_LastName = MyAccountPagelocators.Shoppingcart_Billingaddress_LastName
        self.Shoppingcart_Billingaddress_Address1 =MyAccountPagelocators.Shoppingcart_Billingaddress_Address1
        self.Shoppingcart_Billingaddress_Address2 = MyAccountPagelocators.Shoppingcart_Billingaddress_Address2
        self.Shoppingcart_Billingaddress_Address_city = MyAccountPagelocators.Shoppingcart_Billingaddress_Address_city
        self.Shoppingcart_Billingaddress_State_name = MyAccountPagelocators.Shoppingcart_Billingaddress_State_name
        self.Shoppingcart_Billingaddress_postcode = MyAccountPagelocators.Shoppingcart_Billingaddress_postcode
        self.Shoppingcart_Billingaddress_mobilephone = MyAccountPagelocators.Shoppingcart_Billingaddress_mobilephone
        #Payment
        self.Payment_NameoncardInput = MyAccountPagelocators.Payment_NameoncardInput
        self.Payment_Cardnumberinput = MyAccountPagelocators.Payment_Cardnumberinput
        self.Payment_CVC_input = MyAccountPagelocators.Payment_CVC_input
        self.Payment_ExpirationMM_input = MyAccountPagelocators.Payment_ExpirationMM_input
        self.Payment_ExpirationYY_input = MyAccountPagelocators.Payment_ExpirationYY_input
        self.Payment_ConfirmOrder_Button = MyAccountPagelocators.Payment_ConfirmOrder_Button
        self.Payment_CongratulatonText = MyAccountPagelocators.Payment_CongratulatonText
        self.Payment_DownloadInvoiceButton = MyAccountPagelocators.Payment_DownloadInvoiceButton
        self.Payment_ContinueButton = MyAccountPagelocators.Payment_ContinueButton

        #Contactsuspage
        self.Contactusform_Getintouchtext = MyAccountPagelocators.ContactForm_Getintouchtext
        self.Contactformnameinput = MyAccountPagelocators.ContactForm_Name_input
        self.Contactformemailinput = MyAccountPagelocators.ContactForm_email_input
        self.Contactformsubjectinput = MyAccountPagelocators.ContactForm_subject_input
        self.Contactformmessageinput = MyAccountPagelocators.ContactForm_Message_input
        self.Contactformwybierzplikbutton = MyAccountPagelocators.ContactForm_Wybierzplik_button
        self.ContactformSubmitbutton = MyAccountPagelocators.Contactform_Submitbutton
        self.ContactformSuccesstext = MyAccountPagelocators.Contactform_Successtext
        self.ContactformHomebuttton = MyAccountPagelocators.Contactform_Homebutton

        #TestCases
        self.TestcasesText = MyAccountPagelocators.testcasestext

        #Others
        self.Logo = MyAccountPagelocators.Logo_xpath
        self.Newusertext = MyAccountPagelocators.new_user_signup_text
        self.Enteraccountinfotext = MyAccountPagelocators.enter_account_info_text
        self.Logintoyouraccounttext = MyAccountPagelocators.login_to_your_account_text



    def open_page(self):
        self.logger.info(" Navigate to url 'http://automationexercise.com'")
        self.driver.get('http://automationexercise.com')

    def switch_to_frame(self):
        self.logger.info(" Adv. Scripts ")
        self.driver.implicitly_wait(3)
        self.driver.execute_script("arguments[0].style.display = 'none';",self.driver.find_element(By.TAG_NAME,self.iframe))
        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

        # Loop through each iframe and set display style to "none"
        for iframe in iframes:
            self.driver.execute_script("arguments[0].style.display = 'none';", iframe)

        inselement = self.driver.find_elements(By.TAG_NAME, "ins")
        for ins in inselement:
            self.driver.execute_script("arguments[0].style.display = 'none';", ins)

        fulladv = self.driver.find_elements(By.TAG_NAME, "ad_position_box")
        for ins in inselement:
            self.driver.execute_script("arguments[0].style.display = 'none';", ins)

        Advertisement = self.driver.find_elements(By.TAG_NAME, "Advertisement")
        for ins in inselement:
            self.driver.execute_script("arguments[0].style.display = 'none';", ins)


    def log_in(self,email,password):
        self.driver.find_element(By.XPATH,self.login_input).send_keys(email)
        self.driver.find_element(By.XPATH,self.password_input).send_keys(password)
        self.driver.find_element(By.XPATH,self.password_input).send_keys(Keys.ENTER)

    def create_account_first_step(self,name,email):
        self.logger.info("6. Enter name and email address")
        self.driver.find_element(By.XPATH, self.regname).send_keys(name)
        self.driver.find_element(By.XPATH, self.reg_email_input).send_keys(email)
        self.driver.find_element(By.XPATH, self.reg_email_input).send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    def create_account_second_step(self,name,password):
        self.logger.info("9. Fill details: Title, Name, Email, Password, Date of birth")
        self.driver.find_element(By.XPATH, self.radiobuttonmrs).click()
        self.driver.find_element(By.XPATH, self.regname2).send_keys(name)
        self.driver.find_element(By.XPATH, self.regpassword).send_keys(password)
        dayofbirth_select = Select(self.driver.find_element(By.XPATH,self.dateofbirthselect))
        dayofbirth_select.select_by_visible_text('15')
        monthofbirth_select = Select(self.driver.find_element(By.XPATH, self.monthofbirthselect))
        monthofbirth_select.select_by_visible_text('July')
        yearofbirth_select = Select(self.driver.find_element(By.XPATH, self.yearofbirthselect))
        yearofbirth_select.select_by_visible_text('2000')

        self.driver.find_element(By.XPATH, self.newslettercheckbox).click()
        self.driver.find_element(By.XPATH, self.specialofferscheckbox).click()
        self.driver.find_element(By.XPATH, self.firstname).send_keys('John')
        self.driver.find_element(By.XPATH, self.lastname).send_keys('John')
        self.driver.find_element(By.XPATH, self.company).send_keys('John')
        self.driver.find_element(By.XPATH, self.addres1).send_keys('John')
        self.driver.find_element(By.XPATH, self.addres2).send_keys('John')
        self.driver.find_element(By.XPATH, self.state).send_keys('John')
        self.driver.find_element(By.XPATH, self.city).send_keys('John')
        self.driver.find_element(By.XPATH, self.zipcode).send_keys('44444')
        self.driver.find_element(By.XPATH, self.mobilephone).send_keys('123123123')


    def SendContactusform(self,name,email,subject,message):
        self.logger.info("6. Enter name, email, subject and message")
        file = os.path.abspath(r"C:\Users\ST\PycharmProjects\Allegropreview\pages\image.webp")
        self.driver.find_element(By.XPATH, self.Contactformnameinput).click()
        self.driver.find_element(By.XPATH, self.Contactformnameinput).send_keys(name)
        self.driver.find_element(By.XPATH, self.Contactformemailinput).click()
        self.driver.find_element(By.XPATH, self.Contactformemailinput).send_keys(email)
        self.driver.find_element(By.XPATH, self.Contactformsubjectinput).click()
        self.driver.find_element(By.XPATH, self.Contactformsubjectinput).send_keys(subject)
        self.driver.find_element(By.XPATH, self.Contactformmessageinput).click()
        self.driver.find_element(By.XPATH, self.Contactformmessageinput).send_keys(message)
        self.switch_to_frame()
        self.driver.find_element(By.XPATH, self.Contactformwybierzplikbutton).send_keys(file)
        self.driver.find_element(By.XPATH, self.ContactformSubmitbutton).click()
    def Searching_with_Products_Searchbar(self,productname):
        self.logger.info("Enter product name in search input and click search button")
        self.driver.find_element(By.XPATH, self.Searchbar).click()
        self.driver.find_element(By.XPATH, self.Searchbar).send_keys(productname)
        self.driver.find_element(By.XPATH, self.SearchbarButton).click()
    def Jump_to_Footer(self):
        self.logger.info("Jump to Footer")
        self.driver.find_element(By.XPATH, self.MainPage_Footer).click()
    def Try_Subscription_Email_Input(self,email):
        self.logger.info("Enter Email to Subscription Email Input")
        self.driver.find_element(By.ID, self.MainPage_SubscriptionEmailInput).click()
        self.driver.find_element(By.ID, self.MainPage_SubscriptionEmailInput).send_keys(email)
        self.driver.find_element(By.ID, self.MainPage_SubscriptionEmailInput).send_keys(Keys.ENTER)

    def Write_Review_in_Product_card(self):
        self.logger.info("Enter Email to Subscription Email Input")
        name = 'John'
        email ='email@email.com'
        review = 'John review'
        self.driver.find_element(By.XPATH, self.Productcard_ReviewNameInput).click()
        self.driver.find_element(By.XPATH, self.Productcard_ReviewNameInput).send_keys(name)
        self.driver.find_element(By.XPATH, self.Productcard_ReviewEmailInput).click()
        self.driver.find_element(By.XPATH, self.Productcard_ReviewEmailInput).send_keys(email)
        self.driver.find_element(By.XPATH, self.Productcard_ReviewTextInput).click()
        self.driver.find_element(By.XPATH, self.Productcard_ReviewTextInput).send_keys(review)



    def click_on_Addtocart_on_Recommendeditems(self):
        self.logger.info("click on (Add to card) button in Recommended items")
        self.driver.find_element(By.XPATH, self.Mainpage_Recommended_Items_Add_to_cart).click()
    def click_on_ContinueButton_in_PaymentCard(self):
        self.logger.info("click on (Continue Button ) in Payment")
        self.driver.find_element(By.XPATH, self.Payment_ContinueButton).click()
    def click_on_Submit_Review_in_ProductCard(self):
        self.logger.info("click on (Submit_Review) in ProductCard")
        self.driver.find_element(By.XPATH, self.Productcard_ReviewSubmitButton).click()
    def click_on_Woman_Category(self):
        self.logger.info("Click 'Woman Category' Button")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Mainpage_WomanCattegoryButton).click()
    def click_on_Sare_Category(self):
        self.logger.info("Click 'Sare Category' Button")
        self.driver.find_element(By.XPATH, self.Mainpage_SareCategoryButton).click()
    def click_on_Tops_Category(self):
        self.logger.info("Click 'Tops' Button")
        self.driver.find_element(By.XPATH, self.Mainpage_TopsCategoryButton).click()
    def click_on_Men_Category(self):
        self.logger.info("Click 'Men'category Button")
        self.driver.find_element(By.XPATH, self.Mainpage_Mancattegorybutton).click()
    def click_on_Men_Tshirts_subCategory(self):
        self.logger.info("Click 'Tshirts' subcategory Button")
        self.driver.find_element(By.XPATH, self.Mainpage_MansubcattegoryTshirtsbutton).click()
    def click_on_Brands_Polo_subCategory(self):
        self.logger.info("Click 'Polo' subcategory Button")
        self.driver.find_element(By.XPATH, self.Mainpage_BrandSubCattegoryPolo).click()
    def click_on_Brands_Madame_subCategory(self):
        self.logger.info("Click 'Madame' subcategory Button")
        self.driver.find_element(By.XPATH, self.Mainpage_BrandSubCategoryMadameButton).click()
    def click_on_ProceedToCheckout(self):
        self.logger.info("Click 'Proceed To Checkout' Button")
        self.driver.find_element(By.XPATH, self.Shoppingcart_ProcceedButton).click()

    def click_on_RegistryLoginButtoninShoppingcart(self):
        self.logger.info("Click 'Registry/Login' Button in Shopping Cart")
        self.driver.find_element(By.XPATH, self.Shoppingcart_RegisterLoginbutton).click()

    def click_on_Product_Quantity_input(self):
        self.logger.info("Click 'Quantity' Input")
        self.driver.find_element(By.XPATH, self.Productcard_Quantityinput).click()
        self.driver.find_element(By.XPATH, self.Productcard_Quantityinput).clear()
        self.driver.find_element(By.XPATH, self.Productcard_Quantityinput).send_keys(4)

    def click_on_AddtoCard_in_ProductCard(self):
        self.logger.info("Click 'Add to Card' Input")
        self.driver.find_element(By.XPATH, self.Productcard_Addtocard).click()

    def click_on_Continue_Shoping(self):
        self.logger.info("Click 'Continue Shopping' button")
        self.driver.find_element(By.XPATH, self.ContinueShoppingButton).click()

    def click_on_Add_to_Cart1(self):
        self.logger.info("Click 'Add to Cart' button")
        self.driver.find_element(By.XPATH, self.AddToCart1).click()

    def click_on_Add_to_Cart2(self):
        self.logger.info("Click 'Add to Cart second product' button")
        self.driver.find_element(By.XPATH, self.AddToCart2).click()

    def click_on_searched_AddtoCart1and2(self):
        self.logger.info("Click on searched products 'Add to Cart 1 & 2' button")
        self.driver.find_element(By.XPATH, self.Products_Searched_Addtocart1).click()
        self.driver.find_element(By.XPATH, self.ContinueShoppingButton).click()
        self.driver.find_element(By.XPATH, self.Products_Searched_Addtocart2).click()
    def click_on_Delete_for_Product1_in_shopping_cart(self):
        self.logger.info("Click 'Delete' button in Shopping Cart for product 1")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Shoppingcart_DeleteButton1).click()
    def click_on_Delete_for_Product2_in_shopping_cart(self):
        self.logger.info("Click 'Delete' button in Shopping Cart for product 2")
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.Shoppingcart_DeleteButton2).click()
    def click_on_view_cart(self):
        self.logger.info("Click 'ViewCart' button")
        self.driver.find_element(By.LINK_TEXT, self.ViewCart).click()

    def click_on_Download_Invoice(self):
        self.logger.info("Click 'Download Invoice' button")
        self.driver.find_element(By.XPATH, self.Payment_DownloadInvoiceButton).click()

    def click_on_Cart_Button(self):
        self.logger.info("Click 'Cart Button' button")
        self.driver.find_element(By.LINK_TEXT, self.MainPage_CartButton).click()

    def click_on_Testcases(self):
        self.logger.info("Click 'Test Cases' button")
        self.driver.find_element(By.XPATH, self.MainPage_TestCasesButton).click()

    def click_on_ViewButton(self):
        self.logger.info("Click 'View' button")
        self.driver.find_element(By.XPATH, self.ViewProductButton).click()

    def click_on_DeleteAccountButton(self):
        self.logger.info("Click 'Delete Account' button")
        self.driver.find_element(By.XPATH, self.MainPage_Deletebutton).click()

    def click_on_Signupbutton(self):
        self.logger.info("Click on 'Signup / Login' button")
        self.driver.find_element(By.XPATH, self.signin_button).click()

    def click_on_createbutton(self):
        self.logger.info('Click "Create Account button"')
        self.driver.find_element(By.XPATH,self.createbutton).click()

    def click_on_logoutbutton(self):
        self.logger.info('Click "Logout Button"')
        self.driver.find_element(By.XPATH,self.MainPage_Logoutbutton).click()

    def click_on_Continuebutton(self):
        self.logger.info("Click 'Continue' button")
        self.driver.find_element(By.XPATH, self.Continuebutton).click()

    def click_on_Contactusbutton(self):
        self.logger.info("Click 'Contactsus' button")
        self.driver.find_element(By.XPATH, self.MainPage_Contactusbutton).click()

    def click_on_home_Button(self):
        self.logger.info("Click 'Home' button")
        self.driver.find_element(By.LINK_TEXT, self.ContactformHomebuttton).click()

    def click_on_Products_Button(self):
        self.logger.info("Click 'Products' button")
        self.driver.find_element(By.XPATH, self.MainPage_ProductsButton).click()

    def click_on_MainPage_View_Button(self):
        self.logger.info("Click 'View Product' button")
        self.driver.find_element(By.LINK_TEXT, self.MainPage_ViewButton).click()
    def click_on_TextArea_in_Shoppingcart(self):
        self.logger.info("Click 'View Text area' and write text")
        msng = 'Place order asap'
        self.driver.find_element(By.XPATH, self.Shoppingcart_TextInput).click()
        self.driver.find_element(By.XPATH, self.Shoppingcart_TextInput).send_keys(msng)
    def click_on_PlaceOrderButton_in_ShoppingCart(self):
        self.logger.info("Click 'PlaceOrder' button")
        self.driver.find_element(By.XPATH, self.Shoppingcart_PlaceOrderButton).click()

    def click_on_Scrollup_button(self):
        self.logger.info("Click 'Scrollup' button")
        self.driver.find_element(By.XPATH, self.Mainpage_Scrollupbutton).click()
        time.sleep(5)
    def Scroll_down_Script(self):
        self.logger.info("Click 'Scrolldown' script")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    def Scroll_Up_Script(self):
        self.logger.info("Przesuń stronę do góry")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    def Complete_the_entire_payment_form(self):
        self.logger.info("Click 'Name on Card' input")
        Nameoncard = 'Belita Auten'
        Cardnumber = '5363688784083992'
        CVC = '387'
        Expirationdate = '02'
        Expirationyear =  '2026'

        self.driver.find_element(By.XPATH, self.Payment_NameoncardInput).click()
        self.driver.find_element(By.XPATH, self.Payment_NameoncardInput).send_keys(Nameoncard)
        self.driver.find_element(By.XPATH, self.Payment_Cardnumberinput).click()
        self.driver.find_element(By.XPATH, self.Payment_Cardnumberinput).send_keys(Cardnumber)
        self.driver.find_element(By.XPATH, self.Payment_CVC_input).click()
        self.driver.find_element(By.XPATH, self.Payment_CVC_input).send_keys(CVC)
        self.driver.find_element(By.XPATH, self.Payment_ExpirationMM_input).click()
        self.driver.find_element(By.XPATH, self.Payment_ExpirationMM_input).send_keys(Expirationdate)
        self.driver.find_element(By.XPATH, self.Payment_ExpirationYY_input).click()
        self.driver.find_element(By.XPATH, self.Payment_ExpirationYY_input).send_keys(Expirationyear)
        self.driver.find_element(By.XPATH, self.Payment_ConfirmOrder_Button).click()


    #AssertionMethods


    def is_accountdeletedtextis_displayed(self):
        self.logger.info("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button")
        return self.driver.find_element(By.XPATH, self.MainPage_Deleteaccounttext).is_displayed()
    def is_loggedasis_displayed(self):
        self.logger.info("Verify that 'Logged in as username' is visible")
        return self.driver.find_element(By.XPATH, self.MainPage_Loggedtext).is_displayed()
    def is_textaccountcreated_displayed(self):
        self.logger.info("Verify that 'ACCOUNT CREATED!' is visible")
        return self.driver.find_element(By.XPATH, self.Account_text_created).is_displayed()
    def is_logo_dsplayed(self):
        self.logger.info("Verify that home page is visible successfully")
        return self.driver.find_element(By.XPATH, self.Logo).is_displayed()
    def is_NewUserSignup_displayed(self):
        self.logger.info("Verify 'New User Signup!' is visible")
        return self.driver.find_element(By.XPATH, self.Newusertext).is_displayed
    def is_Logintoyouraccount_displayed(self):
        self.logger.info("Verify 'Login to your Account!' is visible")
        return self.driver.find_element(By.XPATH, self.Logintoyouraccounttext).is_displayed
    def is_Loginisincorrect_displayed(self):
        self.logger.info("Your email or password is incorrect!' is visible")
        return self.driver.find_element(By.XPATH, self.Loginisincorrecttext).is_displayed
    def is_Enter_accountinformation_displayed(self):
        self.logger.info("Verify that 'ENTER ACCOUNT INFORMATION' is visible")
        return self.driver.find_element(By.XPATH, self.Enteraccountinfotext).is_displayed
    def is_Featuresitems_displayed(self):
        self.logger.info("Verify that 'Features items' is visible")
        return self.driver.find_element(By.XPATH, self.MainPage_Feauturesitemstext).is_displayed
    def is_EmailAddressalreadyexist_displayed(self):
        return self.driver.find_element(By.XPATH, self.Emailexisttext).is_displayed
    def is_Getintouch_displayed(self):
        return self.driver.find_element(By.XPATH, self.Contactusform_Getintouchtext).is_displayed
    def is_Successtext_displayed(self):
        self.logger.info("Success text is displayed")
        return self.driver.find_element(By.XPATH, self.ContactformSuccesstext).is_displayed()
    def is_Testcasestext_displayed(self):
        self.logger.info("Testcases text is displayed")
        return self.driver.find_element(By.XPATH, self.TestcasesText).is_displayed()
    def is_featuresitemsdiv_displayed(self):
        self.logger.info("Testcases text is displayed")
        return self.driver.find_element(By.CLASS_NAME, self.Feauturesitemsdiv).is_displayed()
    def Areyousurepopup(self):
        self.driver.switch_to.alert.accept()
    def is_ProductName_displayed(self):
        self.logger.info("Verify that detail detail is visible: product name")
        return self.driver.find_element(By.XPATH, self.Productcard_Name).is_displayed()
    def is_CategoryInformation_displayed(self):
        self.logger.info("Verify that detail detail is visible: category")
        return self.driver.find_element(By.XPATH, self.Productcard_Category).is_displayed()
    def is_PriceInformation_displayed(self):
        self.logger.info("Verify that detail detail is visible: price")
        return self.driver.find_element(By.XPATH, self.Productcard_Price).is_displayed()
    def is_QuantityInformation_displayed(self):
        self.logger.info("Verify that detail detail is visible: availability")
        return self.driver.find_element(By.XPATH, self.Productcard_Quantity).is_displayed()
    def is_QuantitytestInformation_displayed(self):
        self.logger.info("Verify test quantity is visible")
        return self.driver.find_element(By.XPATH, self.Productcard_Quantitytestinput).is_displayed()
    def is_ConditionInformation_displayed(self):
        self.logger.info("Verify that detail detail is visible: condition")
        return self.driver.find_element(By.XPATH, self.Productcard_Condition).is_displayed()
    def is_BrandInformation_displayed(self):
        self.logger.info("Verify that detail detail is visible: brand")
        return self.driver.find_element(By.XPATH, self.Productcard_Brand).is_displayed()
    def is_SearchedProducts_displayed(self):
        self.logger.info("7. Verify 'SEARCHED PRODUCTS' is visible")
        return self.driver.find_element(By.XPATH, self.SearchedProductsText).is_displayed()
    def is_SubscriptionText_displayed(self):
        self.logger.info("Verify text 'SUBSCRIPTION'")
        return self.driver.find_element(By.XPATH, self.MainPage_Subscriptiontext).is_displayed()
    def is_SubscriptionSuccessText_displayed(self):
        self.logger.info("Verify text 'SUBSCRIPTION Success'")
        return self.driver.find_element(By.XPATH, self.MainPage_SubscriptionEmailSuccess).is_displayed()
    def is_ShoppingCart_SecondProduct_displayed(self):
        self.logger.info("Verify is Second Product in Shopping card displayed'")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_Secondproduct).is_displayed()
    def is_ShoppingCart_FirstPrice_displayed(self):
        self.logger.info("Verify text 'First Price' is visible")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_Firstprice).is_displayed()
    def is_ShoppingCart_SecondPrice_displayed(self):
        self.logger.info("Verify text 'Second Price' is visible")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_Secondprice).is_displayed()
    def is_ShoppingCart_FirstQuantity_displayed(self):
        self.logger.info("Verify text 'First Quantity' is visible")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_FirstQuantity).is_displayed()
    def is_ShoppingCart_SecondQuantity_displayed(self):
        self.logger.info("Verify text 'Second Quantity' is visible")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_SecondQuantity).is_displayed()
    def is_ShoppingCart_FirstTotalPrice_displayed(self):
        self.logger.info("Verify text 'First TotalPrice' is visible")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_FirstTotalPrice).is_displayed()
    def is_ShoppingCart_SecondTotalPrice_displayed(self):
        self.logger.info("Verify text 'Second TotalPrice' is visible")
        return self.driver.find_element(By.XPATH, self.ShoppingCart_SecondTotalPrice).is_displayed()
    def is_AddressInShoppingCard_correct(self):
        self.logger.info("is Address1 In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Address1).is_displayed()
    def is_Address2inShoppingCard_correct(self):
        self.logger.info("is Address2 In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Address2).is_displayed()
    def is_Address_cityinShoppingCard_correct(self):
        self.logger.info("is Address_city In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Address_city).is_displayed()
    def is_State_nameinShoppingCard_correct(self):
        self.logger.info("is State_name In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_State_name).is_displayed()
    def is_postcodeinShoppingCard_correct(self):
        self.logger.info("is Postcode In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_postcode).is_displayed()
    def is_mobilephoneinShoppingCard_correct(self):
        self.logger.info("is Mobilephone In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_mobilephone).is_displayed()
    def is_First_nameinShoppingCard_correct(self):
        self.logger.info("is First_name In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_First_name).is_displayed()
    def is_Second_nameinShoppingCard_correct(self):
        self.logger.info("is Second_name In ShoppingCard correct")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_LastName).is_displayed()
    def is_CongratulationText_in_Paymanet_displayed(self):
        self.logger.info("is 'Congratulations!your order has been confirmed' displayed")
        return self.driver.find_element(By.XPATH, self.Payment_CongratulatonText).is_displayed()
    def is_CartIsEmpty_text_in_Shoppingcart_displayed(self):
        self.logger.info("is 'Cart Is Empty' text in Shoppingcart displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_CartIsEmpty_text).is_displayed()
    def is_CategoryBar_in_MainPain_displayed(self):
        self.logger.info("is 'CategoryBar' div in MainPage displayed")
        return self.driver.find_element(By.XPATH, self.MainPage_CattegoryBardiv).is_displayed()
    def is_WomanTopProducts_in_MainPage_displayed(self):
        self.logger.info("is 'WomanTopProducts' div in MainPage displayed")
        return self.driver.find_element(By.XPATH, self.Mainpage_WomanTopsproductstext).is_displayed()
    def is_MenTshirtsProductstext_in_Mainpage_displayed(self):
        self.logger.info("is 'Men Tshirts Producsts' text in MainPage displayed")
        return self.driver.find_element(By.XPATH, self.Mainpage_MenTshirtsProductstext).is_displayed()
    def is_BrandcategoryText_in_Mainpage_displayed(self):
        self.logger.info("is 'Brand' Category  in MainPage displayed")
        return self.driver.find_element(By.XPATH, self.Mainpage_Brandtext).is_displayed()
    def is_Polo_Address_Category_is_Correct(self):
        self.logger.info("is 'Polo url' displayed")
        current_url_address = self.driver.current_url
        return current_url_address == self.Mainpage_BranSubCategoryPoloUrl
    def is_Madame_Address_Category_is_Correct(self):
        self.logger.info("is 'Madame url' displayed")
        current_url_address = self.driver.current_url
        return current_url_address == self.Mainpage_BrandSubCategoryMadameUrl
    def is_ImageOfProduct1_in_PoloCategory_displayed(self):
        self.logger.info("is 'Image of product1' in Polo subcategory displayed")
        return self.driver.find_element(By.XPATH, self.Mainpage_BrandSubCattegoryPoloProduct1img).is_displayed()
    def is_ImageOfProduct1_in_MadameCategory_displayed(self):
        self.logger.info("is 'Image of product1' in Polo subcategory displayed")
        return self.driver.find_element(By.XPATH, self.Mainpage_BrandSubCategoryMadameProduct1img).is_displayed()
    def is_Products_Address_Correct(self):
        self.logger.info("is 'Products url' is correct")
        current_url_address = self.driver.current_url
        return current_url_address == self.Products_url
    def is_ShoppingCart_Address_Correct(self):
        self.logger.info("is 'Products url' is correct")
        current_url_address = self.driver.current_url
        return current_url_address == self.Shoppingcart_url
    def is_Thankyoutext_after_Submited_review_displayed(self):
        self.logger.info("is 'Thank you for your Review' text displayed")
        return self.driver.find_element(By.XPATH, self.Productcard_ReviewThankyoutext).is_displayed()
    def is_RecommendedItemstext_displayed(self):
        self.logger.info("is 'Thank you for your Review' text displayed")
        return self.driver.find_element(By.XPATH, self.Mainpage_Recommended_Items_text).is_displayed()
    def is_Name_in_BillingAddress_displayed(self):
        self.logger.info("is 'Name' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_First_name).is_displayed()
    def is_LastName_in_BillingAddress_displayed(self):
        self.logger.info("is 'Last name' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_LastName).is_displayed()
    def is_Address1_in_BillingAddress_displayed(self):
        self.logger.info("is 'Address1' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_Address1).is_displayed()
    def is_Address2_in_BillingAddress_displayed(self):
        self.logger.info("is 'Address2' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_Address2).is_displayed()
    def is_AddressCity_in_BillingAddress_displayed(self):
        self.logger.info("is 'Address City ' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_Address_city).is_displayed()
    def is_StateName_in_BillingAddress_displayed(self):
        self.logger.info("is 'State Name' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_State_name).is_displayed()
    def is_Postcode_in_BillingAddress_displayed(self):
        self.logger.info("is 'State Name' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_postcode).is_displayed()
    def is_MobilePhone_in_BillingAddress_displayed(self):
        self.logger.info("is 'State Name' in Billing address displayed")
        return self.driver.find_element(By.XPATH, self.Shoppingcart_Billingaddress_mobilephone).is_displayed()
    def is_Fullflegdgedtext_inMainpage_displayed(self):
        self.logger.info("is 'FullFledgedPracticewebsiteforAutomationEngineerstext' in Mainpage disable")
        wait = WebDriverWait(self.driver, 4)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Mainpage_FullFledgedPracticewebsiteforAutomationEngineerstext)))
        if element.is_displayed():
            return True
