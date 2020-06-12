from Pages.base_page import BasePage
from Resource.Locators import *


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver=driver
        #self._visit("http://the-internet.herokuapp.com/login")

    def with_(self, username, password):
        self._type(Locators._username_input, username)
        self._type(Locators._password_input, password)
        self._click(Locators._submit_button)

    def success_message_present(self):
        return self._is_displayed(Locators._success_message)

    def failure_message_present(self):
        return self._is_displayed(Locators._failure_message)






