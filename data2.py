import requests
from datetime import datetime
import json

#Hussain's Key
#api_key = "5wNtcyoZ9FSgibsqLB4BaIci28IYGeG4"

#Hussain's Key 2.0
api_key = "eFUUh9cPRbIoQ5Z0ry7WzYxBBnXD0yRJ"

#Hussain's Key 3.0
#api_key = "RzWZd69tnFHqOdBdah9MxjbCoEZ0xKAA"

#Usman's Key
#api_key = "gSPiDvsqmJJfosaQTA8k9K5rHx47P9AD"

#Usmans Key 2.0
#api_key = "lUnDaYNmmHuLO9ibDM6VHuLIcG7MvgCk"

#Ali's Key
#api_key = "Mkz1VdPSG8r1BQrRh5LqCrwFJGPbwBAu"

#Ali's Key 2.0
#api_key = "EvqiutnUxNmpclMTayZ57T999eiNUznn"

# def main():
#     print("Welcome to the Weather App!")
#     print("Enter the city and country you want to know the weather of.")
#     city = input("City: ")
#     country = input("Country: ")
#     print(all_data(city, country))


# Cache to store API responses
cache = {}

#Ferenheit to Celcius
def f_to_c(fahrenheit_str):
    try:
        fahrenheit = float(fahrenheit_str)
        celsius = int((fahrenheit - 32) * 5 / 9)
        return str(celsius)
    except ValueError:
        return "Invalid input"

def json_file(c, n):
    save_to_json(all_data(c, n))

def all_data(city, country):
    response = {}
    city_id = location_key(city, country)

    forecast_data = get_forecast_data(city_id)  # Fetch 5-day forecast data once

    response["1st_day"] = {
        "day": date_to_day(currentday_date(forecast_data)),
        "date": currentday_date(forecast_data),
        "temperature_now": temperature_now(city_id),
        "minimum_temp": currentday_minimum_temp(forecast_data),
        "maximum_temp": currentday_maximum_temp(forecast_data),
        "weather_day": currentday_weather_day(forecast_data),
        "weather_night": currentday_weather_night(forecast_data)
    }
    
    response["2nd_day"] = {
        "day": date_to_day(secondday_date(forecast_data)),
        "date": secondday_date(forecast_data),
        "minimum_temp": secondday_minimum_temp(forecast_data),
        "maximum_temp": secondday_maximum_temp(forecast_data),
        "weather_day": secondday_weather_day(forecast_data),
        "weather_night": secondday_weather_night(forecast_data)
    }
    response["3rd_day"] = {
        "day": date_to_day(thirdday_date(forecast_data)),
        "date": thirdday_date(forecast_data),
        "minimum_temp": thirdday_minimum_temp(forecast_data),
        "maximum_temp": thirdday_maximum_temp(forecast_data),
        "weather_day": thirdday_weather_day(forecast_data),
        "weather_night": thirdday_weather_night(forecast_data)
    }
    response["4th_day"] = {
        "day": date_to_day(fourthday_date(forecast_data)),
        "date": fourthday_date(forecast_data),
        "minimum_temp": fourthday_minimum_temp(forecast_data),
        "maximum_temp": fourthday_maximum_temp(forecast_data),
        "weather_day": fourthday_weather_day(forecast_data),
        "weather_night": fourthday_weather_night(forecast_data)
    }
    response["5th_day"] = {
        "day": date_to_day(fifthday_date(forecast_data)),
        "date": fifthday_date(forecast_data),
        "minimum_temp": fifthday_minimum_temp(forecast_data),
        "maximum_temp": fifthday_maximum_temp(forecast_data),
        "weather_day": fifthday_weather_day(forecast_data),
        "weather_night": fifthday_weather_night(forecast_data)
    }

    return response

