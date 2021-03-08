"""
Settings file for queries to social networks API
"""

INSTAGRAM_WEB_DATA = {
    "main_url": "https://www.instagram.com/",
    # "main_url": "http://127.0.0.1:8000/",

    "login": {
        "uri": "https://www.instagram.com/accounts/login/ajax/",
        "password_field": "password",
        "username_field": "username",
    },

    "start_request": {
        "uri": "graphql/query/",
        "params": {"query_hash": "b1245d9d251dff47d91080fbdd6b274a",
                   "variables": {
                       "has_threaded_comments": True
                       }
                   }
        },

    "flipping_type": {
        "uri": "graphql/query/",
        "params": {"query_hash": "b1245d9d251dff47d91080fbdd6b274a",
                   "variables": {
                       "cached_feed_item_ids": [],
                       "fetch_media_item_count": 12,
                       "fetch_media_item_cursor": "",
                       "fetch_comment_count": 4,
                       "fetch_like": 3,
                       "has_stories": False,
                       "has_threaded_comments": True
                       }
                   }
        },

    "like": {
        "uri": "web/likes/post_id/like/",
    },

    "subscribe": {
        "uri": "api/subscribe/",
        "data": "",
        "params": ""
    }
}

# haches
# query_hash: ed2e3ff5ae8b96717476b62ef06ed8cc
# variables: {"fetch_media_count":0,"fetch_suggested_count":30,"ignore_cache":true,"filter_followed_friends":true,"seen_ids":[],"include_reel":true}

# query_hash: 003056d32c2554def87228bc3fd9668a
# variables: {"id":"7563037240","first":12}

# query_hash: b1245d9d251dff47d91080fbdd6b274a  данные пользователя + 12 постов(листать ленту) + хеш следующей страницы
# variables: {"cached_feed_item_ids":[],"fetch_media_item_count":12,
# "fetch_media_item_cursor":"KGEAQmUNaGNY_iLDjo0TAjcAIwMKDRAukgAjQ_YBUtxH_yJLgAHcCbX_Ig1KDqtaWAAjzQ6c7Hvp_yKUtAzkbf0AI6LeMagNawEjsZUvR93X_iI69-2L6x8AALz5sWHS2gEjFuKTgpaAXioUBAA=",
# "fetch_comment_count":4,"fetch_like":3,"has_stories":false,"has_threaded_comments":true}

var = {
    "data": {
        "user":
            {"id": "45540342156",
             "profile_pic_url": "https://instagram.fstv8-1.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fstv8-1.fna.fbcdn.net\u0026_nc_ohc=-U1ua_8bi5cAX_eMRzb\u0026oh=ea7d53f7ce1196b84943a5616c953763\u0026oe=606BC40F\u0026ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2",
             "username": "rumych423",
             "edge_web_feed_timeline":
                 {"page_info":
                      {"has_next_page": 'true',
                       "end_cursor": "KCcBDAAoABgAEAAQAAgACADdeo4m9l_m8Ngr__N__89vttYBa2BtIBAW4pOCloBeKhQEAA=="
                       },
                  "edges": []
                  }
             }
    }
}
