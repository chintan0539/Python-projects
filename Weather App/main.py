import requests

api_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = '9dedff07518b32321d272593d1207321'
MY_LAT = 16.7028412
MY_LOG = 74.2405329

parameters = {
    'lat': MY_LAT,
    'lon': MY_LOG,
    'exclude': 'current,minutely,daily',
    'appid': api_key,

}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly'][:12]

for hour in weather_data:
    weather_id=hour['weather'][0]['id']
    if(weather_id<700):
        print('bring your umberalla')
        break
