from settings import instadata


class InitHeaders:

    def __init__(self):
        self.initialization_headers = dict()
        self.default_headers = instadata.DEFAULT_HEADERS
        self.make_headers()

    def get_headers(self) -> dict:
        return self.initialization_headers

    def make_headers(self):
        self.initialization_headers["User-Agent"] = instadata.USER_AGENT
        self.initialization_headers["Content-Length"] = 288
        self.initialization_headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        self.initialization_headers["Host"] = self.default_headers['Host']
        self.initialization_headers["Sec-Fetch-Site"] = 'same-origin'
        self.initialization_headers["Sec-Fetch-Mode"] = 'cors'
        self.initialization_headers["Sec-Fetch-Dest"] = 'empty'
        self.initialization_headers["Referer"] = 'https://www.instagram.com/'
        self.initialization_headers["Accept-Encoding"] = 'gzip, deflate, br'
        self.initialization_headers["Accept-Language"] = self.default_headers["Accept-Language"]
        self.initialization_headers["cookie"] = ''
        self.initialization_headers["x-csrftoken"] = ""  # csrftoken cookie
        self.initialization_headers["x-ig-app-id"] = ""
        self.initialization_headers["x-ig-www-claim"] = ""
        self.initialization_headers["x-requested-with"] = "XMLHttpRequest"

    def set_attribute_headers(self, key, value):
        self.initialization_headers[key] = value

    def get_attribute_headers(self, key):
        return self.initialization_headers[key]
