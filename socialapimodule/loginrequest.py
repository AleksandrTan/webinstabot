class LoginRequest:

    def __init__(self, params: object, headers: object, headers_dict: dict, request: object, requests_map):
        self.params = params
        self.headers = headers
        self.headers_dict = headers_dict
        self.request = request
        self.requests_map = requests_map

    def login(self):
        pass