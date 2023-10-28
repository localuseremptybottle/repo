from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class MyAccountPagelocators:
    #Signup Panel / Login side
    SignupPanel_login_input = '//*[@id="form"]/div/div/div[1]/div/form/input[2]'
    SignupPanel_password_login_input ="//*[@id='form']/div/div/div[1]/div/form/input[3]"
    SignupPanel_login_button = "//*[@id='form']/div/div/div[1]/div/form/button"
    SignupPanel_Emailisincorrect_text = '//*[@id="form"]/div/div/div[1]/div/form/p'
    #Signup Panel / Registration side
    reg_name_input = "//*[@id='form']/div/div/div[3]/div/form/input[2]"
    reg_mail_input = "//*[@id='form']/div/div/div[3]/div/form/input[3]"
    emailaddressalreadyexist_text ='//*[@id="form"]/div/div/div[3]/div/form/p'
    #2stepreg
    reg_radio_button_Mr = "//*[@id='id_gender1']"
    reg_radio_button_Mrs = '//*[@id="id_gender2"]'
    reg_name_input2 = '//*[@id="name"]'
    reg_password_input = '//*[@id="password"]'
    reg_date_of_birth = '//*[@id="days"]'
    reg_month_of_birth = '//*[@id="months"]'
    reg_year_of_birth = '//*[@id="years"]'
    reg_newslettercheckbox = '//*[@id="newsletter"]'
    reg_specialoffercheckbox = '//*[@id="optin"]'
    reg_firstname_input =   '//*[@id="first_name"]'
    reg_lastname_input = '//*[@id="last_name"]'
    reg_company_input = '//*[@id="company"]'
    reg_address_input = '//*[@id="address1"]'
    reg_address2_input = '//*[@id="address2"]'
    reg_country_list = '//*[@id="country"]'
    reg_state_input = '//*[@id="state"]'
    reg_city_input = '//*[@id="city"]'
    reg_zipcode_input = '//*[@id="zipcode"]'
    reg_mobilephone_input = '//*[@id="mobile_number"]'
    create_button = '//*[@id="form"]/div/div/div/div/form/button'
    #Accountcreated
    account_text_created = '//*[@id="form"]/div/div/div/h2/b'
    continuebutton = '//*[@id="form"]/div/div/div/div/a'
    #Others
    button_main_page_adv = "/html/body/ins[2]/div[1]//ins/span"
    iframe_element = "iframe"
    new_user_signup_text = '//*[@id="form"]/div/div/div[3]/div/h2'
    login_to_your_account_text = "//*[@id='form']/div/div/div[1]/div/h2"
    enter_account_info_text = '//*[@id="form"]/div/div/div/div/h2/b'
    sign_up_button = "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"
    Logo_xpath = "//*[@id='header']/div/div/div/div[1]/div/a/img"
    #Mainpage
    Loggedinastext =  "//a[contains(text(),'Logged in as')]"
    deleteaccountbutton = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a'
    deleteaccounttext = '//*[@id="form"]/div/div/div/h2/b'
    Logoutbutton = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
    Feautersitemstext = '/html/body/section[2]/div/div/div[2]/div[1]/h2'
    contactusbutton = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a'
    homebutton = '/html/body/header/div/div/div/div[2]/div/ul/li[1]/a'
    categorytext = '/html/body/section[2]/div/div/div[1]/div/h2/b'
    testcasesbutton = '/html/body/header/div/div/div/div[2]/div/ul/li[5]/a'
    ProductsButton = '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a'
    Footer = '/html/body/footer'
    Subsricptiontext =' /html/body/footer/div[1]/div/div/div[2]/div/h2'
    SubscriptionEmailInput = 'susbscribe_email'
    SubscriptionEmailInputSucces = '/html/body/footer/div[1]/div/div/div[1]/div/div'
    Cart_Button = 'Cart'
    MainPageViewButton = 'View Product'
    CategoryBar = "//div[@class='panel-group category-products' and @id='accordian']"
    WomanCategorybutton = '//*[@id="accordian"]/div[1]/div[1]/h4/a'
    SareCategoryButton = '//*[@id="Women"]/div/ul/li[3]/a'
    TopsCategoryButton = '//*[@id="Women"]/div/ul/li[2]/a'
    WomanTopsProductsText = "//h2[@class='title text-center' and text()='Women - Tops Products']"
    MenTshirtsProductstext = "//h2[@class='title text-center' and text()='Men - Tshirts Products']"
    MenCategoryButton = '//*[@id="accordian"]/div[2]/div[1]/h4/a'
    MensubcategoryTshirtsbutton = '//*[@id="Men"]/div/ul/li[1]/a'
    Brandstext = "//h2[text()='Brands']"
    BrandSubCategoryPoloButton = '//li/a[text()="Polo"]'
    BrandSubCategoryMadameButton = '//li/a[text()="Madame"]'
    BranSubCategoryPoloUrl = "https://automationexercise.com/brand_products/Polo"
    BrandSubCategoryMadameUrl = 'https://automationexercise.com/brand_products/Madame'
    BrandSubCategoryPoloProduct1img ='//img[@src="/get_product_picture/1"]'
    BrandSubCategoryMadameProduct1img = '//img[@src="/get_product_picture/3"]'
    Recommended_Items_text = '//h2[@class="title text-center" and text()="recommended items"]'
    Recommended_Items_Add_to_cart = '//div[@class="carousel-inner"]//a[@class="btn btn-default add-to-cart" and @data-product-id="1"]'
    Scrollupbutton = '//*[@id="scrollUp"]'
    FullFledgedPracticewebsiteforAutomationEngineerstext ='//h2[contains(text(), "Full-Fledged practice website for Automation Engineers")]'

    #Products
    Products_featueresitemsdiv = 'features_items'
    Products_viewproduct = '//li/a[text()="View Product"]'
    Products_Searchbar = '/html/body/section[1]/div/input'
    Products_Searchbutton = '/html/body/section[1]/div/button'
    Products_SearchedProductsText = '//h2[text()="Searched Products"]'
    Products_url = 'https://automationexercise.com/products'
    Products_AddToCart1 = '/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a'
    Products_AddToCart2 = '/html/body/section[2]/div/div/div[2]/div[1]/div[3]/div/div[1]/div[1]/a'
    Products_Searched_Addtocart1 = '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a'
    Products_Searched_Addtocart2 = '/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a'
    Products_ContinueShoppingbutton = '/html/body/section[2]/div/div/div[2]/div[1]/div[1]/div/div/div[3]/button'
    Products_ViewCart = 'View Cart'


    #ProductCard
    Productcard_AddtoCartButton = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button'
    Productcard_productname = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/img[1]'
    Productcard_categoryname = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]'
    Productcard_price = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span'
    Productcard_quantity = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/label'
    Productcard_quantity_4 = "//button[text()='4']" #wygenerowany
    Productcard_quantity_input = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/input[1]'
    Productcard_condition = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]/b'
    Productcard_brand = '/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]/b'
    Productcard_ReviewNameInput ='//*[@id="name"]'
    Productcard_ReviewEmailInput ='//*[@id="email"]'
    Productcard_ReviewTextInput = '//*[@id="review"]'
    Productcard_ReviewSubmitButton = '//*[@id="button-review"]'
    Productcard_ReviewThankyoutext = '//span[contains(text(), "Thank you for your review.")]'

    #ShoppingCart
    ShoppingCart_Second_Product    =  '/html/body/section/div/div[2]/table/tbody/tr[2]'
    ShoppingCart_First_Price       =  '/html/body/section/div/div[2]/table/tbody/tr[1]/td[3]/p'
    Shoppingcart_Second_Price      =  '/html/body/section/div/div[2]/table/tbody/tr[2]/td[3]/p'
    Shoppingcart_First_Quantity    =  '/html/body/section/div/div[2]/table/tbody/tr[1]/td[4]/button'
    Shoppingcart_Second_Quantity   =  '/html/body/section/div/div[2]/table/tbody/tr[2]/td[4]/button'
    Shoppingcart_First_TotalPrice  =  '/html/body/section/div/div[2]/table/tbody/tr[1]/td[5]/p'
    Shoppingcart_Second_TotalPrice =  '/html/body/section/div/div[2]/table/tbody/tr[2]/td[5]/p'
    Shoppingcart_ProceedToCheckoutbutton = '//*[@id="do_action"]/div[1]/div/div/a'
    Shoppingcart_RegisterLoginButton = '//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a'
    Shoppingcart_CartIsEmpty_text ='//*[contains(text(),"Cart is empty")]'
    Shoppingcart_url = 'https://automationexercise.com/view_cart'
    #ShoppingCart/2
    Shoppingcart_Textareainput = ' //*[@id="ordermsg"]/textarea'
    Shoppingcart_First_name = "//li[contains(@class,'address_firstname') and contains(text(),'John')]"
    Shoppingcart_LastName = "//li[contains(@class,'address_lastname') and contains(text(),'John')]"
    Shoppingcart_Address1= "//li[contains(@class,'address_address1') and contains(text(),'John')]"
    Shoppingcart_Address2 = "//li[contains(@class,'address_address2') and contains(text(),'John')]"
    Shoppingcart_Address_city = "//li[contains(@class,'address_city') and contains(text(),'John')]"
    Shoppingcart_State_name = "//li[contains(@class,'address_state_name') and contains(text(),'John')]"
    Shoppingcart_postcode = "//li[contains(@class,'address_postcode') and contains(text(),'44444')]"
    Shoppingcart_mobilephone ="//li[contains(@class,'address_phone') and contains(text(),'123123123')]"
    Shoppingcart_PlaceorderButton = '//*[@id="cart_items"]/div/div[7]/a'
    Shoppingcart_DeleteButton1 = '//*[@id="product-1"]/td[6]/a'
    Shoppingcart_DeleteButton2 = '//*[@id="product-2"]/td[6]/a'
    Shoppingcart_Billingaddress_First_name = "//ul[@class='address alternate_item box']/li[contains(text(), 'John')]"
    Shoppingcart_Billingaddress_LastName = "//ul[@class='address alternate_item box']/li[contains(text(), 'John')]"
    Shoppingcart_Billingaddress_Address1 = "//ul[@class='address alternate_item box']/li[contains(text(), 'John')][3]"
    Shoppingcart_Billingaddress_Address2 = "//ul[@class='address alternate_item box']/li[contains(text(), 'John')][4]"
    Shoppingcart_Billingaddress_Address_city = "//ul[@class='address alternate_item box']/li[contains(text(), 'John')][5]"
    Shoppingcart_Billingaddress_State_name = "//ul[@class='address alternate_item box']/li[contains(text(), 'India')]"
    Shoppingcart_Billingaddress_postcode ="//ul[@class='address alternate_item box']/li[contains(text(), '44444')]"
    Shoppingcart_Billingaddress_mobilephone ="//ul[@class='address alternate_item box']/li[contains(text(), '123123123')]"

    #Payment
    Payment_NameoncardInput ='//*[@id="payment-form"]/div[1]/div/input'
    Payment_Cardnumberinput ='//*[@id="payment-form"]/div[2]/div/input'
    Payment_CVC_input = '//*[@id="payment-form"]/div[3]/div[1]/input'
    Payment_ExpirationMM_input = '//*[@id="payment-form"]/div[3]/div[2]/input'
    Payment_ExpirationYY_input = '//*[@id="payment-form"]/div[3]/div[3]/input'
    Payment_ConfirmOrder_Button = '//*[@id="submit"]'
    Payment_CongratulatonText = '//p[text()="Congratulations! Your order has been confirmed!"]'
    Payment_DownloadInvoiceButton = '//*[@id="form"]/div/div/div/a'
    Payment_ContinueButton = '//*[@id="form"]/div/div/div/div/a'





    #TestCases
    testcasestext ='/html/body/section/div/div[1]/div/h2/b'


    #ContactusForm
    ContactForm_Getintouchtext = "//*[@id='contact-page']/div[2]/div[1]/div/h2"
    ContactForm_Name_input = '//*[@id="contact-us-form"]/div[1]/input'
    ContactForm_email_input = '//*[@id="contact-us-form"]/div[2]/input'
    ContactForm_subject_input = '//*[@id="contact-us-form"]/div[3]/input'
    ContactForm_Message_input = '//*[@id="message"]'
    ContactForm_Wybierzplik_button = "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[5]/input"
    Contactform_Submitbutton = '//*[@id="contact-us-form"]/div[6]/input'
    Contactform_Successtext = '//*[@id="contact-page"]/div[2]/div[1]/div/div[2]'
    Contactform_Homebutton ='Home'

class BillingaddressLocators:

    reg_email_input = (By.ID, "reg_email")
    reg_password_input = (By.ID, "reg_password")
    addresses_link= (By.LINK_TEXT, "Addresses")
    edit_link = (By.LINK_TEXT, "Edit")
    first_name_input = (By.ID, "billing_first_name")
    last_name_input =  (By.ID, "billing_last_name")
    billing_country_select = (By.ID, "billing_country")
    billing_address_input = (By.ID,'billing_address_1')
    billing_postcode_input = (By.ID, "billing_postcode")
    billing_city_input = (By.ID, "billing_city")
    billing_phone_input = (By.ID, "billing_phone")
    save_address_button = (By.NAME, 'save_address')
    message_div = (By.XPATH, "//div[@class='woocommerce-message']")


