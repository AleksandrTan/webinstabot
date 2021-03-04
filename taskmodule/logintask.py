"""
Performs the task of implementing a login on a social network
Parameters and headers are pre-initialized. Prerequisites for initializing the device
and the login request itself are performed.
"""
import sys

from apimodule.systemapiwork import SystemApiRequests
from pprint import pprint
from logsource.logconfig import logger
from core.initheaders import InitHeaders
from core.initparams import InitParams


class LoginTask:
    """
    The first request to the api of instagram. If parameters csrftoken, mid, ig_did are passed,
    initialize InitParams, InitHeaders with existing ones, if not,
    after pre-requests, transfer them to the system api server.
    """

    def __init__(self, social_api, account_data: dict, individual_bot_id: int):
        self.social_api = social_api
        self.account_data = account_data
        self.individual_id = individual_bot_id

    def run(self, task_id: int, initialization_parameters: dict) -> dict:
        """
        Run task login
        :param initialization_parameters:
        :param task_id: int
        :return: dict
        """
        data = dict()
        initialization_parameters = self.initialization_parameters(initialization_parameters)
        initialization_headers = self.initialization_headers()

        # run pre-requests
        # these requests are desirable and in addition,
        # the request will allow you to get the parameter cookie - csrftoken, mid, ig_did from the api
        pre_requests = self.social_api.login(initialization_parameters, initialization_headers,
                                             initialization_headers.get_headers())
        print(self.social_api.request.cookies.get_dict(), 4000)
        if not pre_requests:
            sys.stdout.write(f"The parameters necessary for the further operation of the bot {self.individual_id} "
                             f"were not received.!!!")
            logger.warning(f"The parameters necessary for the further operation of the bot {self.individual_id} "
                           f"were not received.")

            return {"status": False}

        # check if params csrftoken, mid, ig_did are passed
        if initialization_parameters.mid and initialization_parameters.csrftoken:
            sys_report = SystemApiRequests(self.individual_id)
            # send report to api
            sys_report.task_report(task_id, data)
            return {
                "status": True, "initialization_parameters": initialization_parameters,
                "initialization_headers": initialization_headers
            }

        return {"status": False}

    def initialization_parameters(self, initialization_parameters: dict) -> object:
        """
        Initialization of account parameters for login request
        :return: dict
        """
        params = InitParams(self.account_data, initialization_parameters)
        return params

    def initialization_headers(self) -> object:
        """
        Initialization of headers parameters for login request
        :return: dict
        """
        headers = InitHeaders()
        return headers
