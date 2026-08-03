'''
=============
categories.py
=============

'''

from app.models.base_model import Base
from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, DateTime

from app.models.products import Products

from datetime import datetime

class Categories(Base):
    __tablename__ = 'categories'

    id: MappedColumn[int] =  mapped_column(Integer, primary_key=True)
    name: MappedColumn[str] = mapped_column(String, nullable=False)
    description: MappedColumn[str] = mapped_column(Text, nullable=True)
    is_active: MappedColumn[bool] = mapped_column(Boolean, nullable=False)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    products: MappedColumn[Products] = relationship(back_populates='category')