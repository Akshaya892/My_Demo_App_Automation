import pytest
import allure
from utils.driver_setup import create_driver
from pages.product_catalog_page import ProductCatalogPage


@pytest.fixture(scope="function")
def setup(request):
    driver = create_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestProductCatalog:

    @allure.title("PRODUCT CATALOG: open catalog, open product details, verify name/price")
    def test_valid_login(self):
        product_catalog_page = ProductCatalogPage(self.driver)
        product_catalog_page.open_product()
        product_catalog_page.verify_product_details()
