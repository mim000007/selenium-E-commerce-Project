from pages.search_page import SearchPage
import time


def test_search_product(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    search_page = SearchPage(driver)

    # SEARCH PRODUCT
    search_page.search_product("Hammer")

    # WAIT TO SEE RESULT
    time.sleep(3)

    # GET PRODUCT TITLES
    product_titles = search_page.get_product_titles()

    print("Products Found:")
    
    for title in product_titles:
        print(title)

    # ASSERT
    assert any(
        "Hammer" in title
        for title in product_titles
    )

    print("SEARCH SUCCESS")