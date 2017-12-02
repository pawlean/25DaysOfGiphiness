import os
import re

import requests

def get_gifs(keyword="christmas"):

    def correct_url(wrong_url):
        return re.sub(r"media[0-9]", "i", wrong_url)

    params = {
        "api_key": os.environ["giphy_key"],
        "q": keyword,
        "limit": 25
    }
    gif_res = requests.get("https://api.giphy.com/v1/gifs/search", params=params).json()["data"]
    resp = [correct_url(gif["images"]["fixed_width"]["url"]) for gif in gif_res]
    return resp


if __name__ == '__main__':
    gifs = get_gifs()
    print(gifs, len(gifs))
