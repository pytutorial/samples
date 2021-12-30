from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.post('/hello1')
async def hello1(request: Request):
    data = await request.json()
    name = data.get('name', '')
    return {'message': 'Hello ' + name}

@app.post('/hello2')
async def hello2(request: Request):
    form = await request.form()
    name = form.get('name', '')
    return {'message': 'Hello ' + name}

class User(BaseModel):
    username: str
    password: str

@app.post('/log-in')
async def log_in(user: User):
    if user.username != 'admin' or user.password != 'admin':
        return {
            'success': False,
            'error': 'Incorrect username/password'
        }
    return {'success': True}
