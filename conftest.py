import pytest
import allure
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.cls.driver
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Screenshot", attachment_type=AttachmentType.PNG)
