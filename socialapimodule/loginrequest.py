import sys
import time
from seleniumwire import webdriver

from logsource.logconfig import logger
import config


def login(account_data: dict, initialization_headers: object, initialization_cookies: object, requests_map: dict):
    headers = dict()
    cookies = {}

    def interceptor(request):
        try:
            headers["x-ig-app-id"] = request.headers["X-IG-App-ID"]
            new = request.headers["Cookie"].split(';')
            for new_one in new:
                cooka = new_one.split('=')
                cookies[cooka[0].strip()] = cooka[1].strip()
        except AttributeError as errors_inter:
            logger.warning(f"The authorization process was not correct.!!! Error - {errors_inter}")
            sys.stdout.write(f"Error {errors_inter}")

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--window-size=10x10")
        driver = webdriver.Chrome(executable_path=config.PATH_TO_CHROMEDRIVER, options=chrome_options)

        driver.get(requests_map["main_url"])
        time.sleep(5)
        username_field = driver.find_element_by_name(requests_map["login"]["username_field"])
        password_field = driver.find_element_by_name(requests_map["login"]["password_field"])
        submit_elem = driver.find_element_by_tag_name('button')
        username_field.send_keys(account_data["username"])
        password_field.send_keys(account_data["password"])
        submit_elem.click()

        driver.request_interceptor = interceptor
        request = driver.wait_for_request(requests_map["login"]["uri"])
        headers["x-ig-www-claim"] = request.response.headers["x-ig-set-www-claim"]
        driver.close()

        set_cookies(initialization_cookies, cookies)
        if set_headers(initialization_headers, headers, cookies):
            return {"status": True}

        return {"status": False}
    except Exception as errors:
        logger.warning(f"The authorization process was not correct.!!! Error - {errors}")

        return {"status": False}


def set_cookies(initialization_cookies: object, cookies: dict):
    for cooks in cookies:
        setattr(initialization_cookies, cooks, cookies[cooks])


def set_headers(initialization_headers: object, headers: dict, cookies: dict):
    try:
        initialization_headers.set_attribute_headers("x-csrftoken", cookies["csrftoken"])
        initialization_headers.set_attribute_headers("x-ig-www-claim", headers["x-ig-www-claim"])
        initialization_headers.set_attribute_headers("x-ig-app-id", headers["x-ig-app-id"])
        cookies_string = ''
        for cookie in cookies.items():
            cookies_string += cookie[0] + "=" + cookie[1] + "; "
        initialization_headers.set_attribute_headers("Cookie", cookies_string.rstrip())

        return True
    except KeyError as error:
        logger.warning(f"Some parameters from response (/login/ajax/) of instagram was not correct.!!! Error - {error}")

        return False
