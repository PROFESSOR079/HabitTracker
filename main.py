import requests
from datetime import datetime

USERNAME = "professor079"
TOKEN = "hkjasdhjkh"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
   "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

create_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "30",
}

# response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)


update_pixel_endpoint = f"{create_pixel_endpoint}/{pixel_params["date"]}"

new_pixel_data = {
    "quantity": "45"
}

# response = requests.put(url=update_pixel_endpoint, json=new_pixel_data, headers=headers)


delete_pixel_endpoint = f"{create_pixel_endpoint}/{pixel_params["date"]}"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
