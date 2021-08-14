# Bankstown Coordinates - https://www.latlong.net/
# Lat = -33.917301
# Lon = 151.035843

import requests
import json
import os
from twilio.rest import Client

# Weather API
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "2591ad19eed8a1b903ddad912a3023ed"

# SMS API
account_sid = "AC7e474ed4481f270b68d7f63731b526b5"
auth_token = "7ece2a3c260b5d5a818de14d110b5745"
client = Client(account_sid, auth_token)

weather_params = {
    "lat": -33,
    "lon": 151,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

# Write to output file
# oupput_file = open("output.txt","w")
# oupput_file.write(response.text)
# output = json.loads(response.text)

need_umbrella = False
weather_data = response.json()
weather_slice = weather_data["hourly"][0:11]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        need_umbrella = True

if need_umbrella == True:
    message_text = "It's going to rain today, bring an umbrella!" 
else:
    message_text = "Weather is clear today, go for a run!"
    
message = client.messages \
.create(
            body=message_text,
            from_='+16788537540',
            to='+61423495077'
        )
# Send message

print(message.sid)

# Get hourly weather id - https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# 2 = thunder, 