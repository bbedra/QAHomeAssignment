import pytest

from communication.rest.api_client import ApiClient
from models.enums import Selection

STAKE_TO_LOW_MSG = "Stake must be at least 1.00."
STAKE_TO_HIGH_MSG = "Stake must be at most 100.00."
BET_PLACED_SUCCESSFULLY_MSG = "Bet placed successfully"


class TestApi:
    @pytest.mark.parametrize("stake, expected_result", [
        (-1.00, STAKE_TO_LOW_MSG),
        (0.00, STAKE_TO_LOW_MSG),
        (0.99, STAKE_TO_LOW_MSG),
        (1.00, BET_PLACED_SUCCESSFULLY_MSG),
        (1.01, BET_PLACED_SUCCESSFULLY_MSG),
        (99.99, BET_PLACED_SUCCESSFULLY_MSG),
        (100.00, BET_PLACED_SUCCESSFULLY_MSG),
        (100.01, STAKE_TO_HIGH_MSG),
        (10000000.0, STAKE_TO_HIGH_MSG),
    ])
    def test_stake_value_range(self, api_client: ApiClient, stake: float, expected_result: str):
        """
        This test verifies the Business rule that defines the minimum and maximum stake limits.
        It is important, because this affects the correctness of the betting process.
        Additionally, API can be used by external partners, so when it's not working as expected it can harm our
        and our partners' reputation.
        Also, this test is fast, deterministic and thanks to parametrization, it covers multiple scenarios.
        """
        matches = api_client.get_matches()
        match_id = matches[-1]["id"]
        bet_response = api_client.place_bet(match_id, Selection.HOME, stake)
        actual_error_msg = bet_response.get("message", "")
        if expected_result:
            assert actual_error_msg == expected_result,\
                (f"Placing bet with stake '{stake}' should result with error '{expected_result}', "
                 f"but got this instead: {actual_error_msg}.")
        else:
            assert not actual_error_msg, \
                (f"Placing bet with stake '{stake}' should result with no error, "
                 f"but got this instead: {actual_error_msg}.")
