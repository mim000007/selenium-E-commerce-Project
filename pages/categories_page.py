from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CategoriesPage:

    # =========================
    # LOCATORS
    # =========================

    CATEGORIES_MENU = (
        By.XPATH,
        "//button[contains(.,'Categories')]"
    )

    PRODUCT_TITLES = (
        By.CSS_SELECTOR,
        ".card-title"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================
    # OPEN DROPDOWN
    # =========================

    def open_categories_dropdown(self):

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                self.CATEGORIES_MENU
            )
        )

        dropdown.click()

        time.sleep(2)

    # =========================
    # CLICK CATEGORY
    # =========================

    def click_category(
        self,
        category_name
    ):

        category = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//a[contains(.,'{category_name}')]"
                )
            )
        )

        category.click()

        time.sleep(3)

    # =========================
    # GET PRODUCTS
    # =========================

    def get_products(self):

        products = self.driver.find_elements(
            *self.PRODUCT_TITLES
        )

        return products