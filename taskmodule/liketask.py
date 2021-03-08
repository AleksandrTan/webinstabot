"""
Performs the task of implementing a like on a social network
"""
from apimodule.systemapiwork import SystemApiRequests


class LikeTask:

    def __init__(self, social_api, account_data: dict, individual_bot_id: int):
        self.social_api = social_api
        self.account_data = account_data
        self.individual_id = individual_bot_id

    def run(self, task_id: int, initialization_parameters: object, initialization_headers: object,
            initialization_cookies: object) -> dict:
        """
        Run task
        :param initialization_headers: object
        :param initialization_cookies: object
        :param initialization_parameters: object
        :param task_id: int
        :return: dict
        """
        data_result = self.social_api.like(initialization_parameters, initialization_headers, initialization_cookies)
        sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        sys_report.task_report(task_id, data_result)

        return data_result
