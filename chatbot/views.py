from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session

from .settings import get_authentication
from .models import User, MasterAuthentication


# Define the view functions
async def home():
    return {"message": "Welcome to the Home Page"}


async def create_user(request:Request, db: Session = Depends(get_authentication)):
    print('create user fn')
    query = db.query(MasterAuthentication).filter(MasterAuthentication.registration_id=='AGT_ADH000038').first()
    print(query)
    print(query.doc_status)
    hello = await request.json()
    print(hello)
    return {'status': 'Success'}