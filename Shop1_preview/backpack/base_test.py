import pytest

#options = Options()
#options.add_experimental_option('detach',True)

from allure_commons.types import AttachmentType
import allure
from backpack.driver_factory import DriverFactory


class BaseTest:
    @pytest.fixture()
    def setupd(self,request):
        self.driver = DriverFactory.get_driver("chrome")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        request.cls.driver = self.driver
        before_failed = request.session.testsfailed
        yield
        if request.session.testsfailed != before_failed:
            allure.attach(self.driver.get_screenshot_as_png(), name="Test Failed", attachment_type=AttachmentType.PNG)
        self.driver.quit()