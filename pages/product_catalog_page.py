import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductCatalogPage:

    product_image = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    product_name = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    product_price = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("OPEN PRODUCT CATALOG")
    def open_product(self):
        try:
            product = self.wait.until(EC.element_to_be_clickable(self.product_image))
            product.click()
            print("Product clicked successfully")

        except TimeoutException:
            raise AssertionError("Product not clickable within timeout.")
        except NoSuchElementException:
            raise AssertionError("Product not found on screen.")

    @allure.step("VERIFY PRODUCT DETAILS AND PRICE")
    def verify_product_details(self):
        try:
            name_element = self.wait.until(EC.visibility_of_element_located(self.product_name))
            price_element = self.wait.until(EC.visibility_of_element_located(self.product_price))

            name = name_element.text
            price = price_element.text

            print(f"Product Name: {name}")
            print(f"Product Price: {price}")

            return name, price

        except TimeoutException:
            raise AssertionError("Product name or price not visible within timeout.")
        except NoSuchElementException:
            raise AssertionError("Product name or price element not found on screen.")
