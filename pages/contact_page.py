from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ContactPage:

    FIRST_NAME = (
        By.CSS_SELECTOR,
        'input[data-test="first-name"]'
    )

    LAST_NAME = (
        By.CSS_SELECTOR,
        'input[data-test="last-name"]'
    )

    EMAIL = (
        By.CSS_SELECTOR,
        'input[data-test="email"]'
    )

    SUBJECT = (
        By.CSS_SELECTOR,
        'select[data-test="subject"]'
    )

    MESSAGE = (
        By.CSS_SELECTOR,
        'textarea[data-test="message"]'
    )

    FILE_UPLOAD = (
        By.CSS_SELECTOR,
        'input[type="file"]'
    )

    SEND_BUTTON = (
        By.CSS_SELECTOR,
        'input[data-test="contact-submit"]'
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-success"
    )

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # =========================
    # ENTER FIRST NAME
    # =========================

    def enter_first_name(self, first_name):

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        ).send_keys(first_name)

    # =========================
    # ENTER LAST NAME
    # =========================

    def enter_last_name(self, last_name):

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

    # =========================
    # ENTER EMAIL
    # =========================

    def enter_email(self, email):

        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

    # =========================
    # SELECT SUBJECT
    # =========================

    def select_subject(self, subject):

        dropdown = Select(
            self.driver.find_element(
                *self.SUBJECT
            )
        )

        dropdown.select_by_visible_text(
            subject
        )

    # =========================
    # ENTER MESSAGE
    # =========================

    def enter_message(self, message):

        self.driver.find_element(
            *self.MESSAGE
        ).send_keys(message)

    # =========================
    # UPLOAD FILE
    # =========================

    def upload_file(self, file_path):

        self.driver.find_element(
            *self.FILE_UPLOAD
        ).send_keys(file_path)

    # =========================
    # CLICK SEND
    # =========================

    def click_send(self):

        self.driver.find_element(
            *self.SEND_BUTTON
        ).click()

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