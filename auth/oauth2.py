from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import oauth2
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from db import db_user
from db.database import get_db
from db.models import DbUser

oauth_schema = oauth2.OAuth2PasswordBearer(tokenUrl='token')


SECRET_KEY = 'c649b53b63ac9e56fb7c319ffd91a7bf19e3a20cd1916b9f0b2f84d1f11bb79a'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRES_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_current_user(db: Session=Depends(get_db), token: str = Depends(oauth_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate Credentials.',
        headers={"WWW-Authenticat":"Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user: str = payload.get('sub')
        if user is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db_user.get_user_by_name(db , user)

    if user is None:
        raise credentials_exception
    print(user)
    return user
