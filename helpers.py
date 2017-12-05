import json

def fallback_to_file(file_name):
    with open(file_name, "r") as f:
        res = json.load(f)
    return res
