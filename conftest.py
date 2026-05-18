import pytest
from utils.driver_factory import DriverFactory


@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    driver.get("https://practicesoftwaretesting.com/")
    
    yield driver

    driver.quit()