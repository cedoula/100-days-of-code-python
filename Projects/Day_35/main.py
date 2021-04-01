import requests
from key import weather_api_key

MY_LAT = 32.626827
MY_LNG = -97.401011
weather_api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": weather_api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=weather_api_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for i in range(12):
    if int(weather_data["hourly"][i]["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:       
    print("Bring an umbrella")

#Slice it
#weather_slice = weather_data["hourly"][:12]