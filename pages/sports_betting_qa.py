from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from models.enums import Selection
from pages.header import Header
from utils.logger import logger


class SportsBettingQA(Header):
    stake_input_locator = (By.ID, "bet-slip-stake-input")
    potential_payout_locator = (By.ID, "bet-slip-potential-payout")
    place_bet_button_locator = (By.ID, "bet-slip-place-bet")
    modal_success_locator = (By.ID, "modal-success")
    modal_success_payout_locator = (By.ID, "modal-success-payout")
    modal_success_close_button_locator = (By.ID, "modal-success-close")

    def select_first_upcoming_event(self, selection: Selection):
        selection_button_locator = (
            By.XPATH,
            f"//div[contains(@class, 'matchCard') and .//span[contains(text(), 'UPCOMING')]]"
            f"//button[.//span[text()='{selection.value}']]"
        )
        selection_buttons = self.driver.find_elements(*selection_button_locator)
        selection_buttons[0].click()
        logger.info(f"Selected {selection.value} in first upcoming event.")

    def provide_stake(self, value: float):
        logger.info(f"Provide stake {value}.")
        self.driver.find_short(self.stake_input_locator).send_keys(str(value))

    def get_potential_payout(self) -> str:
        potential_payout = self.driver.find_short(self.potential_payout_locator).text
        logger.info(f"Potential payout: {potential_payout}")
        return potential_payout

    def click_place_bet(self):
        logger.info("Click 'PLACE BET' button.")
        self.driver.find_short(self.place_bet_button_locator).click()

    def is_success_modal_visible(self) -> bool:
        try:
            self.driver.find_long(self.modal_success_locator)
            return True
        except TimeoutException:
            return False

    def get_receipt_potential_payout(self) -> str:
        modal_success_payout = self.driver.find_short(self.modal_success_payout_locator).text
        logger.info(f"Potential payout after placing the bet: {modal_success_payout}.")
        return modal_success_payout

    def close_receipt(self):
        logger.info("Click 'CLOSE' button on receipt.")
        self.driver.find_short(self.modal_success_close_button_locator).click()
