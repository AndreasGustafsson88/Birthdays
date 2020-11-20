import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .db_settings import *

engine = db.create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}",
    echo=False
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


