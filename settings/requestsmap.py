"""
Settings file for queries to social networks API
"""

INSTAGRAM_WEB_DATA = {
    # "main_url": "https://www.instagram.com",
    "main_url": "http://127.0.0.1:8000/",

    "login": {
        "uri": "accounts/login/ajax/",
        "data": "",
        "params": ""
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
