from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):

    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    name_surname = Column(String(100),nullable=True)
    gender = Column(String(15),nullable=False)
    role= Column(String(15),nullable=False)
    rel_rating = relationship("Rating",back_populates="rel_user")
    rel_wc = relationship("WC",back_populates = "rel_user")



    def __repr__(self):
        return f"<User {self.username}>"
class Profile(Base):
    GENDER = (
        ("MALE","male"),
        ("FEMALE","female"),
        ("NOT SPECIFIED","not specified")
    )


    __tablename__ = "profile"
    id = Column(Integer,primary_key=True)
    name_surname = Column(String(25),nullable=False)
    avatar_picture = Column(String(255),nullable=False,default="hushsh.png")
    gender = Column(ChoiceType(choices=GENDER),default="NOT SPECIFIED")
    email = Column(String,nullable=True)
    nickname = Column(String,nullable=True)
    role = Column(String,nullable=True)
    score = Column(Integer,default=0)



class WC(Base):
    TOILET_TYPE = (
        ("ALATURKA", "alaturka"),
        ("ALAFRANGA", "alafranga")
    )
    WC_SIZE_RATING = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large")
    )
    WC_SMELL_RATING = (
        ("LESS", "small"),
        ("MEDIUM", "medium"),
        ("TOO MUCH", "large")
    )

    __tablename__='toilet'
    id = Column(Integer,primary_key=True)
    lat_long = Column(Float,nullable=False)
    wc_name = Column(String,nullable=False)
    comment = Column(String(255), nullable=False)
    img1 = Column(String, nullable=False)
    img2 = Column(String, nullable=False)
    img3 = Column(String, nullable=False)
    img4 = Column(String, nullable=False)
    img5 = Column(String, nullable=False)
    size = Column(ChoiceType(choices=WC_SIZE_RATING), default="SMALL")
    price = Column(Integer, nullable=False)
    soap = Column(Boolean, nullable=False)
    smell = Column(ChoiceType(choices=WC_SMELL_RATING), default="LESS")
    if_i_not_a_customer = Column(Boolean, nullable=False)  # if the owners et you use your toilet or not
    type = Column(ChoiceType(choices=TOILET_TYPE), default="ALATURKA")  # alaturka, alafranga
    hygen_point = Column(Integer, nullable=False)  # 1 to 10 point
    hand_dryer = Column(Boolean, nullable=False)
    toilet_paper = Column(Boolean, nullable=False)
    paper_towels = Column(Boolean, nullable=False)
    toilet_seat_cover = Column(Boolean, nullable=False)
    user_id = Column(Integer,ForeignKey("user.id"))
    rel_user = relationship("User",back_populates="rel_wc")
    rel_WC =relationship("Rating",back_populates="rel_rating")




class Rating(Base):
    WC_SIZE_RATING = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large")
    )
    WC_SMELL_RATING = (
        ("LESS", "small"),
        ("MEDIUM", "medium"),
        ("TOO MUCH", "large")
    )
    WC_TYPE_RATING = (
        ("ALATURKA", "alaturka"),
        ("ALAFRANGA", "alafranga")
    )

    __tablename__ = 'rating'
    id = Column(Integer, primary_key=True)
    comment = Column(String(255), nullable=False)
    img1 = Column(String, nullable=False)
    img2 = Column(String, nullable=False)
    img3 = Column(String, nullable=False)
    img4 = Column(String, nullable=False)
    img5 = Column(String, nullable=False)
    size = Column(ChoiceType(choices=WC_SIZE_RATING),default="SMALL")
    price = Column(Integer,nullable=False)
    soap = Column(Boolean,nullable=False)
    smell = Column(ChoiceType(choices=WC_SMELL_RATING),default="LESS")
    not_customer = Column(Boolean,nullable=False)   #if the owners et you use your toilet or not
    type = Column(ChoiceType(choices=WC_TYPE_RATING),default="ALATURKA")    #alaturka, alafranga
    hygen_point = Column(Integer,nullable=False) #1 to 10 point
    hand_dryer = Column(Boolean,nullable=False)
    toilet_paper = Column(Boolean, nullable=False)
    paper_towels = Column(Boolean, nullable=False)
    toilet_seat_cover = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    toilet_id = Column(Integer,ForeignKey("toilet.id"))
    rel_user  = relationship("User", back_populates="rel_rating")
    rel_rating = relationship("WC",back_populates="rel_WC")



