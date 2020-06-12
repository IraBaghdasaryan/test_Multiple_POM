from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, inpute_test):
        self._find(locator).send_keys(inpute_test)

    def _is_displayed(self, locator):
        return self._find(locator).is_displayed()

    #def _displayed_after_wait(self, locator, timeout=0):
        #if timeout>0:
            #try:
                #wait = WebDriverWait(self.driver, timeout)
                #wait.until(
                    #expected_conditions.visibility_of_element_located(
                        #(locator['by'], locator['value'])))
            #except TimeoutException:
                #return False
            #return True
        #else:
            #try:
                #return self._find(locator).is_displayed()
            #except NoSuchElementException:
                #return False


