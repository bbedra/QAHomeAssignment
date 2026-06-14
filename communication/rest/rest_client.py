import requests

from utils.logger import logger


class RestClient:
    def __init__(self, base_url: str, user_id: str):
        self.__base_url = base_url
        self.__user_id = user_id

    @property
    def __headers(self) -> dict:
        headers = {}
        if self.__user_id:
            headers["X-User-Id"] = self.__user_id
        else:
            logger.warning("Missing user id in the .env file.")

        return headers

    def get(self, endpoint: str) -> requests.Response:
        url = f"{self.__base_url}{endpoint}"
        response = requests.get(url, headers=self.__headers)
        logger.info(f"GET {url}: {response.status_code}")
        return response

    def post(self, endpoint: str, json: dict) -> requests.Response:
        url = f"{self.__base_url}{endpoint}"
        response = requests.post(url, json=json, headers=self.__headers)
        logger.info(f"POST {url}: {response.status_code}")
        return response
