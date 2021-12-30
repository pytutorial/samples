Start app:
    uvicorn --reload app:app

Test API (using Postman/Rest Clients):
    POST: 
        url: http://127.0.0.1:8000/upload-file
        data (form-data): image=<image file>