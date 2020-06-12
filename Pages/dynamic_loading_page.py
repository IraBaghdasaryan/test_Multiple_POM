from Pages.base_page import BasePage
from Resource.Locators import *

class DynamicLoad(BasePage):
    def __init__(self,driver):
        self.driver=driver
        #http://the-internet.herokuapp.com/dynamic_loading

    def successful_load_page(self):
        self._is_displayed(Locators._dynamically_load_form)

    def go_to_example1(self):
        self._click(Locators._dynamic_load_ex1_button)




