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
        # "uri": "graphql/web/likes/post_id/like/",
    },

    "subscribe": {
        "uri": "api/subscribe/",
        "data": "",
        "params": ""
    }
}