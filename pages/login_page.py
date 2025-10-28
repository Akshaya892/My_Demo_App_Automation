import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:
    view_menu = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    login_button = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    username_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/username1TV")
    password_field = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/password1TV")
    login_btn = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
    logout_btn = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("OPEN VIEW MENU")
    def open_login_menu(self):
        try:
            menu = self.wait.until(EC.element_to_be_clickable(self.view_menu))
            menu.click()

            login_option = self.wait.until(EC.element_to_be_clickable(self.login_button))
            login_option.click()

            print("Login menu opened successfully")

        except TimeoutException:
            raise AssertionError(" Menu or Login option not clickable in time.")
        except NoSuchElementException:
            raise AssertionError("Menu or Login option not found on screen.")

    @allure.step("VALIDATE LOGIN SCENARIO")
    def login(self):
        try:
            user_field = self.wait.until(EC.element_to_be_clickable(self.username_field))
            user_field.click()

            pass_field = self.wait.until(EC.element_to_be_clickable(self.password_field))
            pass_field.click()

            login_button = self.wait.until(EC.element_to_be_clickable(self.login_btn))
            login_button.click()

            print("Login attempted with username ")

        except TimeoutException:
            raise AssertionError("Username/Password field or Login button not available in time.")
        except NoSuchElementException:
            raise AssertionError("Username/Password element not found on screen.")

    @allure.step("VALIDATE LOGOUT SCENARIO")
    def logout(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            menu = self.wait.until(EC.element_to_be_clickable(self.view_menu))
            menu.click()

            logout_button = self.wait.until(EC.element_to_be_clickable(self.logout_btn))
            logout_button.click()

            print("Logout performed successfully")

        except TimeoutException:
            raise AssertionError("Logout elements not clickable within timeout.")
        except NoSuchElementException:
            raise AssertionError("Logout button not found in the UI.")
