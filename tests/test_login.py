from pages.login_page import LoginPage
import time


def test_valid_login(driver):

    driver.get(
        "https://practicesoftwaretesting.com/auth/login"
    )

    login_page = LoginPage(driver)

    # DEMO ACCOUNT
    login_page.enter_email(
        "customer@practicesoftwaretesting.com"
    )

    login_page.enter_password(
        "welcome01"
    )

    login_page.click_login()

    # WAIT FOR LOGIN
    time.sleep(3)

    print("Current URL:", driver.current_url)

    # VERIFY LOGIN
    if login_page.is_logout_visible():
        print("LOGIN SUCCESS")
    else:
        print("LOGIN FAILED")
        print(
            "Error Message:",
            login_page.get_error_message()
        )

    assert login_page.is_logout_visible()