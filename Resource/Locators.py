from selenium.webdriver.common.by import By


class Locators:
    _login_form = {"by": By.ID, "value": "login"}
    _username_input = {"by": By.ID, "value": "username"}
    _password_input = {"by": By.ID, "value": "password"}
    _submit_button = {"by": By.CSS_SELECTOR, "value": "#login > button"}
    _success_message = {"by": By.CSS_SELECTOR, "value": ".flash.success"}
    _failure_message = {"by": By.CSS_SELECTOR, "value": ".flash.error"}
    _logout_button = {"by": By.CSS_SELECTOR, "value": "#content > div > a"}
    _success_logout = {"by": By.CLASS_NAME, "value": "flash success"}
    _dropdown_list ={"by": By.ID, "value": "dropdown"}
    _homepage_welcome={"by":By.CSS_SELECTOR, "value":"#content > h1"}
    _homepage_login_button={"by":By.CSS_SELECTOR,"value":"#content > ul > li:nth-child(21) > a"}
    _homepage_dynamicload_button={"by":By.CSS_SELECTOR, "value":"#content > ul > li:nth-child(14) > a"}
    _dynamically_load_form={"by":By.CSS_SELECTOR,"value":"#content > div > h3"}
    _dynamic_load_ex1_button={"by":By.CSS_SELECTOR, "value":"#content > div > a:nth-child(5)"}
    _dynamic_load_ex2_button = {"by": By.CSS_SELECTOR, "value": "#content > div > a:nth-child(8)"}
    _dynomic_load_ex1_submit = {"by":By.CSS_SELECTOR, "value": "#content > div"}
    _dynamic_load1_start_button={"by":By.CSS_SELECTOR, "value":"#start > button"}
    _dynamic_load1_finish_text={"by":By.ID,"value":"finish"}
    _dynamic_load1_success={"by":By.CSS_SELECTOR, "value": "#finish > h4"}