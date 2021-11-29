from fastapi import APIRouter,Depends,status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User,WC,Rating
from schemas import WCModel,RatingModel
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

    current_user = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.username==current_user).first()
    getAll= session.query(WC).all()
    return {
        "message":"Welcome to hushsh.com Home Page",
    "flow":jsonable_encoder(getAll)}

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

    if str(user.role).lower() =="admin" or str(user.role).lower() == "moderator":
        newWC = WC(
            lat_long = sample.lat_long,
            wc_name = sample.wc_name,
            comment = sample.comment,
            img1 = sample.img1,
            img2 = sample.img2,
            img3 = sample.img3,
            img4 = sample.img4,
            img5 = sample.img5,
            size = sample.size,
            price = sample.price,
            soap = sample.soap,
            smell = sample.smell,
            if_i_not_a_customer = sample.if_i_not_a_customer,
            type = sample.type,
            hygen_point = sample.hygen_point,
            hand_dryer = sample.hand_dryer,
            toilet_paper = sample.toilet_paper,
            paper_towels = sample.paper_towels,
            toilet_seat_cover = sample.toilet_seat_cover,
            user_id = user.id
        )

        newWC.user = user

        session.add(newWC)

        session.commit()

        response = {
            "message": "New hushsh toilet has been successfully added!",
        }

        return jsonable_encoder(response)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are not a moderator"
    )
