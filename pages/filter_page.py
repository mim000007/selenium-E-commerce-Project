from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FilterPage:

    PRODUCT_TITLES = (
        By.CSS_SELECTOR,
        ".card-title"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_checkbox(self, label_text):

        checkbox = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    f"//label[contains(., '{label_text}')]"
                )
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView();",
            checkbox
        )

        checkbox.click()

    def get_product_titles(self):

        products = self.wait.until(
            EC.presence_of_all_elements_located(
                self.PRODUCT_TITLES
            )
        )

        return [product.text for product in products]