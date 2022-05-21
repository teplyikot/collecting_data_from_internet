import requests
import json

repos = 'https://api.github.com/users/teplyikot/repos'
response = requests.get(repos, auth=('teplyikot', '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'))
j_data = response.json()

for i in response.json():
    print(i['name'])

with open('repos.json', 'w') as f:
    json.dump(response.json(), f)

