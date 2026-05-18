from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage


def test_place_order(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    product_page = ProductPage(driver)

    checkout_page = CheckoutPage(driver)

    print(
        "\nTEST CASE : PLACE ORDER"
    )

    # =========================
    # OPEN PRODUCT PAGE
    # =========================

    product_page.open_first_product()

    print(
        "\nProduct Details Page Opened"
    )

    # =========================
    # CLICK PLUS BUTTON
    # =========================

    product_page.click_plus_button()

    print(
        "\nPlus Button Working Successfully"
    )

    # =========================
    # CLICK ADD TO CART
    # =========================

    product_page.click_add_to_cart()

    print(
        "\nProduct Added To Cart Successfully"
    )

    # =========================
    # OPEN CHECKOUT PAGE
    # =========================

    driver.get(
        "https://practicesoftwaretesting.com/checkout"
    )

    print(
        "\nCheckout Page Opened"
    )

    # =========================
    # CLICK CHECKOUT BUTTON
    # =========================

    checkout_page.click_checkout_button()

    print(
        "\nCheckout Button Clicked Successfully"
    )

    # =========================
    # CLICK GUEST TAB
    # =========================

    checkout_page.click_guest_tab()

    print(
        "\nGuest Tab Opened Successfully"
    )

    # =========================
    # FILL GUEST DETAILS
    # =========================

    checkout_page.fill_guest_details()

    print(
        "\nGuest Details Filled Successfully"
    )

    # =========================
    # CONTINUE AS GUEST
    # =========================

    checkout_page.continue_as_guest()

    print(
        "\nContinue As Guest Successful"
    )

    # =========================
    # CLICK PROCEED TO CHECKOUT
    # =========================

    checkout_page.click_billing_checkout()

    print(
        "\nProceed To Billing Successful"
    )

    # =========================
    # FILL BILLING ADDRESS
    # =========================

    checkout_page.fill_billing_address()

    print(
        "\nBilling Address Filled Successfully"
    )

    # =========================
    # SELECT PAYMENT METHOD
    # =========================

    checkout_page.select_payment_method()

    print(
        "\nPayment Method Selected Successfully"
    )

    # =========================
    # CLICK CONFIRM BUTTON
    # =========================

    checkout_page.click_confirm_button()

    print(
        "\nOrder Confirmed Successfully"
    )

    # =========================
    # VERIFY SUCCESS MESSAGE
    # =========================

    success_message = (
        checkout_page.get_success_message()
    )

    print(
        f"\nSUCCESS MESSAGE:\n{success_message}"
    )

    assert success_message

    print(
        "\nORDER PLACED SUCCESSFULLY"
    )