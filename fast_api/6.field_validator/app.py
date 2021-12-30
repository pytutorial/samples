from fastapi import FastAPI, Response, status
from pydantic import BaseModel, validator, ValidationError

app = FastAPI()

class User(BaseModel):
    username: str
    password: str
    password2: str

    @validator('username')
    def validate_username(cls, value):
        if ' ' in value:
            raise ValueError('Username cannot contain blank character')
        
        return value

    @validator('password')
    def validate_password(cls, value):
        if len(value or '') < 6:
            raise ValueError('Password needs to contain at least 6 characters')

        if (value or '').isdigit():
            raise ValueError('Password cannot be all digits')

        return value

    @validator('password2')
    def validate_password2(cls, value, values, **kwargs):
        if "password" in values and value != values['password']:
            raise ValueError('Confirmation password does not match')

        return value

def dump_error(e: ValidationError):
    errors = {}

    for error in e.raw_errors:
        loc = error._loc
        message = str(error.exc)
        if loc not in errors:
            errors[loc] = []
        errors[loc].append(message)

    return errors

@app.post('/sign-up')
async def sign_up(data: dict, response: Response):
    try:
        user = User(**data)
        return {'success': True, 'user': user}
    except ValidationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return dump_error(e)
