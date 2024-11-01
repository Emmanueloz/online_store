from sqlalchemy import Column, Integer
from app.database import db


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
