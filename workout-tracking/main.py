import requests
from datetime import datetime
import os

GENDER = "male"
AGE = 32
WEIGHT = 75.0
HEIGHT = 176.0

APP_ID = os.environ["APP_ID"]
#APP_ID = "b272f09b"
#APP_ID = os.environ.get("APP_ID")
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

################################################################################
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

exercise = result["exercises"][0]["name"].title()
duration = result["exercises"][0]['duration_min']
calories = result["exercises"][0]['nf_calories']
print(calories)

sheet_input = {
    "workout": {
    "date": date,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories,
    }
}


header1 = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
    # token wqewqewqewqewq
}

post_sheety_endpoint = "https://api.sheety.co/945910ca7ee851937e94aa321f5e90a0/myWorkouts/workouts"

sheet_response = requests.post(url=post_sheety_endpoint, json=sheet_input, headers=header1)
sheet_response.raise_for_status()
