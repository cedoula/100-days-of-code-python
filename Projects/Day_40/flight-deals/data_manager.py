import requests
from keys import sheety_endpoint, TOKEN, sheety_users_endpoint
from pprint import pprint

bearer_headers = {
    "Authorization": TOKEN
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self ):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(sheety_endpoint, headers=bearer_headers)
        data = sheet_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_code(self):
        for destination in self.destination_data:
            sheet_params = {
                "price": {
                    "iataCode": destination["iataCode"]
                }
            }
            response = requests.put(f"{sheety_endpoint}/{destination['id']}", json=sheet_params, headers=bearer_headers)
            print(response.text)
    
    def get_customer_emails(self):
        customers_endpoint = sheety_users_endpoint
        response = requests.get(customers_endpoint, headers=bearer_headers)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data