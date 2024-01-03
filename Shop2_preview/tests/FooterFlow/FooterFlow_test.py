import pytest
from pages.FooterFlow import FooterScripts
from pages.RegistrationFlow import RegistrationScripts
from Utils import Basetest

@pytest.mark.usefixtures("setup")
class Test:

    def test_TryOpenTagsonMainpage(self):
        FooterElements = FooterScripts(self.driver)
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        FooterElements.try_open_all_tags()
    def test_TryOpenAllRecentPostonMainpage(self):
        FooterElements = FooterScripts(self.driver)
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        FooterElements.try_open_all_RecentPost()
    def test_IsAboutTextVisible(self):
        FooterElements = FooterScripts(self.driver)
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        assert FooterElements.is_About_Text_visible_on_footer()
    def test_Verify_Subscription_in_home_page_Passed(self):
        FooterElements = FooterScripts(self.driver)
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        assert FooterElements.Verify_Subscription_in_home_page_Passed()