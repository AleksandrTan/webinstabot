"""
The class describes a bot object that simulates user behavior on the Instagram social network(Web version API).
It is launched from the worker process, initialized, and then, using api,
receives tasks that it performs, accompanying its work with logging at the database level,
a file on the standard output stream.
"""
import sys
import time
import random

from logsource.logconfig import logger
from taskmodule.inittask import InitTasks
from apimodule.systemapiwork import SystemApiRequests
from socialapimodule.instarequestweb import InstagramRequestsWeb
from core.initheaders import InitHeaders
from core.initcookies import InitCookies
from core.initparams import InitParams


class InstaBot:

    def __init__(self, host_proxy: str, port_proxy: int, social_api: object, system_api: object, individual_id: int,
                 account_data: dict, initialization_parameters: dict, login_task=True):
        """
        Bot object initialization
        :param host_proxy: str
        :param port_proxy: int
        :param social_api: object InstagramRequestsWeb or InstagramRequestsMobile
        :param system_api: object SystemApiRequests
        :param login_task: bool
        individual bot identifier
        :param individual_id: int
        :param account_data: dict
        :param initialization_parameters: dict
        """
        self.initialization_parameters = InitParams(initialization_parameters)
        self.initialization_headers = InitHeaders()
        self.initialization_cookies = InitCookies()
        self.individual_id = individual_id
        self.execution_status = True  # a flag that determines the state of the bot running shutdown
        self.login_task = login_task
        self.account_data = account_data
        self.host_proxy = host_proxy
        self.port_proxy = port_proxy
        self.social_api = social_api
        self.system_api = system_api
        tasks = InitTasks(self.host_proxy, self.port_proxy, self.individual_id, self.account_data)
        self.task_objects = tasks.get_init_tasks()

    def start(self):
        logger.warning(f"Bot {self.individual_id} start working!!!")
        # log in to the social network
        if self.login_task:
            sys.stdout.write("Task Login is running!\n")
            data_authorization = self._perform_task(self.task_objects['login'], 0)
            if not data_authorization['status']:
                sys.stdout.write(f"The authorization process for the bot"
                                 f" number {self.individual_id} was not correct.!!!"
                                 f" Check the log file loging_fbi.log!\n")
                logger.warning(f"The authorization process for the bot number {self.individual_id} was not correct.!!!")

                return False
            else:
                # run PageHashTask
                sys.stdout.write("Task PageHashTask is running!\n")
                data_authorization = self._perform_task(self.task_objects['page_hash'], 1)
                if not data_authorization['status']:
                    sys.stdout.write(f"The authorization process for the bot"
                                     f" number {self.individual_id} was not correct.!!!"
                                     f" Check the log file loging_fbi.log!\n")
                    logger.warning(
                        f"The authorization process for the bot number {self.individual_id} was not correct.!!!")

                    return False

        while self.execution_status:
            new_task = self._get_new_task()

            if new_task["status"]:
                # run new task
                sys.stdout.write(f"Task {new_task['task_name']} is running!\n")
                task_result = self._perform_task(self.task_objects[new_task['task_name']], new_task['task_id'])

                if task_result["status"]:
                    sys.stdout.write(f"Task {new_task['task_name']} completed work successfully!\n")
                    time.sleep(random.randint(5, 12))
                    continue
                else:
                    sys.stdout.write(f"Task {new_task['task_name']} completed work with an error, check the log file "
                                     f"loging_fbi.log!\n")
                return

            elif new_task["error"]:
                sys.stdout.write("Server error!!!\n")
                time.sleep(10)
                continue

            else:
                sys.stdout.write("No tasks, I work autonomously!\n")
                task_result = self._perform_task(self.task_objects["flipping_tape"], 2)
                if task_result["status"]:
                    time.sleep(random.randint(5, 12))
                    continue
                return None

    def _perform_task(self, task_object: object, task_id: int) -> dict:
        data_task = task_object.run(task_id, self.initialization_parameters, self.initialization_headers,
                                    self.initialization_cookies)

        return data_task

    def _get_new_task(self) -> dict:
        new_task = self.system_api.get_new_task()

        return new_task


if __name__ == "__main__":
    bot = InstaBot("http://localhost", 3500, InstagramRequestsWeb("http://localhost", 8000),
                   SystemApiRequests(1), 1, {"username": "Rumych423", "password": 'ufeltfvec'}, {"st": 1},
                   login_task=False)

    bot.start()
