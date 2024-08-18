#!/usr/bin/env python3


import os
from dotenv import load_dotenv

import pyowm

from datetime import datetime, timedelta


load_dotenv()

my_api_key = os.getenv('my_api_key')
owm = pyowm.OWM(my_api_key)
mgr = owm.weather_manager()
mgr_air = owm.airpollution_manager()


# Получить текущую погоду в вашем городе и вывести общее состояние
# погоды, скорость ветра, относительную влажность воздуха, температуру
# и температуру по ощущениям
def get_current_weather(city):
    observation = mgr.weather_at_place(city)
    weather = observation.weather

    print(f"Текущая погода в {city}:")
    print(f"Общее состояние погоды: {weather.detailed_status}")
    print(f"Скорость ветра: {weather.wind()['speed']} м/с")
    print(f"Относительная влажность воздуха: {weather.humidity}%")
    print(f"Температура: {weather.temperature('celsius')['temp']}°C")
    feels_like = weather.temperature('celsius')['feels_like']
    print(f"Температура по ощущениям: {feels_like}°C")


# Получить погоду в вашем городе на следующий день и вывести те же
# значения, что и в предыдущем пункте
def get_weather_tomorrow(city):
    forecast = mgr.forecast_at_place(city, '3h').forecast
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_date = tomorrow.date()
    for weather in forecast:
        if weather.reference_time('date').date() == tomorrow_date:
            print(f"Погода в {city} на следующий день:")
            print(f"Общее состояние погоды: {weather.detailed_status}")
            print(f"Скорость ветра: {weather.wind()['speed']} м/с")
            print(f"Относительная влажность воздуха: {weather.humidity}%")
            print(f"Температура: {weather.temperature('celsius')['temp']}°C")
            print(f"Температура по ощущениям: "
                  f"{weather.temperature('celsius')['feels_like']}°C")
            break


# Получить текущий индекс качества воздуха в Лондоне и вывести его
def get_air_quality_in_london():
    list_of_forec = mgr_air.air_quality_forecast_at_coords(51.507351, -0.127758)

    weather = list_of_forec[0]
    print(f"Текущий индекс качества воздуха: { weather.aqi}")
    print(f"CO: { weather.co}")
    print(f"NO: { weather.no}")
    print(f"NO2: { weather.no2}")
    print(f"O3: { weather.o3}")
    print(f"SO2: { weather.so2}")
    print(f"PM2.5: { weather.pm2_5}")
    print(f"PM10: { weather.pm10}")
    print(f"NH3: { weather.nh3}")


def main():
    city = input('Введите название города: ')
    get_current_weather(city)
    print('\n')
    get_weather_tomorrow(city)
    print('\n')
    get_air_quality_in_london()


if __name__ == '__main__':
    main()
