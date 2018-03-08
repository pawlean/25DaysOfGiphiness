import os
import re
import json

import requests

from helpers import fallback_to_file

def get_gifs(keyword="christmas"):

    def correct_url(wrong_url):
        return re.sub(r"media[0-9]", "i", wrong_url)

    params = {
        "api_key": os.getenv("giphy_api_key"),
        "q": keyword,
        "rating": "pg",
        "limit": 30
    }
    gif_res = requests.get("https://api.giphy.com/v1/gifs/search", params=params)
    if gif_res.status_code == 200:
        gif_json_res = gif_res.json()["data"]
        # super simple black list added based on manual inspection
        # to filter out duplicates
        black_list = ["decorating christmas tree GIF", "christmas GIF"]
        resp = [(correct_url(gif["images"]["fixed_width"]["url"]), gif["title"])
                for gif in gif_json_res if gif["title"] not in black_list][:25]
        return resp
    else:
        # fallback in case of API key error
        return fallback_to_file("gifs.json")
