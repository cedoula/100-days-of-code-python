import requests
from key import weather_api_key, account_sid, auth_token
from twilio.rest import Client


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
    #Twilio client
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's raining today. Remember to bring an ☔️.",
        from_='+16788418412',
        to='+18324665667'
    )
    print(message.status)
    print("rain")