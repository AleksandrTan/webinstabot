from seleniumwire import webdriver
import time

from logsource.logconfig import logger


def login(account_data, initialization_parameters, initialization_headers, initialization_cookies, requests_map):
    headers = dict()
    cookies = {}

    def interceptor(request):
        try:
            headers["x-ig-app-id"] = request.headers["X-IG-App-ID"]
            new = request.headers["Cookie"].split(';')
            for new_one in new:
                cooka = new_one.split('=')
                cookies[cooka[0].strip()] = cooka[1].strip()
        except AttributeError as error:
            pass

    # Create a new instance of the Chrome driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=10x10")
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

    driver.get(requests_map["main_url"])
    time.sleep(5)
    username_field = driver.find_element_by_name('username')
    password_field = driver.find_element_by_name('password')
    submit_elem = driver.find_element_by_tag_name('button')
    username_field.send_keys(account_data["username"])
    password_field.send_keys(account_data["password"])
    submit_elem.click()

    driver.request_interceptor = interceptor
    request = driver.wait_for_request(requests_map["login"]["uri"])
    headers["x-ig-www-claim"] = request.response.headers["x-ig-set-www-claim"]
    driver.close()
    headers["x-csrftoken"] = cookies["csrftoken"]

    set_cookies(initialization_cookies, cookies)
    set_headers(initialization_headers, headers, cookies)

    return {"status": True}


def set_cookies(initialization_cookies: object, cookies: dict):
    for cooks in cookies:
        setattr(initialization_cookies, cooks, cookies[cooks])


def set_headers(initialization_headers: object, headers: dict, cookies: dict):
    initialization_headers.set_attribute_headers("x-csrftoken", headers["x-csrftoken"])
    initialization_headers.set_attribute_headers("x-ig-www-claim", headers["x-ig-www-claim"])
    initialization_headers.set_attribute_headers("x-ig-app-id", headers["x-ig-app-id"])
    initialization_headers.set_attribute_headers("Cookie", cookies)
