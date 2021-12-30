Start app:
    uvicorn --reload app:app

Test API (using Postman/Rest Clients):
    POST:
        url: http://127.0.0.1:8000/sign-up
        data (json): {"username": "<username>", "password": "***", "password2": "****"}
