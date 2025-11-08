import sys

import requests
import logging

def get_weather_temp(json_data):
    """
    :param json_data:
    :return: temp
    """
    temp = json_data['main']['temp']
    return temp

def get_wind_speed(json_data):
    """
    :param json_data:
    :return: wind_speed
    """
    wind_speed = json_data['wind']['speed']
    return wind_speed


def get_weather_data(json_data, city):
    """
    :param json_data: JSON data from weather api
    :param city:
    :return: weather data
    """
    description_of_weather = json_data['weather'][0]['description']
    temp = get_weather_temp(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = {
        'city': city,
        'description': description_of_weather,
        'wind_speed': wind_speed,
        'temp': temp,
    }
    return weather_details

def main():
    """
    Main function

    :return:
    """
    api_address = api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Sydney,au&appid=a10fd8a212e47edf8d946f26fb4cdef8&q='
    city = input("Please enter your city: ")
    unit_format = "&units=metric"
    final_url = api_address + city + unit_format
    # print(final_url)
    # proxies = {
    #     'http': '180.242.158.157:80',
    # }

    # logging.basicConfig(level=logging.DEBUG)
    # res = requests.get(final_url, proxies=proxies, timeout=10).json()
    res = requests.get(final_url).json()
    # print(res)
    weather_details = get_weather_data(res, city)
    print(weather_details)


if __name__ == '__main__':
    main()
    sys.exit(0)