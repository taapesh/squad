import requests
import json

url = "https://www.dallasopendata.com/resource/are8-xahz.json"

response = requests.get(url)
if response.status_code == 200:
	data = response.json()
	data_index = 0
	#json_data = json.loads(str(data))
	#data = json.loads(response.text)
	#for d in data:
	#	print d.get("block")
	while True:
		try:
			print data[data_index]["block"]
			print data[data_index]["location"]
			print data[data_index]["date_time"]
			print data[data_index]["nature_of_call"] 
		except KeyError:
			data_index += 1
		data_index += 1