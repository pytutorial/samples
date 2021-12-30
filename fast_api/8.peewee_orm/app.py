from typing import List
from fastapi import FastAPI, Response, status
from db import *
from dto import *
from pydantic import ValidationError

app = FastAPI()

def dump_error(e: ValidationError):
    errors = {}

    for error in e.raw_errors:
        loc = error._loc
        message = str(error.exc)
        if loc not in errors:
            errors[loc] = []
        errors[loc].append(message)

    return errors

def copy_dict_to_object(data, obj, exclude_fields=[]):
    for k,v in data.items():
        if hasattr(obj, k) and k not in exclude_fields:
            setattr(obj, k, v)

@app.post('/category/')
async def create_category(data: dict, response: Response):
    try:
        dto = CategoryDto(**data)
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return dump_error(e)

    category = Category(**dto.dict())
    category.save()
    return CategoryDto.from_orm(category)
    
@app.put('/category/{id}/')
async def update_category(id: int, data: dict, response: Response):
    try:
        dto = CategoryDto(**data, id=id)
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return dump_error(e)

    category = Category.get(id)
    copy_dict_to_object(dto.dict(), category)
    category.save()
    return CategoryDto.from_orm(category)

@app.delete('/category/{id}/')
async def delete_category(id: int):
    category = Category.get(id)
    category.delete_instance()
    return {'success': True}

@app.get('/category/search', response_model=List[CategoryDto])
def search_category(keyword: str=''):
    return list(Category.select().where(
            Category.name.contains(keyword) |
            Category.code.contains(keyword)
        ))