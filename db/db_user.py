from sqlalchemy.orm.session import Session

from db.hash import Hash
from db.models import DbUser
from schemas.user_schema import User


def create_user(db: Session, request: User):
    new_user = DbUser(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def user_all(db: Session):
    return db.query(DbUser).all()


def user_by_id(db : Session, user_id:int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()


def updating_user( user_id: int, request: User, db: Session):
    user = db.query(DbUser).filter(DbUser.id == user_id)
    user.update({
        DbUser.name: request.name,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'OK'


def deleting_user(user_id:int , db: Session):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    db.delete(user)
    db.commit()

    return f'{user_id} Deleted Successfully'