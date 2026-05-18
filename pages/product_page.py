from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage:

    # =========================
    # LOCATORS
    # =========================

    FIRST_PRODUCT = (
        By.XPATH,
        "(//a[contains(@href,'/product/')])[1]"
    )

    PRODUCT_NAME = (
        By.TAG_NAME,
        "h1"
    )

    PLUS_BUTTON = (
        By.XPATH,
        "(//button[@class='btn btn-secondary'])[2]"
    )

    MINUS_BUTTON = (
        By.XPATH,
        "(//button[@class='btn btn-secondary'])[1]"
    )

    QUANTITY_TEXT = (
        By.XPATH,
        "//input[@id='quantity-input']"
    )

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Add to cart')]"
    )

    CART_COUNT = (
        By.CSS_SELECTOR,
        "#lblCartCount"
    )

    CHECKOUT_PRODUCT = (
        By.XPATH,
        "//td[contains(.,'Combination Pliers')]"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    # =========================
    # OPEN PRODUCT DETAILS PAGE
    # =========================

    def open_first_product(self):

        product = self.wait.until(
            EC.element_to_be_clickable(
                self.FIRST_PRODUCT
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            product
        )

        time.sleep(3)

    # =========================
    # GET PRODUCT NAME
    # =========================

    def get_product_name(self):

        product_name = self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCT_NAME
            )
        )

        return product_name.text

    # =========================
    # CLICK PLUS BUTTON
    # =========================

    def click_plus_button(self):

        plus = self.wait.until(
            EC.element_to_be_clickable(
                self.PLUS_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            plus
        )

        time.sleep(2)

    # =========================
    # CLICK MINUS BUTTON
    # =========================

    def click_minus_button(self):

        minus = self.wait.until(
            EC.element_to_be_clickable(
                self.MINUS_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            minus
        )

        time.sleep(2)

    # =========================
    # GET QUANTITY
    # =========================

    def get_quantity(self):

        time.sleep(2)

        quantity = self.wait.until(
            EC.visibility_of_element_located(
                self.QUANTITY_TEXT
            )
        )

        value = quantity.get_attribute(
            "value"
        )

        return value.strip()

    # =========================
    # CLICK ADD TO CART
    # =========================

    def click_add_to_cart(self):

        add_cart = self.wait.until(
            EC.element_to_be_clickable(
                self.ADD_TO_CART_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            add_cart
        )

        time.sleep(3)

    # =========================
    # GET CART COUNT
    # =========================

    def get_cart_count(self):

        cart = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_COUNT
            )
        )

        return cart.text

    # =========================
    # VERIFY PRODUCT IN CHECKOUT
    # =========================

    def verify_checkout_product(self):

        product = self.wait.until(
            EC.visibility_of_element_located(
                self.CHECKOUT_PRODUCT
            )
        )

        return product.is_displayed()