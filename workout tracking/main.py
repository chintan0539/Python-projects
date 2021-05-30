import requests
from datetime import datetime

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
APP_ID = 'c6d19bca'
APP_KEY = '0b279f4c45460b799df4a6d9b457e7fe'

user_input = input("Tell me which exercises you did: ")

exersise_params = {
    'query': user_input,
    'gender': 'male',
    "weight_kg": '66',
    "height_cm": '169',
    "age": '18'

}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,

}

exersise_response = requests.post(url=exercise_endpoint, json=exersise_params, headers=headers)
data = exersise_response.json()
print(data)

# ********************************************* Google Sheets *********************************************
today_date = str(datetime.today().strftime('%d/%m/%Y'))
today_time = str(datetime.now().strftime("%H:%M:%S"))

sheety_endpoint = 'https://api.sheety.co/792686d16b6a8ae30a3ee598d8251b20/myWorkouts/workouts'
sheety_headers = {
    'Authorization': 'Basic Y2hpbnRhbjA1Mzk6Y2hpbnRhbjI3',
}
for exercise in data["exercises"]:
    sheet_inputs = {
        'workout': {
            'date': today_date,
            'time': today_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
    print(sheety_response.json())
