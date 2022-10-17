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
