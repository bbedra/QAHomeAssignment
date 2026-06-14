from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Header(BasePage):
    header_balance_locator = (By.ID, "header-balance")

    def get_balance(self) -> float:
        full_header_balance = self.driver.get_stable(self.header_balance_locator)
        balance = full_header_balance.split(" ")[1][1:]
        return float(balance)
