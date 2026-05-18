from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class CheckoutPage:

    # =========================
    # LOCATORS
    # =========================

    PROCEED_CHECKOUT_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Proceed to checkout')]"
    )

    CONTINUE_AS_GUEST_TAB = (
        By.XPATH,
        "//a[contains(.,'Continue as Guest')]"
    )

    CONTINUE_GUEST_BUTTON = (
        By.CSS_SELECTOR,
        "input[data-test='guest-submit']"
    )

    EMAIL = (
        By.CSS_SELECTOR,
        "input[data-test='guest-email']"
    )

    FIRST_NAME = (
        By.CSS_SELECTOR,
        "input[data-test='guest-first-name']"
    )

    LAST_NAME = (
        By.CSS_SELECTOR,
        "input[data-test='guest-last-name']"
    )

    BILLING_CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        "button[data-test='proceed-2-guest']"
    )

    COUNTRY = (
        By.CSS_SELECTOR,
        "select[data-test='country']"
    )

    POSTCODE = (
        By.CSS_SELECTOR,
        "input[data-test='postal_code']"
    )

    HOUSE_NUMBER = (
        By.CSS_SELECTOR,
        "input[data-test='house_number']"
    )

    STREET = (
        By.CSS_SELECTOR,
        "input[data-test='street']"
    )

    CITY = (
        By.CSS_SELECTOR,
        "input[data-test='city']"
    )

    STATE = (
        By.CSS_SELECTOR,
        "input[data-test='state']"
    )

    ADDRESS_PROCEED_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Proceed to checkout')]"
    )

    PAYMENT_DROPDOWN = (
        By.CSS_SELECTOR,
        "select[data-test='payment-method']"
    )

    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Confirm')]"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".help-block"
    )

    # =========================
    # CONSTRUCTOR
    # =========================

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            20
        )

    # =========================
    # CLICK CHECKOUT BUTTON
    # =========================

    def click_checkout_button(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.PROCEED_CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print(
            "\nCheckout Button Clicked"
        )

    # =========================
    # CLICK GUEST TAB
    # =========================

    def click_guest_tab(self):

        guest = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_AS_GUEST_TAB
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            guest
        )

        print(
            "\nGuest Tab Opened"
        )

    # =========================
    # FILL GUEST DETAILS
    # =========================

    def fill_guest_details(self):

        email = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL
            )
        )

        firstname = self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

        lastname = self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )

        email.clear()
        firstname.clear()
        lastname.clear()

        email.send_keys(
            "rmim2906@gmail.com"
        )

        firstname.send_keys(
            "Mim"
        )

        lastname.send_keys(
            "Rahman"
        )

        print(
            "\nGuest Details Filled Successfully"
        )

    # =========================
    # CONTINUE AS GUEST
    # =========================

    def continue_as_guest(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_GUEST_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print(
            "\nContinue As Guest Successful"
        )

    # =========================
    # CLICK BILLING CHECKOUT
    # =========================

    def click_billing_checkout(self):

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.BILLING_CHECKOUT_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            button
        )

        print(
            "\nBilling Checkout Successful"
        )

    # =========================
    # FILL BILLING ADDRESS
    # =========================

    def fill_billing_address(self):

        country = Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.COUNTRY
                )
            )
        )

        country.select_by_visible_text(
            "Bangladesh"
        )

        postcode = self.wait.until(
            EC.visibility_of_element_located(
                self.POSTCODE
            )
        )

        postcode.clear()

        postcode.send_keys(
            "1212"
        )

        house = self.wait.until(
            EC.visibility_of_element_located(
                self.HOUSE_NUMBER
            )
        )

        house.clear()

        house.send_keys(
            "12"
        )

        street = self.wait.until(
            EC.visibility_of_element_located(
                self.STREET
            )
        )

        street.clear()

        street.send_keys(
            "Gerhard Heights"
        )

        city = self.wait.until(
            EC.visibility_of_element_located(
                self.CITY
            )
        )

        city.clear()

        city.send_keys(
            "Dhaka"
        )

        state = self.wait.until(
            EC.visibility_of_element_located(
                self.STATE
            )
        )

        state.clear()

        state.send_keys(
            "Dhaka"
        )

        print(
            "\nBilling Address Filled Successfully"
        )

    # =========================
    # CLICK ADDRESS PROCEED
    # =========================

    def click_address_proceed(self):

        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                self.ADDRESS_PROCEED_BUTTON
            )
        )

        address_button = buttons[-1]

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            address_button
        )

        self.driver.execute_script(
            "arguments[0].click();",
            address_button
        )

        print(
            "\nAddress Proceed Successful"
        )

    # =========================
    # SELECT PAYMENT METHOD
    # =========================

    def select_payment_method(self):

        payment = Select(
            self.wait.until(
                EC.visibility_of_element_located(
                    self.PAYMENT_DROPDOWN
                )
            )
        )

        payment.select_by_visible_text(
            "Cash on Delivery"
        )

        print(
            "\nPayment Method Selected Successfully"
        )

    # =========================
    # CLICK CONFIRM BUTTON
    # =========================

    def click_confirm_button(self):

        confirm = self.wait.until(
            EC.element_to_be_clickable(
                self.CONFIRM_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            confirm
        )

        print(
            "\nOrder Confirmed Successfully"
        )

    # =========================
    # GET SUCCESS MESSAGE
    # =========================

    def get_success_message(self):

        success = self.wait.until(
            EC.visibility_of_element_located(
                self.SUCCESS_MESSAGE
            )
        )

        return success.text