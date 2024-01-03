from random import randint
import names
import pytest
from pages.BuyingFlow import BuyingFLowScripts
from pages.RegistrationFlow import RegistrationScripts
from pages.MyAccountFlow import MyAccountScripts

@pytest.mark.usefixtures("setup")

class Test:

    def test_PlaceOrderWithoutLogin(self):
        Buyingflowelements = BuyingFLowScripts(self.driver)
        Buyingflowelements.open_page()
        Buyingflowelements.AddingProductsToBracket()
        Buyingflowelements.OrderingProcess()
        MyOrdersElements = MyAccountScripts(self.driver)
        MyOrdersElements.VerifyOrdersTab()
    def test_PlaceOrderLoginBeforeCheckout(self):
        email = str(randint(0, 1000)) + 'ser@ser.pl'
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female'))
        Buyingflowelements = BuyingFLowScripts(self.driver)
        Buyingflowelements.open_page()
        Buyingflowelements.AddingProductsToBracket()
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.create_account_first_step(email,password)
        Buyingflowelements.OrderingwithLoggedUser()
    def test_PlaceOrderRegistryWhileCheckout(self):
        email = str(randint(0, 1000)) + 'ser@ser.pl'
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female'))
        Buyingflowelements = BuyingFLowScripts(self.driver)
        Buyingflowelements.open_page()
        Buyingflowelements.AddingProductsToBracket()
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.create_account_first_step(email,password)
        Buyingflowelements.OrderingwithLoggedUser()
    def test_AddProductfromProductCardtoBracket(self):
        Buyingflowelements = BuyingFLowScripts(self.driver)
        Buyingflowelements.open_page()
        Buyingflowelements.AddingProducttoBracketfromProductPage()
    def test_AddProductfromTrendsCategoryMainpagetoBracket(self):
        Buyingflowelements = BuyingFLowScripts(self.driver)
        Buyingflowelements.open_page()
        Buyingflowelements.AddProductfromTrendsCategoryMainpagetoBracket()

    @pytest.mark.xfail
    def test_AddProductfromListMenuCategoryMainpagetoBracket(self):
        Buyingflowelements = BuyingFLowScripts(self.driver)
        Buyingflowelements.open_page()
        Buyingflowelements.AddProductfromListMenuCategoryMainpagetoBracket()



