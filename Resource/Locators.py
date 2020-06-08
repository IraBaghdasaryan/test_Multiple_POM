from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class Locators:
    _login_form = {"by": By.ID, "value": "login"}
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "#login > button"}
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}
    _logout_button = {"by": By.CSS_SELECTOR, "value": "#content > div > a"}
    _success_logout = {"by": By.CLASS_NAME, "value": "flash success"}


