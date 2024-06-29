from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..hashing import Hash


router = APIRouter(
    tags=['Authentication']
)
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
 

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    username = db.query(models.User).filter(models.User.email == request.username).first()
    if not username:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")

    if not Hash.verify(username.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorect Password")

    ## Generate JWT Token and return 
    #     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(data={"sub": username.email})
    return {"access_token": access_token, "token_type": "bearer"}   


