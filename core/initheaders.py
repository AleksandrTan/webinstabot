from settings import instadata


class InitHeaders:

    def __init__(self, params: object):
        self.initialization_headers = dict()
        self.params = params
        self.default_headers = instadata.DEFAULT_HEADERS
        self.make_headers()

    def get_headers(self) -> dict:
        return self.initialization_headers

    def make_headers(self):
        self.initialization_headers["User-Agent"] = instadata.USER_AGENT
        self.initialization_headers["Content-Length"] = 288
        self.initialization_headers["X-IG-WWW-Claim"] = 0
        self.initialization_headers["X-Instagram-AJAX"] = '63a87693d17'
        self.initialization_headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
        self.initialization_headers["Host"] = self.default_headers['Host']
        self.initialization_headers["X-CSRFToken"] = ''
        self.initialization_headers["X-IG-App-ID"] = 936619743392459
        self.initialization_headers["Sec-Fetch-Site"] = 'same-origin'
        self.initialization_headers["Sec-Fetch-Mode"] = 'cors'
        self.initialization_headers["Sec-Fetch-Dest"] = 'empty'
        self.initialization_headers["Referer"] = 'https://www.instagram.com/'
        self.initialization_headers["Accept-Encoding"] = 'gzip, deflate, br'
        self.initialization_headers["Accept-Language"] = self.default_headers["Accept-Language"]
        self.initialization_headers["Cookie"] = 'ig_did=1106BD6C-3DD6-4EBD-B353-05948C7AA16D; ' \
                                                'csrftoken=GmzQl4Y91OWXCP3Boce3AZRMHDAw8dKF; ' \
                                                'mid=YD-SiwAEAAELCH-p293ePwQOkApD; ig_nrcb=1'

    def set_attribute_headers(self, key, value):
        self.initialization_headers[key] = value
