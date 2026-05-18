import pytest
import time

from pages.sort_page import SortPage


@pytest.mark.parametrize(
    "sort_option",
    [
        "Name (A - Z)",
        "Name (Z - A)",
        "Price (Low - High)",
        "Price (High - Low)"
    ]
)

def test_sort_products(driver, sort_option):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    sort_page = SortPage(driver)

    # SELECT SORT OPTION
    sort_page.select_sort_option(
        sort_option
    )

    # WAIT FOR UI UPDATE
    time.sleep(3)

    print(f"\nSORT OPTION: {sort_option}")

    products = sort_page.get_product_titles()

    for product in products:
        print(product)

    print("\nSORT TEST COMPLETED")