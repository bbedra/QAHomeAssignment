import pytest
from selenium import webdriver

from communication.ui.driver_wrapper import DriverWrapper
from pages.sports_betting_qa import SportsBettingQA


@pytest.fixture(scope="session")
def driver() -> DriverWrapper:
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield DriverWrapper(driver)
    driver.quit()


@pytest.fixture(scope="session")
def sports_betting_qa(driver, authorized_app_address) -> SportsBettingQA:
    driver.get(authorized_app_address)
    return SportsBettingQA(driver)
