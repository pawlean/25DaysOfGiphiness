import os
import re
import json

import requests

from helpers import fallback_to_file

def get_gifs(keyword="christmas"):

    def correct_url(wrong_url):
        return re.sub(r"media[0-9]", "i", wrong_url)

    params = {
        "api_key": os.environ["giphy_api_key"],
        "q": keyword,
        "limit": 25
    }
    gif_res = requests.get("https://api.giphy.com/v1/gifs/search", params=params)
    if gif_res.status_code == 200:
        gif_json_res = gif_res.json()["data"]
        resp = [(correct_url(gif["images"]["fixed_width"]["url"]), gif["title"])
                for gif in gif_json_res]
        return resp
    else:
        # fallback in case of API key error
        return fallback_to_file("gifs.json")
