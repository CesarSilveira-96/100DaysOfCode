import requests
from datetime import datetime
import os

nutri_api_id = os.environ.get("NUTRI_API_ID")
nutri_api_key = os.environ.get("NUTRI_API_KEY")

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 177
AGE = 28

today = datetime.now()
formatted_date = today.strftime("%Y/%m/%d")
formatted_time = today.strftime("%H:%M:%S")

# >>>>>>>>>>>>>>>>>>>> Fetching info from nutritionix API <<<<<<<<<<<<<<<<<<<<<<<<<
exercise_info = {
    "query": input("Tell me which exercises you did today:\n"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id":nutri_api_id,
    "x-app-key":nutri_api_key
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url= exercise_endpoint, json=exercise_info, headers=headers)
data = response.json()
print (data)

# >>>>>>>>>>>>>>>>>>>> sending info to sheets through Sheety API <<<<<<<<<<<<<<<<<<<<<<<<<
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in data["exercises"]:
    sheety_params = {
        "workout":{
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration (min)": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json= sheety_params, headers=sheety_headers)

    print(sheety_response.text)