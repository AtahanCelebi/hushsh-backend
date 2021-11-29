from database import engine,Base
from models import User,WC,Profile,Rating


Base.metadata.create_all(bind=engine)
