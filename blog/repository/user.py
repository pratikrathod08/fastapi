from passlib.context import CryptContext
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
get_db = database.get_db



def create(request:schemas.User, db:Session):
    hashedpassword = pwd_cxt.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id:int, db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=400, detail=f"Blog with id {id} not availbale")
    return user