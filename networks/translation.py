''' chương trình dịch đoạn văn bản giữa 2 ngôn ngữ'''

import requests, json, base64  

url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyBSut2ax6ct7NAMGELpAZ_bRxNVuDS-ZRU'

data = {
        'q': '''What's the weather like?''',
        'source': 'en',
        'target': 'vi',
        'format': 'text'
}

headers = {"Content-Type" : "application/json"}
result = requests.post(url, data = json.dumps(data), headers = headers).text
obj = json.loads(result)
print(obj['data']['translations'][0]['translatedText'])

#obj = json.loads(req.text)
