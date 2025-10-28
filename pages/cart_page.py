import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CartPage:

    product_image = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    add_to_cart = (AppiumBy.ACCESSIBILITY_ID, "Tap to add product to cart")
    cart_icon = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
    cart_page_title = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    display_cart = (AppiumBy.ACCESSIBILITY_ID, "Displays selected product")
    cart_info = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/infoCL")
    remove_cart = (AppiumBy.ACCESSIBILITY_ID, "Removes product from cart")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("PRODUCT ADD TO CART")
    def open_product(self):
        try:
            product = self.wait.until(EC.element_to_be_clickable(self.product_image))
            product.click()
            print("Product clicked successfully")

            add_cart = self.wait.until(EC.element_to_be_clickable(self.add_to_cart))
            add_cart.click()

        except TimeoutException:
            raise AssertionError("Failed to add product to cart")
        except NoSuchElementException:
            raise AssertionError("Element is not found")

    @allure.step("VERIFY CART PAGE")
    def verify_cart_page(self):
        try:
            # Open the cart
            cart_icon = self.wait.until(EC.element_to_be_clickable(self.cart_icon))
            cart_icon.click()

            # Validate title, info, and remove button
            wait = WebDriverWait(self.driver, 10)
            title = self.wait.until(EC.presence_of_element_located(self.cart_page_title))
            info = self.wait.until(EC.presence_of_element_located(self.cart_info))
            remove_btn = self.wait.until(EC.presence_of_element_located(self.remove_cart))

            print("Title", title)
            print("Cart info displayed successfully", info)
            print("Remove button visible", remove_btn)


        except TimeoutException:
            raise AssertionError("Cart page elements not visible within timeout.")
        except NoSuchElementException:
            raise AssertionError("Cart page elements not found on screen.")
