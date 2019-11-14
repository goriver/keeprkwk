import requests, json

r = requests.get('https://kmuin.com/api/v1/notices/')
print(r.text)

