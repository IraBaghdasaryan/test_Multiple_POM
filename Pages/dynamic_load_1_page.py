from Pages.base_page import BasePage
from Resource.Locators import *

class DynamicLoadex1(BasePage):
    def __init__(self,driver):
        self.driver=driver
        #http://the-internet.herokuapp.com/dynamic_loading/1


    def start_loading(self):
        self._click(Locators._dynamic_load1_start_button)


    def load(self):
        self._is_displayed(Locators._dynomic_load_ex1_submit)

    def finishload(self):

         self._is_displayed(Locators._dynamic_load1_finish_text)

    def successmessage(self):
        self._is_displayed(Locators._dynamic_load1_success)