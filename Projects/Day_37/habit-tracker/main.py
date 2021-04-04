import requests
import datetime as dt
from keys import TOKEN

USER_NAME = "cedoula"
GRAPH_ID = "graph1"
date = dt.datetime.now().strftime('%Y%m%d')

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Workout Tracker",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

my_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_params = {
    "date": date,
    "quantity": input("How many hours did you workout today? ")
}

#response = requests.post(url=my_graph_endpoint, json=pixel_params, headers=headers)
#print(response.text)

pixel_update_endpoint = f"{my_graph_endpoint}/{date}"

pixel_update_params = {
    "quantity": "2"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_update_endpoint, headers=headers)
print(response.text)