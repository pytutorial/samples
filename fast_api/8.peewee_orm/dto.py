from typing import Optional
from pydantic import BaseModel, validator
from db import *

class CategoryDto(BaseModel):
    id: Optional[int]
    code: str
    name: str

    class Config:
        orm_mode = True

    @validator('code')
    def validate_code(cls, value, values, **kwargs):
        if Category.select().where(
            (Category.code == value) &
            (Category.id != values.get('id'))
        ).count() > 0:
            raise ValueError(f'Category with code "{value}" already exists')
        
        return value

class ProductDto(BaseModel):
    id: Optional[int]
    category_id: int
    code: str
    name: str
    price: int
    image_url: Optional[str]

    class Config:
        orm_mode = True

    @validator('code')
    def validate_code(cls, value, values, **kwargs):
        if Category.select().where(
            (Category.code == value) &
            (Category.id != values.get('id'))
        ).count() > 0:
            raise ValueError(f'Product with code "{value}" already exists')
        
        return value