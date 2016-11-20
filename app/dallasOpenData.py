import requests
import json

from app.services.dallas_service import dallas_service

url = "https://www.dallasopendata.com/resource/are8-xahz.json"

response = requests.get(url)
if response.status_code == 200:
	data = response.json()
	data_index = 0
	while True:
		try:
			create_police_call(data[data_index]["block"], data[data_index]["location"], data[data_index]["nature_of_call"], data[data_index]["date_time"])
		except KeyError:
			data_index += 1
		data_index += 1