from app.database import db
from app.database import BaseModel
from sqlalchemy import Column, Integer, String, Float


class Product(BaseModel):
    __tablename__ = 'productos'
    name = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    category = Column(String(100), nullable=False)

    def __init__(self, name, description, price, amount, category):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
        self.category = category
