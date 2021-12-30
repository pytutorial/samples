from fastapi import FastAPI, Request
app = FastAPI()

@app.get('/hello1')
async def hello1(name: str=''):
    return {'message': 'Hello ' + name}

@app.get('/hello2')
async def hello1(request: Request):
    name = request.query_params.get('name', '')
    return {'message': 'Hello ' + name}
