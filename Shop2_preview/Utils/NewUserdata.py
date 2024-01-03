import pytest
import logging
from pages.RegistrationFlow import RegistrationScripts
from random import randint
import names

class Userdata:
    # test do sprawdzania logowania

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
    def NewUserData(self):
        email = str(randint(0, 1000)) + 'test@test.com'
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female'))
        RegistrationElements = RegistrationScripts(self.driver)
        RegistrationElements.open_page()
        RegistrationElements.click_on_MyAccountButton()
        RegistrationElements.create_account_first_step(email, password)

        assert RegistrationElements.is_user_loged()

        user = dict()
        user['email'] = email
        user['password'] = password

        return user
