from pages.register_page import RegisterPage
from selenium.webdriver.common.by import By
import random
import time


# =========================
# GENERATE RANDOM EMAIL
# =========================

def generate_email():

    random_number = random.randint(
        1000,
        999999
    )

    return (
        f"mim{random_number}@gmail.com"
    )


# =========================
# TEST REGISTRATION
# =========================

def test_customer_registration(driver):

    driver.get(
        "https://practicesoftwaretesting.com/auth/register"
    )

    register_page = RegisterPage(driver)

    print(
        "\nTEST CASE : CUSTOMER REGISTRATION"
    )

    # =========================
    # DYNAMIC EMAIL
    # =========================

    email = generate_email()

    print(
        f"\nGenerated Email: {email}"
    )

    # =========================
    # FILL FORM
    # =========================

    register_page.enter_first_name(
        "Mim"
    )

    register_page.enter_last_name(
        "Rahman"
    )

    register_page.enter_dob(
        "2001-12-07"
    )

    register_page.select_country(
        "Bangladesh"
    )

    register_page.enter_postcode(
        "1212"
    )

    register_page.enter_house_number(
        "121"
    )

    register_page.enter_street(
        "Gerhard Heights"
    )

    register_page.enter_city(
        "Bangladesh"
    )

    register_page.enter_state(
        "dhaka"
    )

    register_page.enter_phone(
        "12345678"
    )

    register_page.enter_email(
        email
    )

    register_page.enter_password(
        "NAim1????"
    )

    print(
        "\nRegistration Form Filled"
    )

    time.sleep(2)

    # =========================
    # CLICK REGISTER
    # =========================

    register_page.click_register()

    print(
        "\nRegister Button Clicked"
    )

    time.sleep(5)

    # =========================
    # DEBUG ERRORS
    # =========================

    errors = driver.find_elements(
        By.CSS_SELECTOR,
        ".help-block"
    )

    for error in errors:

        if error.text.strip():

            print(
                "\nVALIDATION ERROR:"
            )

            print(error.text)

    # =========================
    # VERIFY
    # =========================

    current_url = driver.current_url

    print(
        f"\nCurrent URL: {current_url}"
    )

    if "login" in current_url:

        print(
            "\nREGISTRATION SUCCESSFUL"
        )

    else:

        print(
            "\nREGISTRATION FAILED"
        )

    assert "login" in current_url

    print(
        "\nTEST CASE PASSED"
    )