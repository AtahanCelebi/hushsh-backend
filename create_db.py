from database import Base,engine
from models import Users

print("Creating database ....")

Base.metadata.create_all(engine)