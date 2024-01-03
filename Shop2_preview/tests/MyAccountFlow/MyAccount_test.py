import pytest
from pages.MyAccountFlow import MyAccountScripts
from pages.BuyingFlow import BuyingFLowScripts
from Utils.BackToMain import BacktoMainclass
from Utils.JumptoMyAccount import JumptoMyAccountClass



@pytest.mark.usefixtures("setup")
class Test:
    def test_MyAccount_Dashboardtab_verification(self):
        MyAccountElements = MyAccountScripts(self.driver)
        MyAccountElements.open_page()
        MyAccountElements.create_account()
        MyAccountElements.VerifyDashboardtab()

    def test_LoginUserwithincorrectpassword(self):
        MyAccountElements = MyAccountScripts(self.driver)
        MyAccountElements.open_page()
        MyAccountElements.LogintoAccountWithWrongPassword()
        assert MyAccountElements.is_ErrorIncorectPasswordtext_inMyAccount_displayed()
    def test_LoginUserwithincorrectemail(self):
        MyAccountElements = MyAccountScripts(self.driver)
        MyAccountElements.open_page()
        MyAccountElements.LogintoAccountWithWrongEmail()
        assert MyAccountElements.is_ErrorIncorecteEmailtext_inMyAccount_displayed()
    def test_RecorveryEmailProces(self):
        MyAccountElements = MyAccountScripts(self.driver)
        MyAccountElements.open_page()
        MyAccountElements.RecorveryyourAccount()
    def test_Historyofbuying(self):
        MyAccountElements = MyAccountScripts(self.driver)
        MyAccountElements.open_page()
        MyAccountElements.create_account()

        UntilisAddon1 = BacktoMainclass(self.driver)
        UntilisAddon1.BackToMain()

        BuyingFlowElements = BuyingFLowScripts(self.driver)
        BuyingFlowElements.AddingProductsToBracket()
        BuyingFlowElements.OrderingwithLoggedUser()
        UntilisAddon1.BackToMain()
        BuyingFlowElements.AddingProductsToBracket()
        BuyingFlowElements.OrderingwithLoggedUser()

        UntilisAddon2 = JumptoMyAccountClass(self.driver)
        UntilisAddon2.JumptoMyAccount()

        MyAccountElements.VerifyOrdersTab()



