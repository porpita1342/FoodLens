#this program is used to confirm that the website actually works 

import requests
import json

url = "http://dummyserver-production-c59a.up.railway.app/webhook"


response = requests.get(url)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())

with open('webhook_response.json', 'w') as f:
    json.dump(response.json(), f, indent=2)

post_data = {"test": "from python"}
post_response = requests.post(url, json=post_data)
print("POST Response:", post_response.json())
