import requests
ENDPOINT_URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=ENDPOINT_URL)
response.raise_for_status()

data = response.json()
print(data["iss_position"]["longitude"])