# It will make a JSON file from the dictionary we provide
def save_to_json(data, filename='weather_data.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Converting date to day
def date_to_day(date):
    current_year = datetime.now().year 
    date_with_year = f"{current_year}-{date}"
    date_str = datetime.strptime(date_with_year, "%Y-%m-%d")
    day_name = date_str.strftime("%A")
    return day_name

# Unique ID of the location of which we want to find the information
def location_key(city, country):
    # if "location" not in cache:
    location = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={api_key}&q={city}")
    i = location.json()
    for result in i:
        y = result["Country"]
        y = y["EnglishName"]
        if y == country:
            cache["location"] = result["Key"]
            break
    return cache["location"]

# Current temperature of any location
def temperature_now(id):
    # if "current_conditions" not in cache:
    x = requests.get(f"http://dataservice.accuweather.com/currentconditions/v1/{id}?apikey={api_key}")
    cache["current_conditions"] = x.json()
    y = cache["current_conditions"]
    z = int(y[0]["Temperature"]["Metric"]["Value"])
    return f"{z}°C"

# Fetch 5-day forecast data once
def get_forecast_data(id):
    # if "forecast" not in cache:
    forecast_url = requests.get(f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{id}?apikey={api_key}")
    cache["forecast"] = forecast_url.json()
    return cache["forecast"]

# Functions using forecast data
def currentday_date(forecast_data):
    return forecast_data["DailyForecasts"][0]["Date"][5:10]

def currentday_minimum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][0]["Temperature"]["Minimum"]
    return f"{f_to_c(temp['Value'])}°C"

def currentday_maximum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][0]["Temperature"]["Maximum"]
    return f"{f_to_c(temp['Value'])}°C"

def currentday_weather_day(forecast_data):
    return forecast_data["DailyForecasts"][0]["Day"]["IconPhrase"]

def currentday_weather_night(forecast_data):
    return forecast_data["DailyForecasts"][0]["Night"]["IconPhrase"]

def secondday_date(forecast_data):
    return forecast_data["DailyForecasts"][1]["Date"][5:10]

def secondday_minimum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][1]["Temperature"]["Minimum"]
    return f"{f_to_c(temp['Value'])}°C"

def secondday_maximum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][1]["Temperature"]["Maximum"]
    return f"{f_to_c(temp['Value'])}°C"

def secondday_weather_day(forecast_data):
    return forecast_data["DailyForecasts"][1]["Day"]["IconPhrase"]

def secondday_weather_night(forecast_data):
    return forecast_data["DailyForecasts"][1]["Night"]["IconPhrase"]

def thirdday_date(forecast_data):
    return forecast_data["DailyForecasts"][2]["Date"][5:10]

def thirdday_minimum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][2]["Temperature"]["Minimum"]
    return f"{f_to_c(temp['Value'])}°C"

def thirdday_maximum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][2]["Temperature"]["Maximum"]
    return f"{f_to_c(temp['Value'])}°C"

def thirdday_weather_day(forecast_data):
    return forecast_data["DailyForecasts"][2]["Day"]["IconPhrase"]

def thirdday_weather_night(forecast_data):
    return forecast_data["DailyForecasts"][2]["Night"]["IconPhrase"]

def fourthday_date(forecast_data):
    return forecast_data["DailyForecasts"][3]["Date"][5:10]

def fourthday_minimum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][3]["Temperature"]["Minimum"]
    return f"{f_to_c(temp['Value'])}°C"

def fourthday_maximum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][3]["Temperature"]["Maximum"]
    return f"{f_to_c(temp['Value'])}°C"

def fourthday_weather_day(forecast_data):
    return forecast_data["DailyForecasts"][3]["Day"]["IconPhrase"]

def fourthday_weather_night(forecast_data):
    return forecast_data["DailyForecasts"][3]["Night"]["IconPhrase"]

def fifthday_date(forecast_data):
    return forecast_data["DailyForecasts"][4]["Date"][5:10]

def fifthday_minimum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][4]["Temperature"]["Minimum"]
    return f"{f_to_c(temp['Value'])}°C"

def fifthday_maximum_temp(forecast_data):
    temp = forecast_data["DailyForecasts"][4]["Temperature"]["Maximum"]
    return f"{f_to_c(temp['Value'])}°C"

def fifthday_weather_day(forecast_data):
    return forecast_data["DailyForecasts"][4]["Day"]["IconPhrase"]

def fifthday_weather_night(forecast_data):
    return forecast_data["DailyForecasts"][4]["Night"]["IconPhrase"]

if __name__ == "__main__":
    json_file("Karachi", "Russia")
