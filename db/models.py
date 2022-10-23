from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String
from db.database import Base
from sqlalchemy import Column, ForeignKey


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    articles = relationship('DbArticle', back_populates='user')


class DbArticle(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("DbUser", back_populates='articles')
