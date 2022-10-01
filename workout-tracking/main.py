import requests
from datetime import datetime

GENDER = "male"
AGE = 32
WEIGHT = 75.0
HEIGHT = 176.0

APP_ID = "b272f09b"
APP_KEY = "197a9ef992e7f21b798bc461b882c505"
post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("what was your exercise")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

user_param = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}


response = requests.post(url=post_endpoint, json=user_param, headers=headers)
result = response.json()
print(result)
################################################################################
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result['exercises']:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise['name'].title(),
            "duration": exercise["duration_min"],
            "calories": exercise['nf_calories'],
        }
    }

header = {
    "Authorization": "Bearer wqewqewqewqewq"
}
print(sheet_input)
post_sheety_endpoint = "https://api.sheety.co/945910ca7ee851937e94aa321f5e90a0/myWorkouts/workouts"

sheet_response = requests.post(url=post_sheety_endpoint, json=sheet_input)
print(sheet_response.text)


