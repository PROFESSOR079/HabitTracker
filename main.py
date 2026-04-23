import requests

USERNAME = "professor079"
TOKEN = "hkjasdhjkh"



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
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
   "X-USER-TOKEN": TOKEN
}

response = requests.post(
    url=graph_endpoint,
    json=graph_config,
    headers=headers)











