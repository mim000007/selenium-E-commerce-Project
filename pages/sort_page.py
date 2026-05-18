from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class SortPage:

    SORT_DROPDOWN = (
        By.CSS_SELECTOR,
        'select[data-test="sort"]'
    )

    PRODUCT_TITLES = (
        By.CSS_SELECTOR,
        ".card-title"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_sort_option(self, option_text):

        dropdown_element = self.wait.until(
            EC.visibility_of_element_located(
                self.SORT_DROPDOWN
            )
        )

        dropdown = Select(dropdown_element)

        dropdown.select_by_visible_text(
            option_text
        )

    def get_product_titles(self):

        products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_TITLES
            )
        )

        return [product.text for product in products]