from pages.product_page import ProductPage
import time


def test_add_to_cart_functionality(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    product_page = ProductPage(driver)

    print(
        "\nTEST CASE : ADD TO CART FUNCTIONALITY"
    )

    # =========================
    # OPEN PRODUCT PAGE
    # =========================

    product_page.open_first_product()

    print(
        "\nProduct Details Page Opened"
    )

    # =========================
    # VERIFY PRODUCT NAME
    # =========================

    product_name = (
        product_page.get_product_name()
    )

    print(
        f"\nProduct Name: {product_name}"
    )

    # =========================
    # TEST PLUS BUTTON
    # =========================

    product_page.click_plus_button()

    quantity = (
        product_page.get_quantity()
    )

    print(
        f"\nQuantity After Plus: {quantity}"
    )

    assert quantity == "2"

    print(
        "\nPLUS BUTTON WORKING"
    )

    # =========================
    # TEST MINUS BUTTON
    # =========================

    product_page.click_minus_button()

    quantity = (
        product_page.get_quantity()
    )

    print(
        f"\nQuantity After Minus: {quantity}"
    )

    assert quantity == "1"

    print(
        "\nMINUS BUTTON WORKING"
    )

    # =========================
    # CLICK ADD TO CART
    # =========================

    product_page.click_add_to_cart()

    print(
        "\nAdd To Cart Button Clicked"
    )

    # =========================
    # VERIFY CART COUNT
    # =========================

    cart_count = (
        product_page.get_cart_count()
    )

    print(
        f"\nCart Count: {cart_count}"
    )

    assert int(cart_count) > 0

    print(
        "\nPRODUCT ADDED TO CART"
    )

    # =========================
    # OPEN CHECKOUT PAGE
    # =========================

    driver.get(
        "https://practicesoftwaretesting.com/checkout"
    )

    time.sleep(3)

    print(
        "\nCheckout Page Opened"
    )

    # =========================
    # VERIFY PRODUCT IN CHECKOUT
    # =========================

    product_visible = (
        product_page.verify_checkout_product()
    )

    assert product_visible

    print(
        "\nPRODUCT DISPLAYED IN CHECKOUT"
    )

    print(
        "\nADD TO CART FUNCTIONALITY PASSED"
    )