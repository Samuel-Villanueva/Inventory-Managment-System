'''
============
supplires.py
============

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, DateTime
from app.models.base_model import Base

from datetime import datetime

from app.models.products import Products

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    name: MappedColumn[str] = mapped_column(String, nullable=False)
    email: MappedColumn[str] = mapped_column(String, nullable=False, unique=True)
    phone: MappedColumn[str] = mapped_column(String, nullable=True)
    address: MappedColumn[str] = mapped_column(String, nullable=True)
    is_active: MappedColumn[bool] = mapped_column(Boolean, nullable=False)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    products: MappedColumn[Products] = relationship(back_populates='supplier')