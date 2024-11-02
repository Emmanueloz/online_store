from app.database.model import BaseModel
from sqlalchemy import Column, String, Integer


class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(500), nullable=False)
    role = Column(String(80), nullable=False)

    # directions
    street = Column(String(100))
    number = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    zip_code = Column(Integer)
    country = Column(String(100))
    neighborhood = Column(String(100))
    phone = Column(String(10))

    def __init__(self, username, email, password, role, street=None, number=None,
                 city=None, state=None, zip_code=None, country=None, neighborhood=None, phone=None):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self.street = street
        self.number = number
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country
        self.neighborhood = neighborhood
        self.phone = phone
