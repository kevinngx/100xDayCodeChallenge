import requests
from datetime import datetime
from requests.models import Response

# https://pixe.la/@kevinngx
# https://pixe.la/v1/users/kevinngx/graphs/wkg.html

TOKEN = "thisissecret"
USERNAME = "kevinngx"

def main():
    graph_name = "Workout Tracker"
    graph_id = "wkg"
    
    #createUser()
    #createGraph(graph_name, graph_id)

    # Post
    date = getCurrentDate()
    quantity = 1
    postToGraph(graph_id, date, quantity)

def getCurrentDate():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    return year + month + day

def postToGraph(graph_id, date, quantity):
    endpoint = "https://pixe.la/v1/users/" + USERNAME + "/graphs/" + graph_id 
    post_params = {
        "date": date,
        "quantity": str(quantity)
    }

    headers = { "X-USER-TOKEN": TOKEN }
    response = requests.post(url=endpoint, json=post_params, headers=headers)
    print(response.text)


def createUser():
    endpoint = "https://pixe.la/v1/users"
    post_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=endpoint, json=post_params)
    print(response.text)

def createGraph(graph_name, graph_id):
    endpoint = "https://pixe.la/v1/users/" + USERNAME + "/graphs" 
    post_params = {
        "id": graph_id,
        "name": graph_name,
        "unit": "COMMIT",
        "type": "int",
        "color": "sora"
    }

    headers = { "X-USER-TOKEN": TOKEN }
    response = requests.post(url=endpoint, json=post_params, headers=headers)
    print(response.text)

if __name__ == "__main__":
    main()
    