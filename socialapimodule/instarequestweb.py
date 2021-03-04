"""
A class for making requests to the social network Instagram used mobile API
"""
from json.decoder import JSONDecodeError
from pprint import pprint

import requests
import json
from logsource.logconfig import logger
from settings import requestsmap
from socialapimodule.loginrequest import LoginRequest


class InstagramRequestsWeb:

    def __init__(self, host_proxy: str, port_proxy: int):
        self.request = requests.Session()
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.requests_map = requestsmap.INSTAGRAM_WEB_DATA

    def _make_request_post(self, main_url: str, uri: str, params: dict, headers: dict) -> dict:
        """
        :param headers:
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        data = dict()
        try:
            response = self.request.post(main_url + uri, data=params, headers=headers)
            try:
                data = response.json()
                print(main_url + uri, response.status_code, data, response.headers)
                print(params)
                print(headers)
                print(self.request.cookies.get_dict())
            except JSONDecodeError as error:
                logger.warning(f"Error decode json - {error}, {response}")
                return {"status": False, "error": True, "error_type": error, "error_message": data}

        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 400:
            logger.warning(f"Error login request {response.status_code}, {data}")

            return {"status": False, "error_type": "Error login request"}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"] == 'ok':
                return {"status": True, "data": data}

        return {"status": False, "error": True, "error_type": response.status_code}

    def login(self, account_data: dict, initialization_parameters: object, initialization_headers: dict) -> dict:
        """
        :param initialization_headers: dict
        :param account_data: dict
        :param initialization_parameters: dict
        :return: dict
        """
        pre_request_obj = LoginRequest(initialization_parameters, initialization_headers,
                                       initialization_headers.get_headers(), self.request, self.requests_map)

        login_data = pre_request_obj.login()
        if not initialization_parameters.passwordEncryptionPubKey:
            logger.warning(f"The parameters required for the request are not set!")

            return {"status": False, "error": True}

        return {"status": True}

    def like(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self._make_request_post(self.requests_map["main_url"], self.requests_map["like"]["uri"], params,
                                           authorization_data)

        return response

    def flipping_tape(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self._make_request_post(self.requests_map["main_url"], self.requests_map["flipping_type"]["uri"],
                                           params,
                                           authorization_data)

        return response

    def subscribe(self, params: dict, authorization_data: dict) -> dict:
        """
        :param authorization_data: dict
        :param params: dict
        :return: dict
        """
        response = self._make_request_post(self.requests_map["main_url"], self.requests_map["subscribe"]["uri"], params,
                                           authorization_data)

        return response