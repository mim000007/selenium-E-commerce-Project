from pages.login_page import LoginPage
from utils.logger import setup_logger
import time


logger = setup_logger()


def test_valid_login(driver):

    driver.get(
        "https://practicesoftwaretesting.com/auth/login"
    )

    logger.info(
        "Login Page Opened"
    )

    login_page = LoginPage(driver)

    # =========================
    # ENTER EMAIL
    # =========================

    login_page.enter_email(
        "customer@practicesoftwaretesting.com"
    )

    logger.info(
        "Email Entered"
    )

    # =========================
    # ENTER PASSWORD
    # =========================

    login_page.enter_password(
        "welcome01"
    )

    logger.info(
        "Password Entered"
    )

    # =========================
    # CLICK LOGIN
    # =========================

    login_page.click_login()

    logger.info(
        "Login Button Clicked"
    )

    time.sleep(5)

    # =========================
    # VERIFY LOGIN
    # =========================

    current_url = (
        driver.current_url.lower()
    )

    logger.info(
        f"Current URL: {current_url}"
    )

    print(
        f"\nCurrent URL: {current_url}"
    )

    assert "account" in current_url

    logger.info(
        "TEST CASE PASSED"
    )

    print(
        "\nLOGIN TEST PASSED"
    )