from fastapi import APIRouter

router = APIRouter()

@router.get('/hello2')
async def hello1():
    return {'message': 'Hello 2'}