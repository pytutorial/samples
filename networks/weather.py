import requests, json

#url = "http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8"
url = "http://api.openweathermap.org/data/2.5/weather?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9"
result = requests.get(url).text

data = json.loads(result)
print(json.dumps(data, indent=4))
