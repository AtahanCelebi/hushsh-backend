from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)
    rel = relationship("WC",back_populates="rel2")



    def __repr__(self):
        return f"<User {self.username}>"

class WC(Base):
    WC_STATUS = (
        ("PENDING","pending"),  #if user add a new toilet accepted or not!
        ("ACCEPTED","accepted")
    )

    WC_SIZE =(
        ("SMALL","small"),
        ("MEDIUM","medium"),
        ("LARGE","large")
    )

    __tablename__='tuvalet'
    id = Column(Integer,primary_key=True)
    score = Column(Integer,nullable=False)
    wc_status=Column(ChoiceType(choices=WC_STATUS),default="PENDING")
    wc_size=Column(ChoiceType(choices=WC_SIZE),default="SMALL")
    user_id = Column(Integer,ForeignKey("user.id"))
    rel2 =relationship("User",back_populates="rel")





