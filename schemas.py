from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    name_surname:Optional[str]
    gender: Optional[str]
    email:str
    password:str
    role:str


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "name_surname":"atahan çelebi",
                "username":"atahan",
                "email":"atahancelebi98@gmail.com",
                "password":"password",
                "gender":"NOT SPECIFIED",
                "role":"MEMBER"
            }
        }

class ProfileModel(BaseModel):
    id:Optional[int]
    name_surname:str
    avatar_picture:str
    gender:str
    email:str
    nickname:str
    role:str
    score:str



class Settings(BaseModel): #import secrets then prompt > secrets.token_hex()
    authjwt_secret_key:str='51b5c653373d4efe7e38cc705d07b301ff671b888383b429a147863c309806d0'


class LoginModel(BaseModel):
    username:str
    password:str

class WCModel(BaseModel):
    id:Optional[int]
    lat_long : int
    wc_name : str
    comment : str
    img1:str
    img2:str
    img3:str
    img4:str
    img5:str
    size:str
    price :int
    soap:bool
    smell :str
    if_i_not_a_customer:bool
    type:str
    hygen_point:int
    hand_dryer:bool
    toilet_paper:bool
    paper_towels:bool
    toilet_seat_cover:bool
    user_id:Optional[int]

    class Config:
        orm_mode =True
        schema_extra={
            "example":{
                "lat_long":1010,
                "wc_name":"yeniwc",
                "comment": "it was nice and clear!",
                "img1": "img1.png",
                "img2": "img2.png",
                "img3": "img3.png",
                "img4": "img4.png",
                "img5": "img5.png",
                "size": "MEDIUM",
                "price": 0,
                "soap": True,
                "smell": "MEDIUM",
                "if_i_not_a_customer": True,
                "type": "ALATURKA",
                "hygen_point": 7,
                "hand_dryer": True,
                "toilet_paper": True,
                "paper_towels": True,
                "toilet_seat_cover": False
            }
        }

class RatingModel(BaseModel):
    id:Optional[int]
    comment:str
    img1:str
    img2:str
    img3:str
    img4:str
    img5:str
    size:str
    price:int
    soap:bool
    smell:str
    not_customer : bool
    type: str
    hygen_point:int
    hand_dryer:bool
    toilet_paper:bool
    paper_towels:bool
    toilet_seat_cover:bool
    user_id: Optional[int]
    toilet_id : Optional[int]

    class Config:
        orm_mode = True
        schema_extra={
            "example":{
                "comment":"it was nice and clear!",
                "img1":"img1.png",
                "img2":"img2.png",
                "img3":"img3.png",
                "img4":"img4.png",
                "img5":"img5.png",
                "size":"MEDIUM",
                "price":0,
                "soap":True,
                "smell":"MEDIUM",
                "not_customer": True,
                "type":"ALATURKA",
                "hygen_point":7,
                "hand_dryer":True,
                "toilet_paper":True,
                "paper_towels":True,
                "toilet_seat_cover":False

            }
        }









