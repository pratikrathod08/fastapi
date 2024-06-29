from fastapi import APIRouter, Depends, status, HTTPException
from .. import database, models, schemas 
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. repository import user


router = APIRouter(
    prefix="/user",
   tags=['Users']
)

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
get_db = database.get_db


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id:int,  db: Session = Depends(get_db)):
    return user.get_user(id, db)