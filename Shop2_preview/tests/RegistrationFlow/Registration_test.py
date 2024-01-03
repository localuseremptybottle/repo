import pytest
from pages.RegistrationFlow import RegistrationScripts
from random import randint
import names


@pytest.mark.usefixtures("setup")

class Test:
    def test_RegistrationAccountPassed(self):
        email = str(randint(0, 1000)) + 'test@test.com'
        name = str(names.get_full_name(gender='male'))
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female'))
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        RegistrationElements.click_on_MyAccountButton()
        RegistrationElements.create_account_first_step(email,password)
        assert RegistrationElements.is_user_loged()
    def test_RegistrationAccountdenied(self):
        email = str(randint(0, 1000)) + 'ser@ser.pll'
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female'))
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        RegistrationElements.click_on_MyAccountButton()
        RegistrationElements.create_account_first_step(email,password)
        assert RegistrationElements.is_user_loged()