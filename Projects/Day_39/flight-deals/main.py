#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import  pprint
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

for data in sheet_data:
    if data["iataCode"] == '':
        flight_search = FlightSearch(data["city"])
        data["iataCode"] = flight_search.get_iata_code()
pprint(sheet_data)
data_manager.destination_data = sheet_data
data_manager.update_iata_code()