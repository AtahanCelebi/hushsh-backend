from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User,WC
from schemas import WCModel
from database import Session , engine
from fastapi.encoders import jsonable_encoder

wc_router = APIRouter(
    prefix="/hushsh-wc",
    tags=["hushsh-wc"]
)

session = Session(bind=engine) #refers to our database.py

#home page access
@wc_router.get('/')
async def home(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required() #if the our hushsh user have his/her specific token!!!
                                                #then this page can be seen.
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )


    return {"message":"Welcome to hushsh.com Home Page"}

#wc add section
@wc_router.post('/add')
async def add_new_wc(sample:WCModel,Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )

    current_user = Authorize.get_jwt_subject()

    user = session.query(User).filter(User.username == current_user).first()

    newWC = WC(
        wc_size=sample.wc_size,
        score=sample.score,
        user_id = user.id,
        wc_status = "PENDING"
    )

    newWC.user = user

    session.add(newWC)

    session.commit()

    response = {
        "message": "New hushsh toilet has been successfully added!",
        "score":newWC.score,
        "wcSize":newWC.wc_size
    }

    return jsonable_encoder(response)