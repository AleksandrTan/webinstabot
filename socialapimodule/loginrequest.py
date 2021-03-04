class LoginRequest:

    def __init__(self, account_data, initialization_parameters, initialization_headers, initialization_cookies,
                 requests_map):
        self.account_data = account_data
        self.params = initialization_parameters
        self.headers = initialization_headers
        self.initialization_cookies = initialization_cookies
        self.requests_map = requests_map

    def login(self) -> dict:
        pass