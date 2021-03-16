"""
Bot tasks initialization class
"""
from taskmodule.logintask import LoginTask
from taskmodule.get_page_hash import PageHashTask
from taskmodule.flipping_tape import FlippingTapeTask
from taskmodule.liketask import LikeTask


class InitTasks:
    def __init__(self, individual_id, account_data, social_api):
        self.account_data = account_data
        self.individual_id = individual_id
        self.social_api = social_api
        self.task_objects = dict({"login": LoginTask(self.social_api, self.account_data, self.individual_id),
                                  "page_hash": PageHashTask(self.social_api, self.account_data, self.individual_id),
                                  "flipping_tape": FlippingTapeTask(self.social_api, self.account_data,
                                                                    self.individual_id),
                                  "like": LikeTask(self.social_api, self.account_data, self.individual_id),
                                  })

    def get_init_tasks(self):
        return self.task_objects
