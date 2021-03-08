"""
A class for making requests to the social network Instagram used mobile API
"""
from json.decoder import JSONDecodeError
import requests
import json

from logsource.logconfig import logger
from settings import requestsmap
from socialapimodule.loginrequest import login


class InstagramRequestsWeb:

    def __init__(self, host_proxy: str, port_proxy: int):
        self.request = requests.Session()
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.requests_map = requestsmap.INSTAGRAM_WEB_DATA

    def _make_request_post(self, main_url: str, uri: str, params: dict, headers: dict, cookies: dict) -> dict:
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
            except JSONDecodeError as error:
                logger.warning(f"Error decode json - {error}, {response}")
                return {"status": False, "error": True, "error_type": error, "error_message": data}

        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            logger.warning(f"Error login request {response.status_code}, {data}")

            return {"status": False, "error": True, "error_type": response.status_code}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"] == 'ok':
                return {"status": True, "data": data}

        return {"status": False, "error": True, "error_type": response.status_code}

    def _make_request_get(self, main_url: str, uri: str, params: dict, headers: dict, cookies: dict) -> dict:
        """
        :param headers:
        :param main_url: str
        :param uri: str
        :param params: dict
        :return: dict
        """
        data = dict()
        try:
            response = self.request.get(main_url + uri, params=params, headers=headers)
            try:
                data = response.json()
            except JSONDecodeError as error:
                logger.warning(f"Error decode json - {error}, {response}")
                return {"status": False, "error": True, "error_type": error, "error_message": data}

        except requests.exceptions.ConnectionError as error:
            logger.warning(f"{error}")
            return {"status": False, "error": True, "error_type": error}

        if response.status_code == 400:
            logger.warning(f"Error login request {response.status_code}, {data}")

            return {"status": False, "error": True, "error_type": response.status_code}

        if response.status_code == 200:
            data = json.loads(response.text)
            if data["status"] == 'ok':
                return {"status": True, "data": data}

        return {"status": False, "error": True, "error_type": response.status_code}

    def login(self, account_data: dict, initialization_headers: object, initialization_cookies: object) -> dict:
        """
        :param initialization_cookies: object
        :param initialization_headers: object
        :param account_data: dict
        :return: dict
        """
        pre_request_obj = login(account_data, initialization_headers, initialization_cookies, self.requests_map)

        if not pre_request_obj["status"]:
            logger.warning(f"The parameters required for the request are not set!")

            return {"status": False}

        return {"status": True}

    def page_hash_task(self, initialization_parameters: object, initialization_headers: object,
                       initialization_cookies: object) -> dict:
        """
        :param initialization_parameters: object
        :param initialization_cookies: object
        :param initialization_headers: object
        :return: dict
        """
        # prepare params for request
        request_data = dict()
        request_data["query_hash"] = self.requests_map["start_request"]["params"]["query_hash"]
        variables = self.requests_map["start_request"]["params"]["variables"]
        for key in variables:
            request_data[key] = variables[key]
        if initialization_parameters.fetch_media_item_cursor:
            request_data["fetch_media_item_cursor"] = initialization_parameters.fetch_media_item_cursor

        # request
        response = self._make_request_get(self.requests_map["main_url"], self.requests_map["start_request"]["uri"],
                                          request_data, initialization_headers.get_headers(),
                                          initialization_cookies.get_dict())

        return response

    def flipping_tape(self, initialization_parameters: object, initialization_headers: object,
                      initialization_cookies: object) -> dict:
        """
        :param initialization_parameters: object
        :param initialization_cookies: object
        :param initialization_headers: object
        :return: dict
        """
        # prepare params for request
        request_data = dict()
        request_data["query_hash"] = self.requests_map["start_request"]["params"]["query_hash"]
        variables = self.requests_map["start_request"]["params"]["variables"]
        for key in variables:
            request_data[key] = variables[key]

        if initialization_parameters.fetch_media_item_cursor:
            request_data["fetch_media_item_cursor"] = initialization_parameters.fetch_media_item_cursor

        # request
        response = self._make_request_get(self.requests_map["main_url"], self.requests_map["flipping_type"]["uri"],
                                          request_data, initialization_headers.get_headers(),
                                          initialization_cookies.get_dict())

        return response

    def like(self, initialization_parameters: object, initialization_headers: object,
             initialization_cookies: object) -> dict:
        """
        :param initialization_cookies: object
        :param initialization_parameters: object
        :param initialization_headers: object
        :return: dict
        """
        request_data = dict()
        post_id = initialization_parameters.get_post_id()
        if post_id:
            uri = self.requests_map["like"]["uri"].replace('post_id', str(post_id))
            response = self._make_request_post(self.requests_map["main_url"], uri, request_data,
                                               initialization_headers.get_headers(),
                                               initialization_cookies.get_dict())

            return response

        else:
            return {"status": False}

    def subscribe(self, initialization_parameters: object, initialization_headers: object,
                  initialization_cookies: object) -> dict:
        """
        :param initialization_headers:
        :param initialization_parameters:
        :param initialization_cookies:
        :return: dict
        """
        request_data = dict()
        response = self._make_request_post(self.requests_map["main_url"], self.requests_map["subscribe"]["uri"],
                                           request_data, initialization_headers.get_headers(),
                                           initialization_cookies.get_dict())

        return response
