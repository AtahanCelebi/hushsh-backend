from fastapi import APIRouter,status,Depends
from fastapi.exceptions import HTTPException
from database import Session,engine
from schemas import SignUpModel,LoginModel,ProfileModel
from models import User,Profile
from fastapi.exceptions import HTTPException
from werkzeug.security import generate_password_hash , check_password_hash
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder


auth_router=APIRouter(
    prefix='/auth',
    tags=['auth']

)


session=Session(bind=engine)

@auth_router.get('/profile')
async def MyProfile(Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )


    current_user = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.username == current_user).first()
    return {"message":"Welcome %s"%(user.username),
            "email":user.email,
            "Your id":user.id,
            "Name Surname":user.name_surname
            }


@auth_router.post('/signup',
    status_code=status.HTTP_201_CREATED
)
async def signup(user:SignUpModel,profile:ProfileModel):

    db_email=session.query(User).filter(User.email==user.email).first()

    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the email already exists"
        )

    db_username=session.query(User).filter(User.username==user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with the username already exists"
        )
    new_user=User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        role=user.role,
        name_surname = user.name_surname,
        gender = user.gender

    )
    session.add(new_user)

    session.commit()


    new_profile=create_profil(new_user)
    session.add(new_profile)
    session.commit()

    return   "{Message:You successfully signup to hushsh.com}"       #new_user da dönebilirsin

def create_profil(db_user):
    new_profile = Profile(
        id=db_user.id,
        name_surname=db_user.name_surname,
        gender=db_user.gender,
        email=db_user.email,
        nickname=db_user.username,
        role=db_user.role
    )
    return new_profile

#login route

@auth_router.post('/login',status_code=200)
async def login(user:LoginModel,Authorize:AuthJWT=Depends()):
    """     
        ## Login a user
        This requires
            ```
                username:str
                password:str
            ```
        and returns a token pair `access` and `refresh`
    """
    db_user=session.query(User).filter(User.username==user.username).first()

    if db_user and check_password_hash(db_user.password, user.password):
        access_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_token(subject=db_user.username)

        response={
            "access":access_token,
            "refresh":refresh_token
        }

        return jsonable_encoder(response)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid Username Or Password"
    )

#refreshing tokens

@auth_router.get('/refresh')
async def refresh_token(Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_refresh_token_required()

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please provide a valid refresh token"
        ) 

    current_user=Authorize.get_jwt_subject()

    
    access_token=Authorize.create_access_token(subject=current_user)

    return jsonable_encoder({"access":access_token})

