Install packages:
    pip install "python-jose[cryptography]"
    pip install passlib
    pip install bcrypt

Start app:
    uvicorn --reload app:app

Test API: Go to http://127.0.0.1:8000/docs
    Get token:
        url: http://127.0.0.1:8000/token
        data (form-data): username=admin, password=admin

    Hello:
        url: http://127.0.0.1:8000/hello
        Authorization: Bearer, token=<token from above step>