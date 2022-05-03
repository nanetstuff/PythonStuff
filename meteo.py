import requests
import time
import hashlib
import datetime

BASE_URL = 'https://api.openweathermap.org/data/2.5'
BASE_URL2 = 'http://www.windguru.cz/upload/api.php'

param = {
"lat":38.8099681,
"lon":-9.2538553,
"units":"metric",
"appid":"bd1fcfcf277b408d5d7943d83c6fccf7"
}

while True:
    response = requests.get(f"{BASE_URL}/onecall", params=param).json()

    temp = response['current']['temp']
    humidity = response['current']['humidity']
    pressure = response['current']['pressure']
    wind_speed= response['current']['wind_speed']*1.94384449
    wind_deg = response['current']['wind_deg']


    uid = "DonaMariaCasa"
    stationPass ="CatWindAna2022#"

    dt = datetime.datetime.now()
    salt = dt.strftime("%m/%d/%Y, %H:%M:%S")

    str2hash = salt+uid+stationPass
    result = hashlib.md5(str2hash.encode())
    res = result.hexdigest()

    param2 = {
    "uid" : uid,
    "salt" :salt,
    "hash" : res,
    "wind_avg" : wind_speed,
    "wind_dir" : wind_deg,
    "temperature" : temp,
    "rh" : humidity,
    "mslp" : pressure
    }

    response2 = requests.get(f"{BASE_URL2}", params=param2)

    print (salt+ " " + str(temp) + " " + str(humidity) + " " + str(wind_speed) + " " + str(wind_deg) )
    time.sleep(60)







