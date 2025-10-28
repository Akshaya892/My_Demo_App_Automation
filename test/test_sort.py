import pytest
import allure
from utils.driver_setup import create_driver
from pages.sort_page import SortPage


@pytest.fixture(scope="class")
def setup(request):
    driver = create_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestSortPrices:

    @allure.title("SORT: Verify sorting by price and verify order")
    def test_sort_prices(self):
        sort_page = SortPage(self.driver)

        # Fetch initial prices for reference
        sort_page.fetch_all_prices()

        # Verify ascending order
        sort_page.verify_sort_ascending()

        # Verify descending order
        sort_page.verify_sort_descending()
