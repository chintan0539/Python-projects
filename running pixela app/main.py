import requests
from datetime import datetime

USERNAME = 'chintan0539'
TOKEN='chintanpatel0539'
GRAPH_ID='graph01'
pixela_endpoint = 'https://pixe.la/v1/users'
userparam = {
    "token": "chintanpatel0539",
    "username": 'chintan0539',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response=requests.post(pixela_endpoint, json=userparam)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphParam = {
    'id': 'graph01',
    "name": "Running graph",
    "unit": 'km',
    'type': 'float',
    'color': 'kuro'

}
headers={
    'X-USER-TOKEN':TOKEN
}

# response=requests.post(url=graph_endpoint,json=graphParam,headers=headers)

# print(response.text)

pixelEndpoint=f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
today=datetime.today()
pixelParams={
    'date':str(today.strftime('%Y%m%d')),
    'quantity':'10',
}

response=requests.post(url=pixelEndpoint,json=pixelParams,headers=headers)
print(response.text)
