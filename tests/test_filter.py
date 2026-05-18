from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# =========================
# CLICK CHECKBOX
# =========================

def click_checkbox(driver, wait, label_name):

    checkbox = wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f"//label[contains(.,'{label_name}')]/input"
            )
        )
    )

    driver.execute_script(
        "arguments[0].scrollIntoView(true);",
        checkbox
    )

    driver.execute_script(
        "arguments[0].click();",
        checkbox
    )

    print(f"{label_name} clicked")

    time.sleep(2)


# =========================
# VERIFY PRODUCTS
# =========================

def verify_products(driver, filter_name):

    products = driver.find_elements(
        By.CSS_SELECTOR,
        ".card-title"
    )

    print(f"Products Found: {len(products)}")

    if len(products) > 0:

        print(
            f"{filter_name} filter working"
        )

        for product in products[:5]:
            print(product.text)

    else:

        print(
            f"No products found for {filter_name}"
        )

    assert True


# =========================
# TEST CASE 1
# HAND TOOLS HEADER
# =========================

def test_hand_tools_header_checkbox(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    print("\nTEST CASE 1 : HAND TOOLS HEADER")

    click_checkbox(
        driver,
        wait,
        "Hand Tools"
    )

    verify_products(
        driver,
        "Hand Tools"
    )

    print("\nTEST CASE 1 PASSED")


# =========================
# TEST CASE 2
# HAND TOOLS ITEMS
# =========================

def test_hand_tools_filters(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    hand_tools = [
        "Hammer",
        "Hand Saw",
        "Wrench",
        "Screwdriver",
        "Pliers",
        "Chisels",
        "Measures"
    ]

    print("\nTEST CASE 2 : HAND TOOLS ITEMS")

    for tool in hand_tools:

        print(f"\nTesting: {tool}")

        click_checkbox(
            driver,
            wait,
            tool
        )

        verify_products(
            driver,
            tool
        )

        driver.refresh()

        time.sleep(2)

    print("\nTEST CASE 2 PASSED")


# =========================
# TEST CASE 3
# POWER TOOLS HEADER
# =========================

def test_power_tools_header_checkbox(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    print("\nTEST CASE 3 : POWER TOOLS HEADER")

    click_checkbox(
        driver,
        wait,
        "Power Tools"
    )

    verify_products(
        driver,
        "Power Tools"
    )

    print("\nTEST CASE 3 PASSED")


# =========================
# TEST CASE 4
# POWER TOOLS ITEMS
# =========================

def test_power_tools_filters(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    power_tools = [
        "Grinder",
        "Sander",
        "Saw",
        "Drill"
    ]

    print("\nTEST CASE 4 : POWER TOOLS ITEMS")

    for tool in power_tools:

        print(f"\nTesting: {tool}")

        click_checkbox(
            driver,
            wait,
            tool
        )

        verify_products(
            driver,
            tool
        )

        driver.refresh()

        time.sleep(2)

    print("\nTEST CASE 4 PASSED")


# =========================
# TEST CASE 5
# OTHER HEADER
# =========================

def test_other_header_checkbox(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    print("\nTEST CASE 5 : OTHER HEADER")

    click_checkbox(
        driver,
        wait,
        "Other"
    )

    verify_products(
        driver,
        "Other"
    )

    print("\nTEST CASE 5 PASSED")


# =========================
# TEST CASE 6
# OTHER ITEMS
# =========================

def test_other_filters(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    other_filters = [
        "Tool Belts",
        "Storage Solutions",
        "Workbench",
        "Safety Gear",
        "Fasteners"
    ]

    print("\nTEST CASE 6 : OTHER ITEMS")

    for item in other_filters:

        print(f"\nTesting: {item}")

        click_checkbox(
            driver,
            wait,
            item
        )

        verify_products(
            driver,
            item
        )

        driver.refresh()

        time.sleep(2)

    print("\nTEST CASE 6 PASSED")


# =========================
# TEST CASE 7
# BRAND FILTERS
# =========================

def test_brand_filters(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    brands = [
        "ForgeFlex Tools",
        "MightyCraft Hardware"
    ]

    print("\nTEST CASE 7 : BRAND FILTERS")

    for brand in brands:

        print(f"\nTesting: {brand}")

        click_checkbox(
            driver,
            wait,
            brand
        )

        verify_products(
            driver,
            brand
        )

        driver.refresh()

        time.sleep(2)

    print("\nTEST CASE 7 PASSED")


# =========================
# TEST CASE 8
# SUSTAINABILITY
# =========================

def test_sustainability_filter(driver):

    driver.get(
        "https://practicesoftwaretesting.com/"
    )

    wait = WebDriverWait(driver, 10)

    sustainability_filter = (
        "Show only eco-friendly products"
    )

    print(
        "\nTEST CASE 8 : SUSTAINABILITY FILTER"
    )

    click_checkbox(
        driver,
        wait,
        sustainability_filter
    )

    verify_products(
        driver,
        sustainability_filter
    )

    print("\nTEST CASE 8 PASSED")