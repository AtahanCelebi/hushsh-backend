from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text




class Users(Base):
        __tablename__ = 'hushshUsers'
        id = Column(Integer, primary_key=True)
        nameSurname = Column(String(50), nullable=False)
        nickName = Column(String(15), nullable=False, unique=True)
        email = Column(String(15), nullable=False, unique=True)
        password = Column(String(15), nullable=False)
        #verified = Column(Boolean, default=False)
        #userRole = Column(Boolean, default=False)

