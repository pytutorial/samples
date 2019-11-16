''' chương trình để từ một bức ảnh, đọc lấy nội dung văn bản trong ảnh'''

import requests, json, base64  

url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBSut2ax6ct7NAMGELpAZ_bRxNVuDS-ZRU'

def docVanBan(file):
    with open(file, 'rb') as f:
        img = f.read()
        img_base64 = base64.b64encode(img)
        
    body = {"requests": [
        {
            "image": {"content" : f'{img_base64.decode("utf-8")}'},
            "features": [{"type": "DOCUMENT_TEXT_DETECTION"}]
            }
        ]}
    headers = {"Content-Type" : "application/json"}

    req = requests.post(url, data = json.dumps(body), headers = headers)
    obj = json.loads(req.text)
    return obj['responses'][0]['fullTextAnnotation']['text']

print(docVanBan('sample.jpg'))
