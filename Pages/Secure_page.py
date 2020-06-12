from Pages.base_page import BasePage
from Resource.Locators import *

class SecurePage(BasePage):

    def __init__(self, driver):
        self.driver=driver
        #self._visit("http://the-internet.herokuapp.com/secure")

    def logout_from(self):
        self._click(Locators._logout_button)

    def success_message_present(self):
        return self._is_displayed(Locators._success_message)

    def successful_logout(self):
        return self._is_displayed(Locators._login_form)
