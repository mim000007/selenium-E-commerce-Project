from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-test="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[data-test="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'input[data-test="login-submit"]')

    LOGOUT_BUTTON = (
        By.XPATH,
        "//a[contains(text(),'Sign out') or contains(text(),'Logout')]"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        ".alert-danger"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        ).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def is_logout_visible(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.LOGOUT_BUTTON
                )
            )
            return True
        except:
            return False

    def get_error_message(self):
        try:
            error = self.wait.until(
                EC.visibility_of_element_located(
                    self.ERROR_MESSAGE
                )
            )
            return error.text
        except:
            return "No error message found"