from seleniumwire import webdriver
import time

from logsource.logconfig import logger


def login(account_data, initialization_parameters, initialization_headers, initialization_cookies, requests_map):

    headers = dict()
    cookies = {
        "csrftoken": 'csrftoken', "mid": 'mid', "ig_did": 'ig_did', "ds_user_id": 'ds_user_id',
        "sessionid": 'sessionid', "ig_nrcb": 'ig_nrcb', "rur": 'rur'}

    # def interceptor(request):
    #     try:
    #         new = request.headers["Cookie"].split(';')
    #         for new_one in new:
    #             cooka = new_one.split('=')
    #             cookies[cooka[0].strip()] = cooka[1].strip()
    #     except AttributeError as error:
    #         pass
    #
    # # Create a new instance of the Chrome driver
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--window-size=10x10")
    # driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    #
    # driver.get(requests_map["main_url"])
    # time.sleep(5)
    # username_field = driver.find_element_by_name('username')
    # password_field = driver.find_element_by_name('password')
    # submit_elem = driver.find_element_by_tag_name('button')
    # username_field.send_keys(account_data["username"])
    # password_field.send_keys(account_data["password"])
    # submit_elem.click()
    # driver.request_interceptor = interceptor
    # request = driver.wait_for_request(requests_map["login"]["uri"])
    # # print('-' * 50)
    # # print(request.body, request.headers, request.querystring, 80001)
    # # print('-' * 50)
    # # print('* response' * 50)
    # # print(request.response, request.response.headers, 9000)
    # # print('* response' * 50)
    # driver.close()

    set_cookies(initialization_cookies, cookies)
    set_headers(initialization_headers)

    return {"status": True}


def set_cookies(initialization_cookies: object, cookies: dict):
    for cooks in cookies:
        setattr(initialization_cookies, cooks, cookies[cooks])


def set_headers(initialization_headers: object):
    initialization_headers.set_attribute_headers("X-CSRFToken", "1234567yurjmgDFGDGHB")