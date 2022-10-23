from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from fastapi import status
from schemas.user_schema import User, DisplayUser
from auth.oauth2 import oauth_schema

router = APIRouter(prefix='/user', tags=['user'])


# create User
@router.post('/create', response_model= DisplayUser, status_code=status.HTTP_201_CREATED)
def add_user(request: User, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get('/', response_model= List[DisplayUser])
def get_all_user(db: Session = Depends(get_db)):
    return db_user.user_all(db)


@router.get('/{user_id}', response_model=DisplayUser)
def get_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth_schema)):
    return db_user.user_by_id(db, user_id)


@router.put('/{user_id}')
def update_user_by_id(user_id, request: User,  db: Session = Depends(get_db), token: str = Depends(oauth_schema)):
    return db_user.updating_user(user_id, request, db)


@router.delete('/delete/{user_id}')
def deleting_by_id(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth_schema)):
    return db_user.deleting_user(user_id, db)

