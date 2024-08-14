import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR OWM API KEY"
account_sid = "YOU TWILIO SID"
auth_token = "YOUR TWILIO TOKEN"

weather_params = {
    "lat": "YOUR LAT",
    "lon": "YOUR LON",
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='YOUR TWILIO NUMBER',
        body='NOTE',
        to='YOUR TWILIO Verified PHONE NUMBER'
    )
    print(message.status)
