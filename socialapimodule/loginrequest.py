from logsource.logconfig import logger


class LoginRequest:

    def __init__(self, account_data, initialization_parameters, initialization_headers, initialization_cookies,
                 requests_map):
        self.account_data = account_data
        self.initialization_parameters = initialization_parameters
        self.initialization_headers = initialization_headers
        self.initialization_cookies = initialization_cookies
        self.requests_map = requests_map

    def login(self) -> dict:
        self.set_cookies()
        self.set_headers()

        return {"status": True}

    def set_cookies(self):
        self.initialization_cookies.csrftoken = "1234567"

    def set_headers(self):
        self.initialization_headers.set_attribute_headers("X-CSRFToken", "1234567yurjmgDFGDGHB")
