from app.database.model import BaseModel
from sqlalchemy import Column, String


class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    role = Column(String(80), nullable=False)

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
