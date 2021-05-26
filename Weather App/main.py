import requests

from twilio.rest import Client
import os

api_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '9dedff07518b32321d272593d1207321'
MY_LAT = 22.373022
MY_LOG = 85.197174
account_sid = 'AC6f8d019d05c76a24871a4753f2b34999'
auth_token = '2e32cc9c765280232d824448241b042a'
parameters = {
    'lat': MY_LAT,
    'lon': MY_LOG,
    'exclude': 'current,minutely,daily',
    'appid': api_key,

}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly'][:12]
will_it_rain = False
for hour in weather_data:
    weather_id = hour['weather'][0]['id']
    if weather_id < 700:
        will_it_rain = True

if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It is going to rain today plz remember to get your Umbrella ☂️",
        from_='+12023357029',
        to='+917769938811'
    )

    print(message.status)
