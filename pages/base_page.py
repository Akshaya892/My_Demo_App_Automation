from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_type, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((locator_type, locator))
        )

    def click(self, locator_type, locator):
        self.wait_for_element(locator_type, locator).click()

    def send_keys(self, locator_type, locator, text):
        element = self.wait_for_element(locator_type, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator_type, locator):
        return self.wait_for_element(locator_type, locator).text
