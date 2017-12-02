#!/usr/bin/env python3

import my_git_token
import requests
import json

token = my_git_token.my_token()
pass1 = my_git_token.pass1()

headers = {'Authorization':'Bearer '+token}
print(headers)

query = '{ repository(owner: "paulienuh", name: "25DaysOfGiphiness") { collaborators(first: 20) {edges {node {name login bio bioHTML }}}}}'



r = requests.post('https://api.github.com/graphql', json.dumps({"query": query}), headers=headers)


git_bio = (r.json())

with open('git_bio.json', 'w') as outfile:
	json.dump(git_bio, outfile)
