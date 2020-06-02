
from selenium.webdriver import Chrome

driver = Chrome()
driver.get("http://the-internet.herokuapp.com/login");


username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")


login1 = driver.find_element_by_css_selector('#login > button > i')

login1.click()
