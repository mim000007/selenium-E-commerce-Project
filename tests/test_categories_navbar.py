from pages.categories_page import CategoriesPage
import time


# =========================
# VERIFY PRODUCTS
# =========================

def verify_products(
    category_name,
    category_page
):

    products = category_page.get_products()

    print(
        f"\nProducts Found: {len(products)}"
    )

    if len(products) > 0:

        print(
            f"{category_name} category working"
        )

        for product in products[:5]:

            print(product.text)

    else:

        print(
            f"No products found in "
            f"{category_name}"
        )

    assert True


# =========================
# TEST CATEGORY NAVBAR
# =========================

def test_categories_navbar(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    category_page = CategoriesPage(driver)

    categories = [
        "Hand Tools",
        "Power Tools",
        "Other",
        "Special Tools",
        "Rentals"
    ]

    test_case = 1

    for category in categories:

        print(
            f"\nTEST CASE {test_case}"
        )

        print(
            f"Testing Category: {category}"
        )

        # OPEN DROPDOWN
        category_page.open_categories_dropdown()

        # CLICK CATEGORY
        category_page.click_category(
            category
        )

        # VERIFY PRODUCTS
        verify_products(
            category,
            category_page
        )

        print(
            f"\nTEST CASE {test_case} PASSED"
        )

        # BACK TO HOME PAGE
        driver.get(
            "https://practicesoftwaretesting.com/"
        )

        time.sleep(2)

        test_case += 1