from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # =========================
    # LOCATORS
    # =========================

    EMAIL_INPUT = (
        By.ID,
        "email"
    )

    PASSWORD_INPUT = (
        By.ID,
        "password"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//input[@data-test='login-submit']"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    # =========================
    # ENTER EMAIL
    # =========================

    def enter_email(self, email):

        email_input = self.wait.until(
            EC.visibility_of_element_located(
                self.EMAIL_INPUT
            )
        )

        email_input.clear()

        email_input.send_keys(
            email
        )

    # =========================
    # ENTER PASSWORD
    # =========================

    def enter_password(self, password):

        password_input = self.wait.until(
            EC.visibility_of_element_located(
                self.PASSWORD_INPUT
            )
        )

        password_input.clear()

        password_input.send_keys(
            password
        )

    # =========================
    # CLICK LOGIN BUTTON
    # =========================

    def click_login(self):

        login_button = self.wait.until(
            EC.element_to_be_clickable(
                self.LOGIN_BUTTON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            login_button
        )