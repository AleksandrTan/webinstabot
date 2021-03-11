"""
Performs the task of implementing a login on a social network
Parameters and headers are pre-initialized. Prerequisites for initializing the device
and the login request itself are performed.
"""
import sys

from apimodule.systemapiwork import SystemApiRequests
from logsource.logconfig import logger


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

    def run(self, task_id: int, initialization_parameters: object, initialization_headers: object,
            initialization_cookies: object) -> dict:
        """
        Run task login
        :param initialization_cookies: object
        :param initialization_headers: object
        :param initialization_parameters: object
        :param task_id: int
        :return: dict
        """
        sys.stdout.write("Task Login is running!\n")
        # run login
        # these requests are desirable and in addition,
        # the request will allow you to get the parameter cookie - csrftoken, mid, ig_did... from the api
        login_data = self.social_api.login(self.account_data, initialization_headers, initialization_cookies)

        # send report to api
        sys_report = SystemApiRequests(self.individual_id)
        sys_report.task_report(task_id, login_data)

        if not login_data:
            sys.stdout.write(f"The authorization process for the bot number {self.individual_id} was not correct.!!!"
                             f" Check the log file loging_fbi.log!\n")

            return {"status": False}

        # check if params csrftoken, mid, ig_did are passed
        if initialization_cookies.check_init_attributes():
            sys.stdout.write(f"Task Login completed work successfully!\n")
            return {"status": True}

        return {"status": False}
