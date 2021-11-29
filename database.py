from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine=create_engine('postgresql://postgres:19981116@localhost/hushshWC8',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()