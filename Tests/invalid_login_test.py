from selenium import webdriver
driver = webdriver.Chrome()


def test_valid_credentials():
    driver.get("http://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").send_keys("tomsmith")
    driver.find_element_by_id("password").send_keys("SuperSecretPassword!")
    driver.find_element_by_css_selector('#login > button > i').click()

    assert (driver.find_element_by_id("flash"))
    text_error = driver.find_element_by_id("flash").text
    assert text_error == "Your password is invalid!"



