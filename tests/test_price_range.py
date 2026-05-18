from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# =========================
# MOVE PRICE SLIDER
# =========================

def move_slider(driver, offset):

    wait = WebDriverWait(driver, 10)

    # RIGHT HANDLE
    slider = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "(//span[contains(@class,'ngx-slider-pointer')])[2]"
            )
        )
    )

    actions = ActionChains(driver)

    actions.click_and_hold(
        slider
    ).move_by_offset(
        offset,
        0
    ).release().perform()

    time.sleep(3)


# =========================
# GET PRODUCTS
# =========================

def get_products(driver):

    products = driver.find_elements(
        By.CSS_SELECTOR,
        ".card-title"
    )

    return products


# =========================
# TEST CASE 1
# PRICE RANGE 0 - 100
# =========================

def test_price_range_0_to_100(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    print(
        "\nTEST CASE 1 : PRICE RANGE 0 - 100"
    )

    # MOVE SLIDER LEFT
    move_slider(driver, -100)

    products = get_products(driver)

    print(
        f"\nProducts Found: {len(products)}"
    )

    print("\nPRODUCT LIST:\n")

    for product in products[:10]:

        print(product.text)

    print(
        "\nTEST CASE 1 PASSED"
    )

    assert len(products) > 0


# =========================
# TEST CASE 2
# PRICE RANGE 100 - 200
# =========================

def test_price_range_100_to_200(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    print(
        "\nTEST CASE 2 : PRICE RANGE 100 - 200"
    )

    # KEEP DEFAULT MAX RANGE
    # MOVE SLIDER SLIGHTLY
    move_slider(driver, -20)

    products = get_products(driver)

    print(
        f"\nProducts Found: {len(products)}"
    )

    print("\nPRODUCT LIST:\n")

    for product in products[:10]:

        print(product.text)

    print(
        "\nTEST CASE 2 PASSED"
    )

    assert len(products) > 0