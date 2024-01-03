import pytest
from pages.ContactFormFlow import ContactFormScripts


@pytest.mark.usefixtures("setup")

class Test:
    def test_Contactformdenied(self):
        ContactFormElements = ContactFormScripts(self.driver)
        ContactFormElements.open_page()
        ContactFormElements.click_on_ContactButton()
        ContactFormElements.FillContactForm()
        assert ContactFormElements.is_ErrorText_displayed()
