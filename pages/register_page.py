from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class RegisterPage:

    FIRST_NAME = (
        By.CSS_SELECTOR,
        'input[data-test="first-name"]'
    )

    LAST_NAME = (
        By.CSS_SELECTOR,
        'input[data-test="last-name"]'
    )

    DOB = (
        By.CSS_SELECTOR,
        'input[data-test="dob"]'
    )

    COUNTRY = (
        By.CSS_SELECTOR,
        'select[data-test="country"]'
    )

    POSTCODE = (
        By.CSS_SELECTOR,
        'input[data-test="postal_code"]'
    )

    HOUSE_NUMBER = (
        By.CSS_SELECTOR,
        'input[data-test="house_number"]'
    )

    STREET = (
        By.CSS_SELECTOR,
        'input[data-test="street"]'
    )

    CITY = (
        By.CSS_SELECTOR,
        'input[data-test="city"]'
    )

    STATE = (
        By.CSS_SELECTOR,
        'input[data-test="state"]'
    )

    PHONE = (
        By.CSS_SELECTOR,
        'input[data-test="phone"]'
    )

    EMAIL = (
        By.CSS_SELECTOR,
        'input[data-test="email"]'
    )

    PASSWORD = (
        By.CSS_SELECTOR,
        'input[data-test="password"]'
    )

    REGISTER_BUTTON = (
        By.CSS_SELECTOR,
        'button[data-test="register-submit"]'
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    # =========================
    # ENTER FIRST NAME
    # =========================

    def enter_first_name(self, value):

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys(value)

    # =========================
    # ENTER LAST NAME
    # =========================

    def enter_last_name(self, value):

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(value)

    # =========================
    # ENTER DOB
    # =========================

    def enter_dob(self, value):

        self.driver.find_element(
            *self.DOB
        ).send_keys(value)

    # =========================
    # SELECT COUNTRY
    # =========================

    def select_country(self, value):

        dropdown = Select(
            self.driver.find_element(
                *self.COUNTRY
            )
        )

        dropdown.select_by_visible_text(
            value
        )

    # =========================
    # ENTER POSTCODE
    # =========================

    def enter_postcode(self, value):

        self.driver.find_element(
            *self.POSTCODE
        ).send_keys(value)

    # =========================
    # ENTER HOUSE NUMBER
    # =========================

    def enter_house_number(self, value):

        self.driver.find_element(
            *self.HOUSE_NUMBER
        ).send_keys(value)

    # =========================
    # ENTER STREET
    # =========================

    def enter_street(self, value):

        self.driver.find_element(
            *self.STREET
        ).send_keys(value)

    # =========================
    # ENTER CITY
    # =========================

    def enter_city(self, value):

        self.driver.find_element(
            *self.CITY
        ).send_keys(value)

    # =========================
    # ENTER STATE
    # =========================

    def enter_state(self, value):

        self.driver.find_element(
            *self.STATE
        ).send_keys(value)

    # =========================
    # ENTER PHONE
    # =========================

    def enter_phone(self, value):

        self.driver.find_element(
            *self.PHONE
        ).send_keys(value)

    # =========================
    # ENTER EMAIL
    # =========================

    def enter_email(self, value):

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(value)

    # =========================
    # ENTER PASSWORD
    # =========================

    def enter_password(self, value):

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(value)

    # =========================
    # CLICK REGISTER
    # =========================

    def click_register(self):

        self.driver.find_element(
            *self.REGISTER_BUTTON
        ).click()

        time.sleep(5)