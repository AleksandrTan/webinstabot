"""
Bot tasks initialization class
"""
from socialapimodule.instarequestweb import InstagramRequestsWeb
from taskmodule.logintask import LoginTask
from taskmodule.liketask import LikeTask
from taskmodule.flipping_tape import FlippingTapeTask


class InitTasks:
    def __init__(self, host_proxy, port_proxy, individual_id, account_data):
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.account_data = account_data
        self.individual_id = individual_id
        self.social_api = InstagramRequestsWeb(self.host_proxy, self.port_proxy)
        self.task_objects = dict({"login": LoginTask(self.social_api, self.account_data, self.individual_id),
                                  "like": LikeTask(self.social_api, self.account_data, self.individual_id),
                                  "flipping_tape": FlippingTapeTask(self.social_api, self.account_data,
                                                                    self.individual_id)})

    def get_init_tasks(self):
        return self.task_objects
