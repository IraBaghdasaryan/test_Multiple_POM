from selenium.webdriver import Chrome
import pytest
from Pages import login_page


class TestLogin():
    @pytest.fixture
    def login(self, request):
        driver_ = Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return login_page.LoginPage(driver_)

    def test_invalid_wrong_pass(self, login):
        login.with_("tomsmith", "Not very super password!")
        assert login.failure_message_present() == True

    def test_invalid_wrond_username(self, login):
        login.with_("TomSmith", "SuperSecretePassword!")
        assert login.failure_message_present() == True

    def test_invalid_empty (self, login):
        login.with_("","")
        assert login.failure_message_present() == True


