import pytest
from selenium import webdriver
import os


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    # CLOSE BROWSER
    driver.quit()


# SCREENSHOT ON FAILURE
@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        if not os.path.exists(
            "screenshots"
        ):

            os.makedirs(
                "screenshots"
            )

        screenshot_name = (
            f"screenshots/{item.name}.png"
        )

        driver.save_screenshot(
            screenshot_name
        )

        print(
            f"\nScreenshot Saved: {screenshot_name}"
        )