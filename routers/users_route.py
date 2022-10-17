from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_user import create_user
from schemas.user_schema import User, DisplayUser
router = APIRouter(prefix='/user', tags=['user'])


# create User
@router.post('/create', response_model= DisplayUser)
def add_user(request: User, db: Session = Depends(get_db)):
    return create_user(db, request)
