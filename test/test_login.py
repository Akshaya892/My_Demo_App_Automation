import pytest
import allure
from utils.driver_setup import create_driver
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def setup(request):
    driver = create_driver()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.title("LOGIN PAGE VALIDATION")
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.open_login_menu()
        login_page.login()
        login_page.logout()
    