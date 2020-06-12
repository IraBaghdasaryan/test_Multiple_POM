from Pages.base_page import BasePage
from Resource.Locators import *

class HomePage(BasePage):
    def __init__(self,driver):
        self.driver=driver
        #self._visit("http://the-internet.herokuapp.com/")

    def successful_homepage(self):
        return self._is_displayed(Locators._homepage_welcome)

    def go_to__authentication(self):
        return self._click(Locators._homepage_login_button)

    def go_to__dynamicload(self):
        return self._click(Locators._homepage_dynamicload_button)
