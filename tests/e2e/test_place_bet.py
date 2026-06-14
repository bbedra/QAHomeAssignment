from models.enums import Selection
from pages.sports_betting_qa import SportsBettingQA


class TestPlaceBet:
    def test_place_bet(self, sports_betting_qa: SportsBettingQA):
        """
        I've chosen this test because it checks the core functionality of the product
        and the most used path by the users.
        """
        initial_balance = sports_betting_qa.get_balance()
        sports_betting_qa.select_first_upcoming_event(Selection.HOME)

        stake = 10.0
        sports_betting_qa.provide_stake(stake)
        bet_slip_potential_payout = sports_betting_qa.get_potential_payout()
        sports_betting_qa.click_place_bet()
        assert sports_betting_qa.is_success_modal_visible(), "Success modal is not visible."

        receipt_potential_payout = sports_betting_qa.get_receipt_potential_payout()
        errors = []
        if bet_slip_potential_payout != receipt_potential_payout:
            errors.append("Bet slip potential payout and Receipt potential payout are different "
                          f"({bet_slip_potential_payout} != {receipt_potential_payout})")

        sports_betting_qa.close_receipt()
        updated_balance = sports_betting_qa.get_balance()
        expected_balance = initial_balance - stake
        if updated_balance != expected_balance:
            errors.append(
                f"Balance was not updated correctly. Expected: {expected_balance}, actual: {updated_balance}."
            )

        assert not errors, f"Following errors were found: {','.join(errors)}"
