Start app:
    uvicorn --reload app:app

Test API: Go to http://127.0.0.1:8000/docs
    url: http://127.0.0.1:8000/sign-up
    data (json): {"username": "<username>", "password": "***", "password2": "****"}
