#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

# Retrieve data from datamanageer
data_manager = DataManager()
data_manager.getSheetData()

# Update codes if 
#data_manager.destination_data[0]["iataCode"] == "":
for row in data_manager.destination_data:
    if row["iataCode"] == "":
        row["iataCode"] = FlightSearch().getDestinationCode( row["city"] )
data_manager.updateIataCodes()