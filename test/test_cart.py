import pytest
import allure
from utils.driver_setup import create_driver
from pages.cart_page import CartPage


@pytest.fixture(scope="function")
def setup(request):
    driver = create_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestCart:

    @allure.title("VALIDATE CART: add a product, verify it appears correctly")
    def test_valid_login(self):
        cart_page = CartPage(self.driver)
        cart_page.open_product()
        cart_page.verify_cart_page()
