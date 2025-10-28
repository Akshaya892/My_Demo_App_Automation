from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "ZD222NXZD5"
    options.app_package = "com.saucelabs.mydemoapp.android"
    options.app_activity = "com.saucelabs.mydemoapp.android.view.activities.SplashActivity"
    options.no_reset = False

    # Connect to Appium server (default 4723)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    return driver
