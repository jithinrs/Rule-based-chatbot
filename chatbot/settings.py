from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from sqlalchemy.orm import DeclarativeBase



load_dotenv(verbose=True, override=True)
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_URL = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/uat_ffms_authentication"
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

# Base = declarative_base()


class Base(DeclarativeBase):
    pass

Base.metadata.create_all(bind=engine)


def get_authentication():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
