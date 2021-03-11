"""
Performs the flipping tape of implementing a like on a social network
"""
import sys

from apimodule.systemapiwork import SystemApiRequests
from logsource.logconfig import logger

class PageHashTask:

    def __init__(self, social_api, account_data: dict, individual_bot_id: int):
        self.social_api = social_api
        self.account_data = account_data
        self.individual_id = individual_bot_id

    def run(self, task_id: int, initialization_parameters: object, initialization_headers: object,
            initialization_cookies: object) -> dict:
        """
        Run task
        :param initialization_parameters: object
        :param initialization_cookies: object
        :param initialization_headers: object
        :param task_id: int
        :return: dict
        """
        data_result = self.social_api.page_hash_task(initialization_parameters, initialization_headers,
                                                     initialization_cookies)
        if data_result["status"]:
            if data_result["data"]["status"] == 'ok':
                try:
                    initialization_parameters.fetch_media_item_cursor = \
                        data_result["data"]["data"]["user"]["edge_web_feed_timeline"]["page_info"]["end_cursor"]

                    initialization_parameters.has_next_page = \
                        data_result["data"]["data"]["user"]["edge_web_feed_timeline"]["page_info"]["has_next_page"]

                    # set posts id list
                    initialization_parameters.posts_id_list.clear()
                    for post_id in data_result["data"]["data"]["user"]["edge_web_feed_timeline"]["edges"]:
                        initialization_parameters.posts_id_list.append(str(post_id["node"]["id"]))
                except KeyError as error:
                    error_text = f"Some parameters from response of instagram (graphql/query/) was not correct.!!! Error - {error}"
                    logger.warning(error_text)
                    sys.stdout.write(error_text)

                    data_result["status"] = False

        sys_report = SystemApiRequests(self.individual_id)
        # send report to api
        sys_report.task_report(task_id, data_result)

        return data_result
