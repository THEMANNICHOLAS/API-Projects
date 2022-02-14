import requests; import json
response = requests.get("https://api.kanye.rest/")
print(response.status_code)
print(response.json())