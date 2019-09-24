''' chương trình để từ một bức ảnh, đọc lấy nội dung văn bản trong ảnh'''

import requests, json, base64  

url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyDhAQHbiBhucBPHFw0hvaxh-k5pod6kZJs'

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
