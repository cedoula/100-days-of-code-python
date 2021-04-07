import datetime as dt

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.departure_airport_code = origin_airport
        self.destination_airport_code = destination_airport
        self.out_date = out_date
        self.return_date = return_date