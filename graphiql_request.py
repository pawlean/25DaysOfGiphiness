import json
import requests
import os

from helpers import fallback_to_file

def get_profiles():
    token = os.environ["github_api_key"]

    headers = {'Authorization':'Bearer ' + token}
    query = '{ repository(owner: "paulienuh", name: "25DaysOfGiphiness") { collaborators(first: 20) {nodes {name login bio avatarUrl }}}}'
    r = requests.post('https://api.github.com/graphql', json.dumps({"query": query}), headers=headers)
    if r.status_code == 200:
        git_bios = r.json()["data"]["repository"]["collaborators"]["nodes"]
        return git_bios
    else:
        # fallback in case of API key error
        return fallback_to_file("git_bio.json")
