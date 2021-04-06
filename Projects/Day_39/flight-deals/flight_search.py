import requests
import datetime as dt
from keys import KIWI_API_KEY
TEQUILA_KIWI_ENDPOINT = "https://tequila-api.kiwi.com"

HEADERS = {"apikey": KIWI_API_KEY}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city

    def get_iata_code(self):
        global HEADERS
        search_params = {
            "term": self.city
        }
        response = requests.get(f"{TEQUILA_KIWI_ENDPOINT}/locations/query", params=search_params, headers=HEADERS)
        data = response.json()

        return data["locations"][0]["code"]

    def search_flights(self):
        global HEADERS
        flight_search_params = {
            "fly_from": "DFW",
            "fly_to": self.city,
            "date_from": (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d/%m/%Y'),
            "date_to": (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "USD"
        }
        
