import sys

MAIN_API_URL = "http://127.0.0.1:8000/apiapp/"
NEXT_TASK_URL = "bot/id/task/next/"
TASK_RESULT_DONE = "bot/id/task/ib/done/"
TASK_RESULT_FAIL = "bot/id/task/ib/fail/"
PATH_TO_CHROMEDRIVER = '/usr/bin/chromedriver' if sys.platform == "linux" else 'C:/Users/alext/Downloads/chromedriver_win32/chromedriver'