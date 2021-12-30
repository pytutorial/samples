from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post('/upload-file')
async def upload_file(image: UploadFile=File(...)):
    data = await image.read()
    with open(image.filename, 'wb') as fo:
        fo.write(data)

    return {'success': True}