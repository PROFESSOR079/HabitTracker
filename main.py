import requests

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

pixel_params = {
    "date": "20260 223",
    "quantity": "31.25",
}

response = requests.post(url=create_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)







