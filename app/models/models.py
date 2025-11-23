# app/models/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False, default=0)
    qr_code_file = Column(String, nullable=True)  # مسیر نسبی داخل static/uploads


class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=0)
    action = Column(String, default="in")  # 'in' یا 'out'
    timestamp = Column(DateTime(timezone=True), server_default=func.now())