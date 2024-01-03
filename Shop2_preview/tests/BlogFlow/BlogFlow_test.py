import pytest
from pages.BlogFlow import BlogPageScripts
from pages.RegistrationFlow import RegistrationScripts
from Utils.BackToMain import BacktoMainclass
from random import randint
import names

@pytest.mark.usefixtures("setup")
class Test:
    def test_ViewBlogPage(self):
        BlogPageElements = BlogPageScripts(self.driver)
        BlogPageElements.Open_Main_Page()
        BlogPageElements.Click_on_BlogTab_button()
        assert BlogPageElements.is_Blog_Address_Correct()
    def test_Find_Post_and_comment_without_Log_in(self):
        BlogPageElements = BlogPageScripts(self.driver)
        BlogPageElements.Open_Main_Page()
        BlogPageElements.Click_on_BlogTab_button()
        assert BlogPageElements.is_Blog_Address_Correct()
        BlogPageElements.Find_Post_and_open()
        BlogPageElements.CommentPostwithoutLoggedUser()
    def test_Find_Post_and_comment_with_Log_in(self):
        email = str(randint(0, 1000)) + 'test@test.com'
        password = str(randint(0, 1000)) + str(names.get_full_name(gender='female'))
        RegistrationElements = RegistrationScripts(self.driver)
        BlogPageElements = BlogPageScripts(self.driver)
        BackToMainelement = BacktoMainclass(self.driver)

        RegistrationElements.open_page()
        RegistrationElements.create_account_first_step(email,password)
        BlogPageElements.Open_Main_Page()
        BlogPageElements.Click_on_BlogTab_button()
        assert BlogPageElements.is_Blog_Address_Correct()
        BlogPageElements.Find_Post_and_open()
        BlogPageElements.CommentPostwithLoggedUser()
        BackToMainelement.BackToMain()

