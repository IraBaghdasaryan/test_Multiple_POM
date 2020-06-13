import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.Secure_page import SecurePage
from Pages.home_page import HomePage
from Pages.dynamic_loading_page import DynamicLoad
from Pages.dynamic_load_1_page import DynamicLoadex1
import time


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def testloginlogout(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        home_pg = HomePage(self.driver)
        login_pg = LoginPage(self.driver)
        secure_pg = SecurePage(self.driver)
        assert home_pg.successful_homepage()
        home_pg.go_to__authentication()
        login_pg.with_("tomsmith", "SuperSecretPassword!")
        assert secure_pg.success_message_present() == True
        secure_pg.logout_from()
        assert secure_pg.successful_logout() == True
        self.driver.get("http://the-internet.herokuapp.com/")
        dynamic_pg = DynamicLoad(self.driver)
        dynamic_pg1 = DynamicLoadex1(self.driver)
        home_pg.go_to__dynamicload()
        dynamic_pg.successful_load_page()
        dynamic_pg.go_to_example1()
        dynamic_pg1.load()
        dynamic_pg1.start_loading()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        print("Test complete!")

if __name__ == '__main__':
    unittest.main()