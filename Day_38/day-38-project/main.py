import os
import requests

# API Variables
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_API_APP_ID = os.environ.get('NUTRITIONIX_API_APP_ID')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/28b8ecbf576dbb86c2335c6d97b52ee7/workoutTracker/workouts"

# DEFAULT VARIABLES
GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = 168.0
AGE = 23

def main():
    query = "ran 3 miles"
    parameters = {
        "query": query,
        "gender": GENDER,
        "weight_kg":WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age":"30"
    }
    
    headers = { 
        "x-app-id": NUTRITIONIX_API_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
        "x-remote-user-id": "0"
        }
    
    print("Making requests...")
    response = requests.post(NUTRITIONIX_ENDPOINT, params=parameters, headers=headers)
    print(response)

if __name__ == "__main__":
    main()