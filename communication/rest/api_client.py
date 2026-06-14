from communication.rest.rest_client import RestClient
from models.enums import Selection


class ApiClient:
    def __init__(self, base_url: str, user_id: str):
        self.__rest_client = RestClient(base_url, user_id)

    def __handle_get_request(self, endpoint: str) -> dict:
        response = self.__rest_client.get(endpoint)
        return response.json()

    def __handle_post_requests(self, endpoint: str, json: dict = None) -> dict:
        response = self.__rest_client.post(endpoint, json=json)
        return response.json()

    def get_matches(self) -> dict:
        return self.__handle_get_request("/api/matches")

    def get_balance(self):
        return self.__handle_get_request("/api/balance")

    def place_bet(self, match_id: str, selection: Selection, stake: float) -> dict:
        data = {
            "matchId": match_id,
            "selection": selection.name,
            "stake": stake
        }
        return self.__handle_post_requests("/api/place-bet", data)

    def reset_balance(self):
        self.__handle_post_requests("/api/reset-balance")
