import requests

request_url = "https://api.chucknorris.io/jokes/random"

response = requests.get(request_url).json()

print(response['value'])