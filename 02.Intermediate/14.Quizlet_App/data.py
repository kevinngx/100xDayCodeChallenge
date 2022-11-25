import requests
QUIZ_URL = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

request = requests.get(url=QUIZ_URL, params=PARAMETERS)
question_data = request.json()['results']