Start app:
    uvicorn --reload app:app

Test API (using Postman/Rest Clients):
    POST: 
        url: http://127.0.0.1:8000/hello1
        data (json): {"name": "Nguyen Van A"}

    POST: 
        url: http://127.0.0.1:8000/hello2
        data (form-data): name=Nguyen Van A
    
    POST:
        url: http://127.0.0.1:8000/log-in
        data (json): {"username": "admin", "password": "admin"}
