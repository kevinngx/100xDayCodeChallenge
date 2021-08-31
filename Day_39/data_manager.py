import requests
from requests.api import put

SHEETY_ENDPOINT = "https://api.sheety.co/28b8ecbf576dbb86c2335c6d97b52ee7/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
    
    def getSheetData(self):
        self.destination_data = requests.get(SHEETY_ENDPOINT).json()['prices'] 
        return self.destination_data

    def updateIataCodes(self):
        print(self.destination_data)
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }

            response = requests.put(
                SHEETY_ENDPOINT + "/" + str(row["id"]), 
                json=new_data
            )
            print(response.text)
            
