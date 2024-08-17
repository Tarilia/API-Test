#!/usr/bin/env python3


import os
from dotenv import load_dotenv

from geopy.geocoders import Nominatim

load_dotenv()


# Вывести полную информацию о введённом адресе полученную из API;
# На новой строке вывести ширину и долготу для заданного адреса;
# На новой строке отобразить необработанные данные, полученные из API.
my_user_agent = os.getenv('my_user_agent')
geolocator = Nominatim(user_agent=my_user_agent)
address = "1 Lenina Moscow Russia"
location = geolocator.geocode(address)

print("Полная информация о введённом адресе:")
print(location.address)
print(f"Широта: {location.latitude}")
print(f"Долгота: {location.longitude}")
print("Необработанные данные, полученные из API:")
print(location.raw)
