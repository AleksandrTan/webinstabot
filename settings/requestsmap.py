"""
Settings file for queries to social networks API
"""

INSTAGRAM_WEB_DATA = {
    "main_url": "https://www.instagram.com",
    # "main_url": "http://127.0.0.1:8000/",

    "login": {
        "uri": "https://www.instagram.com/accounts/login/ajax/",
        "password_field": "password",
        "username_field": "username",
    },

    "flipping_type": {
        "uri": "api/flippingtape/",
        "data": "",
        "params": ""
    },

    "like": {
        "uri": "api/successlike/",
        "data": "",
        "params": ""
    },

    "subscribe": {
        "uri": "api/subscribe/",
        "data": "",
        "params": ""
    }
}
h = {'ig_did': 'A49DE7D1-CFD7-482D-9D74-8F851C43DAF6', 'csrftoken': 'APeSrNtoOcRY1podYQyZggoYbd2RxbZj',
     'mid': 'YEDyQwAEAAHpNCiccdHUmaALGyoe', 'ig_nrcb': '1', 'rur': 'VLL', 'ds_user_id': '45540342156',
     'sessionid': '45540342156%3A0m7rG6GooNOfGl%3A11'}
