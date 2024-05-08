# API key fb0810eec2de4b59b42200541240705
import sys
import requests
import json
from telegram import Update

def main():
    if len(sys.argv) != 2:
        sys.exit('Too many or too few arguments are given.')
    r = requests.get('https://api.weatherapi.com/v1/current.json?key=fb0810eec2de4b59b42200541240705&q=' + sys.argv[
        1] + '&aqi=no').json()
    formatted_r = json.dumps(r)
    return r







def location_func():
    loc = main()
    print(f"{loc['location']['name']} is located in {loc['location']['country']}.")
def wind_func():
    wind = main()
    print(f"Current wind is {wind['current']['wind_kph']}kph.")
    if wind['current']['wind_kph'] > 10:
        print('Strong wind for fishing.')
    elif 5 < wind['current']['wind_kph'] < 10:
        print('Wind is not so strong')
    else: print('This wind is perfect')
def temperature_func():
    temp = main()
    print(f"Now temperature is {temp['current']['temp_c']} C")
    print(f"Feels like {temp['current']['feelslike_c']}")
    if temp['current']['temp_c'] > 30:
        print('To high temperature. Not good for fishing.')
    elif 15 < temp['current']['temp_c'] < 30:
        print('Very good temperature for fishing.')
    else:
        print('It\'s a bit cold.')

def pressure_func():
    press = main()
    print(f"Now pressure is {press['current']['pressure_mb']} mb")
    if press['current']['pressure_mb'] > 1013:
        print('The pressure is a bit high')
    elif press['current']['pressure_mb'] < 1013:
        print('The pressure is a bit decreased.')
    else:
        print('The pressure is good.')







