from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SearchPage:

    # =========================
    # LOCATORS
    # =========================

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        "input[data-test='search-query']"
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-test='search-submit']"
    )

    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".card-title"
    )

    # =========================
    # CONSTRUCTOR
    # =========================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            15
        )

    # =========================
    # SEARCH PRODUCT
    # =========================

    def search_product(self, product_name):

        # WAIT SEARCH BOX

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        # CLICK SEARCH INPUT

        search_box.click()

        # CLEAR FIELD

        search_box.clear()

        # TYPE SLOWLY

        for char in product_name:

            search_box.send_keys(char)

            time.sleep(0.3)

        print(
            f"\nSearching Product: {product_name}"
        )

        # CLICK SEARCH BUTTON

        search_button = self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            search_button
        )

        # WAIT PRODUCTS LOAD

        self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_TITLE
            )
        )

    # =========================
    # GET PRODUCT TITLES
    # =========================

    def get_product_titles(self):

        products = self.driver.find_elements(
            *self.PRODUCT_TITLE
        )

        titles = []

        for product in products:

            title = product.text.strip()

            if title:

                titles.append(title)

        return titles