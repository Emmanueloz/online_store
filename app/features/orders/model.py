from app.database import db
from app.database.model import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime


class Order(Base):
    __tablename__ = 'orders'

    user_id = Column(Integer, ForeignKey('users.id'))
    state = Column(String(10), default='pending')
    creation_date = Column(DateTime)
    delivery_date = Column(DateTime)
    total = Column(Float)


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    amount = Column(Integer)
    price = Column(Float)
