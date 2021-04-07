#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import  pprint
from flight_search import FlightSearch
from twilio.rest import Client
from keys import account_sid, auth_token, TWILIO_NUMBER, MY_NUMBER

ORIGIN_CITY_CODE = "DFW"
ORIGIN_CITY = "Dallas"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

#Check if iata code is missing in first city, if yes get the code and update the sheet
if sheet_data[0]["iataCode"] == '':
    for data in sheet_data:
        data["iataCode"] = flight_search.get_iata_code(data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_iata_code()

for destination in sheet_data:
    flight = flight_search.search_flights(ORIGIN_CITY_CODE, destination["iataCode"])
    if flight != None:
        if flight.price < destination["lowestPrice"]:
            #Twilio client
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"""\n
                    Low price alert!!!\n
                    Only ${flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.destination_city}-{flight.destination_airport_code},\n
                    from {flight.out_date} to {flight.return_date}.
                    """,
                from_= TWILIO_NUMBER,
                to= MY_NUMBER
            )
            print(message.status)