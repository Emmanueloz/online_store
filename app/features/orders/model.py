from app.database import db
from app.database.model import BaseModel
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta


class Order(BaseModel):
    __tablename__ = 'orders'

    user_id = Column(Integer, ForeignKey('users.id'))
    state = Column(String(10), default='pending')
    creation_date = Column(DateTime)
    delivery_date = Column(DateTime)
    total = Column(Float)

    user = relationship('User')
    items = relationship('OrderItem')

    def __init__(self, user_id, state, total):
        self.user_id = user_id
        self.state = state
        self.creation_date = datetime.now()
        self.delivery_date = datetime.now() + timedelta(days=14)
        self.total = total


class OrderItem(BaseModel):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('productos.id'))
    amount = Column(Integer)
    price = Column(Float)

    def __init__(self, order_id, product_id, amount, price):
        self.order_id = order_id
        self.product_id = product_id
        self.amount = amount
        self.price = price
