from fastapi import APIRouter

router = APIRouter()

@router.get('/hello1')
async def hello1():
    return {'message': 'Hello 1'}