import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SortPage:

    price_elements = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")
    sort_menu = (AppiumBy.ACCESSIBILITY_ID, "Shows current sorting order and displays available sorting options")
    sort_price_ascending = (AppiumBy.ACCESSIBILITY_ID, "Displays ascending sorting order by price")
    sort_price_descending = (AppiumBy.ACCESSIBILITY_ID, "Displays descending sorting order by price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Fetch all product prices from by scrolls")
    def fetch_all_prices(self):
        all_prices = []
        try:
            self.wait.until(EC.presence_of_all_elements_located(self.price_elements))
            all_prices.extend(self._get_visible_prices())
            print(f"Scroll 0: Prices so far → {all_prices}")

            # scroll and collect more prices
            for scroll_num in range(1, 6):
                self._scroll_down()
                time.sleep(1)
                current_prices = self._get_visible_prices()
                all_prices.extend(current_prices)

            allure.attach(str(all_prices), name="Fetched All Prices", attachment_type=allure.attachment_type.TEXT)
            print(f"Final fetched prices ({len(all_prices)}): {all_prices}")
            self.scroll_to_top()
            return all_prices

        except TimeoutException:
            raise AssertionError("Price elements not found within time.")

    def _click_sort_option(self, option_locator, order_name):
        try:
            sort_menu_btn = self.wait.until(EC.element_to_be_clickable(self.sort_menu))
            sort_menu_btn.click()
            time.sleep(1)

            sort_option = self.wait.until(EC.element_to_be_clickable(option_locator))
            sort_option.click()
            print(f"{order_name} order applied in UI.")
            time.sleep(3)
        except TimeoutException:
            raise AssertionError(f"Unable to apply {order_name} order. Sort option not found.")

    @allure.step("Apply ascending sort and verify order")
    def verify_sort_ascending(self):
        self._click_sort_option(self.sort_price_ascending, "Ascending")

        sorted_prices = self.fetch_all_prices()
        expected_sorted = sorted(sorted_prices)

        if sorted_prices == expected_sorted:
            message = f"Sort working correctly in ascending order.\nFinal Prices: {sorted_prices}"
            print(message)
            allure.attach(message, name="Ascending Sort Passed", attachment_type=allure.attachment_type.TEXT)
        else:
            message = (
                f"Sort not working correctly.\n"
                f"UI Prices: {sorted_prices}\n"
                f"Expected (Ascending): {expected_sorted}"
            )
            print(message)
            allure.attach(message, name="Ascending Sort Failed", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Prices are not sorted in ascending order.")
        return sorted_prices

    @allure.step("Apply descending sort and verify order")
    def verify_sort_descending(self):
        self._click_sort_option(self.sort_price_descending, "Descending")

        sorted_prices = self.fetch_all_prices()
        expected_sorted = sorted(sorted_prices, reverse=True)

        if sorted_prices == expected_sorted:
            message = f"Sort working correctly in descending order.\nFinal Prices: {sorted_prices}"
            print(message)
            allure.attach(message, name="Descending Sort Passed", attachment_type=allure.attachment_type.TEXT)
        else:
            message = (
                f"Sort not working correctly.\n"
                f"UI Prices: {sorted_prices}\n"
                f"Expected (Descending): {expected_sorted}"
            )
            print(message)
            allure.attach(message, name="Descending Sort Failed", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Prices are not sorted in descending order.")
        return sorted_prices

    def _get_visible_prices(self):
        price_elements = self.driver.find_elements(*self.price_elements)
        prices = []
        for el in price_elements:
            text = el.text.replace("$", "").strip()
            if text:
                prices.append(float(text))
        return prices

    def _scroll_down(self):
        size = self.driver.get_window_size()
        start_y = size["height"] * 0.8
        end_y = size["height"] * 0.3
        x = size["width"] / 2
        self.driver.swipe(x, start_y, x, end_y, 800)

    def scroll_to_top(self):
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToBeginning(10)'
            )
            print("Scrolled to top successfully.")
        except Exception as e:
            print(f"Failed to scroll to top: {e}")
