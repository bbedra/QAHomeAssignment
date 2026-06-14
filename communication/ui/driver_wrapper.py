import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

EXPLICIT_TIMEOUT_SHORT_WAIT = 3
EXPLICIT_TIMEOUT_LONG_WAIT = 10


class DriverWrapper:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait_short = self.get_custom_wait(EXPLICIT_TIMEOUT_SHORT_WAIT)
        self.wait_long = self.get_custom_wait(EXPLICIT_TIMEOUT_LONG_WAIT)

    def __getattr__(self, name):
        return getattr(self.driver, name)

    def get_custom_wait(self, timeout: float) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    def find_short(self, locator: tuple[str, str]) -> WebElement:
        return self.wait_short.until(ec.presence_of_element_located(locator))

    def find_long(self, locator: tuple[str, str]) -> WebElement:
        return self.wait_long.until(ec.presence_of_element_located(locator))

    def get_stable(self, locator: tuple[str, str]):
        end_time = time.time() + EXPLICIT_TIMEOUT_LONG_WAIT

        previous = None
        stable_count = 0

        while time.time() < end_time:
            current = self.driver.find_element(*locator).text

            if current == previous:
                stable_count += 1
            else:
                stable_count = 0

            if stable_count >= 2:
                return current

            previous = current
            time.sleep(1)

        raise TimeoutError("Element did not stabilize.")
