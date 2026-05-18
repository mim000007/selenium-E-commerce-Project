from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        'input[data-test="search-query"]'
    )

    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        'button[data-test="search-submit"]'
    )

    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".card-title"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_product(self, product_name):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_INPUT
            )
        )

        search_box.clear()
        search_box.send_keys(product_name)

        self.wait.until(
            EC.element_to_be_clickable(
                self.SEARCH_BUTTON
            )
        ).click()

    def get_product_titles(self):

        products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_TITLE
            )
        )

        return [product.text for product in products]