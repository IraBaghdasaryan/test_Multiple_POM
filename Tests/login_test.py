from selenium.webdriver import Chrome
import pytest
from Pages import login_page
import time


class TestLogin():
    @pytest.fixture
    def login(self, request):
        driver_ = Chrome()

        def quit():
            driver_.quit()
        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_valid(self, login):
        login.with_("tomsmith","SuperSecretPassword!")
        assert login.success_message_present() == True

    def test_logout_page(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        time.sleep(3)
        login.logout_from()
        assert login.successful_logout() == True

    def test_invalid_wrong_pass(self, login):
        login.with_("tomsmith", "Not very super password!")
        assert login.failure_message_present() == True

    def test_invalid_wrond_username(self, login):
        login.with_("TomSmith", "SuperSecretePassword!")
        assert login.failure_message_present() == True

    def test_invalid_empty (self, login):
        login.with_("","")
        assert login.failure_message_present() == True



