import requests


class ApiManage:
    def __init__(self, url: str, params: dict = {}):
        self.__url = url
        self.__params = params

    def get_json(self) -> dict:
        response = requests.get(url=self.__url, params=self.__params)
        response.raise_for_status()
        return response.json()
