import requests
from keys import alpha_api_key, newsapi_api_key, account_sid, auth_token
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#Get today, yesterday and day before yesterday dates
TODAY = dt.datetime.now()
prev_day = TODAY - dt.timedelta(days=1)
prev_day = prev_day.strftime('%Y-%m-%d')
second_prev_day = TODAY - dt.timedelta(days=2)
second_prev_day = second_prev_day.strftime('%Y-%m-%d')

#Retrieve stock value at closing hour yesterday and day before yesterday and get news if the delta is above +/- 5%
alpha_api_endpoint = "https://www.alphavantage.co/query"

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api_key,
    "sortBy": "publishedAt"
}

response = requests.get(alpha_api_endpoint, alpha_parameters)
response.raise_for_status()
data = response.json()
close_value_yesterday = float(data["Time Series (Daily)"][prev_day]["4. close"])
close_value_before_yesterday = float(data["Time Series (Daily)"][second_prev_day]["4. close"])

delta = abs(close_value_yesterday - close_value_before_yesterday)

if delta >= close_value_before_yesterday * 0.05:
    if close_value_yesterday - close_value_before_yesterday < 0:
        sign = "🔻"
    else:
        sign = "🔺"
    change_percent = round(delta / close_value_before_yesterday * 100)

    newsapi_api_endpoint = "https://newsapi.org/v2/everything"
    newsapi_parameters = {
        "apiKey": newsapi_api_key,
        "qInTitle": COMPANY_NAME
    }
    response = requests.get(newsapi_api_endpoint, newsapi_parameters)
    response.raise_for_status()
    data = response.json()["articles"]
    articles = data[:3]
    
    #Twilio client
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"""\n
            {COMPANY_NAME}: {sign}{change_percent}%
            Headline: {articles[0]["title"]}. 
            Brief: {articles[0]["description"]}.
            
            Headline: {articles[1]["title"]}. 
            Brief: {articles[1]["description"]}.

            Headline: {articles[2]["title"]}. 
            Brief: {articles[2]["description"]}.
            """,
        from_='+16788418412',
        to='+18324665667'
    )
    print(message.status)