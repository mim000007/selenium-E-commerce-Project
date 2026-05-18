from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class GoogleLoginPage:

    # =========================
    # LOCATORS
    # =========================

    GOOGLE_LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Google')]"
    )

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            driver,
            10
        )

    # =========================
    # CLICK GOOGLE LOGIN BUTTON
    # =========================

    def click_google_login(self):

        google_button = self.wait.until(
            EC.element_to_be_clickable(
                self.GOOGLE_LOGIN_BUTTON
            )
        )

        google_button.click()

        time.sleep(3)

    # =========================
    # SWITCH TO GOOGLE WINDOW
    # =========================

    def switch_to_google_window(self):

        windows = self.driver.window_handles

        self.driver.switch_to.window(
            windows[-1]
        )

        time.sleep(3)

    # =========================
    # GET CURRENT URL
    # =========================

    def get_current_url(self):

        return self.driver.current_url

    # =========================
    # GET PAGE TITLE
    # =========================

    def get_page_title(self):

        return self.driver.title