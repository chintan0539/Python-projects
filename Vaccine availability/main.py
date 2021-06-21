import requests
from datetime import date
import time

from twilio.rest import Client

COWIN_ENDPOINT = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
today = date.today()
d = today.strftime("%d-%m-%Y")

# Twilio data
account_sid = 'AC6f8d019d05c76a24871a4753f2b34999'
auth_token = '2e32cc9c765280232d824448241b042a'
client = Client(account_sid, auth_token)

cowin_params = {
    "district_id": "371",
    "date": d
}


def repeat():
    response = requests.get(COWIN_ENDPOINT, params=cowin_params)
    response.raise_for_status()

    data = response.json()['sessions']

    for location in data:
        if location['available_capacity'] > 0:
            loc_name = location["name"]
            pin = location["pincode"]
            fee = location["fee"]
            dose_1 = location["available_capacity_dose1"]
            dose_2 = location["available_capacity_dose2"]
            vaccine = location['vaccine']

            message = client.messages \
                .create(
                body=f"Alert: vaccine available:\nlocation: {loc_name}   pincode: {pin}\nfee: {fee}    vaccine: {vaccine}\n dose1: {dose_1}   dose2: {dose_2}",
                from_='+12023357029',
                to='+917769938811'
            )

while True:
    repeat()
    print("repeated")
    time.sleep(60)
