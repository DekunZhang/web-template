import json

import requests

# GET request with multiple parameters
url = 'http://localhost:8080/'
params = {'message': 'Hello', 'name': 'John', 'age': 30}
response = requests.get(url, params=params)
print(response.text)

# POST request with multiple parameters
response = requests.post(url, data=params)
print(response.text)

response = requests.get(f"{url}json")
data = response.json()
print(data['message'])

data = {'message': 'Hello, world!'}
headers = {'Content-Type': 'application/json'}
response = requests.post(f"{url}json", headers=headers, data=json.dumps(data))
print(response.text)
