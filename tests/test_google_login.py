from pages.google_login_page import GoogleLoginPage
import time


# =========================
# TEST GOOGLE LOGIN
# =========================

def test_google_login_button(driver):

    driver.get(
        "https://practicesoftwaretesting.com/auth/login"
    )

    google_page = GoogleLoginPage(driver)

    print(
        "\nTEST CASE : GOOGLE LOGIN"
    )

    # =========================
    # CLICK GOOGLE BUTTON
    # =========================

    google_page.click_google_login()

    print(
        "\nGoogle Login Button Clicked"
    )

    # =========================
    # SWITCH WINDOW
    # =========================

    google_page.switch_to_google_window()

    print(
        "\nSwitched To Google Window"
    )

    # =========================
    # GET CURRENT URL
    # =========================

    current_url = (
        google_page.get_current_url()
    )

    print(
        f"\nCurrent URL:\n{current_url}"
    )

    # =========================
    # GET PAGE TITLE
    # =========================

    title = (
        google_page.get_page_title()
    )

    print(
        f"\nPage Title:\n{title}"
    )

    # =========================
    # VERIFY GOOGLE PAGE
    # =========================

    if "google" in current_url.lower():

        print(
            "\nGOOGLE LOGIN PAGE OPENED"
        )

    else:

        print(
            "\nGOOGLE LOGIN FAILED"
        )

    # =========================
    # ASSERTION
    # =========================

    assert "google" in current_url.lower()

    print(
        "\nTEST CASE PASSED"
    )

    time.sleep(3)