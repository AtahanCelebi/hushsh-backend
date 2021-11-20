from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"atahan",
                "email":"atahancelebi98@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }



class Settings(BaseModel): #import secrets then prompt > secrets.token_hex()
    authjwt_secret_key:str='51b5c653373d4efe7e38cc705d07b301ff671b888383b429a147863c309806d0'


class LoginModel(BaseModel):
    username:str
    password:str


