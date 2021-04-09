import requests
import datetime as dt
from keys import KIWI_API_KEY
from flight_data import FlightData
from pprint import pprint

TEQUILA_KIWI_ENDPOINT = "https://tequila-api.kiwi.com"

HEADERS = {"apikey": KIWI_API_KEY}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # def __init__(self, city):
    #     self.city = city

    def get_iata_code(self, city):
        global HEADERS
        search_params = {
            "term": city
        }
        response = requests.get(f"{TEQUILA_KIWI_ENDPOINT}/locations/query", params=search_params, headers=HEADERS)
        data = response.json()

        return data["locations"][0]["code"]

    def search_flights(self, origin_city_code, destination_city_code):
        global HEADERS
        flight_search_params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d/%m/%Y'),
            "date_to": (dt.datetime.now() + dt.timedelta(days=180)).strftime('%d/%m/%Y'),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(f"{TEQUILA_KIWI_ENDPOINT}/v2/search", params=flight_search_params, headers=HEADERS)
        try:
            data = response.json()["data"][0]
        except IndexError:
            flight_search_params["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_KIWI_ENDPOINT}/v2/search",
                headers=HEADERS,
                params=flight_search_params,
            )
            
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flight found for {destination_city_code}.")
                return None
            
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                data["price"], 
                data["route"][0]["cityFrom"], 
                data["route"][0]["flyFrom"], 
                data["route"][0]["cityTo"], 
                data["route"][0]["flyTo"], 
                data["route"][0]["local_departure"].split("T")[0], 
                data["route"][1]["local_departure"].split("T")[0]
            )

            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
        