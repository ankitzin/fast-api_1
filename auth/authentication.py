from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth import oauth2
from db.database import get_db
from db.models import DbUser
from db.hash import Hash

router = APIRouter(
    tags=['authentication'],
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credential')
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credential')

    access_token = oauth2.create_access_token(data={
        'sub': user.name
    })

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'user_id': user.id,
        'username': user.name
    }