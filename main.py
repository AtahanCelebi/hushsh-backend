from os import stat
from fastapi import FastAPI,status,HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()
#python -m uvicorn main2:app --reload

oauthSchema=OAuth2PasswordBearer(tokenUrl="token")
@app.post("/token")
async def token_generate(form_data: OAuth2PasswordRequestForm= Depends()):
    return {"access_token":form_data.username,"token_type":"bearer"}
@app.get("/users/profile")
async def profile(token: str = Depends(oauthSchema)):
    return {
        "user":"HEllo!"
    }

class Users(BaseModel): #serializer
    nameSurname:str
    nickName:str
    email:str
    password:str

    class Config:
        orm_mode=True


db=SessionLocal()

@app.get('/all-users',response_model=List[Users],status_code=200)
def get_all_items():
    getUsers=db.query(models.Users).all()

    return getUsers

@app.get('/user/{user_id}',response_model=Users,status_code=status.HTTP_200_OK)
def get_an_item(user_id:int,token: str = Depends(oauthSchema)):
    getUser=db.query(models.Users).filter(models.Users.id==user_id).first()
    return getUser

@app.post('/users',response_model=Users,
        status_code=status.HTTP_201_CREATED)
def create_an_item(user:Users):
    db_user=db.query(models.Users).filter(models.Users.nickName==user.nickName).first()

    if db_user is not None:
        raise HTTPException(status_code=400,detail="Item already exists")



    new_user=models.Users(
        nameSurname=user.nameSurname,
        nickName=user.nickName,
        email=user.email,
        password=user.password
    )


    db.add(new_user)
    db.commit()

    return new_user

@app.put('/user/{user_id}',response_model=Users,status_code=status.HTTP_200_OK)
def update_an_item(user_id:int,user:Users):
    item_to_update=db.query(models.Users).filter(models.Users.id==user_id).first()
    item_to_update.nameSurname=user.nameSurname
    item_to_update.nickName=user.nickName
    item_to_update.email=user.email
    item_to_update.password=user.password

    db.commit()

    return item_to_update

@app.delete('/user/{user_id}')
def delete_item(user_id:int):
    item_to_delete=db.query(models.Users).filter(models.Users.id==user_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete