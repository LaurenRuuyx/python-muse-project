import requests

url = "http://127.0.0.1:8000/current_player/swap"

response = requests.post(url)

response_json = response.json()

print(response_json)
print(type(response_json))


