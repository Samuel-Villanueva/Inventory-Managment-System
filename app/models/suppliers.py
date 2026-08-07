'''
============
supplires.py
============

'''

from sqlalchemy.orm import Mapped, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, Boolean, DateTime, UUID as PG_UUID
from app.models.base_model import Base

from datetime import datetime
from uuid import UUID

from app.models.products import Products

class Suppliers(Base):
    __tablename__ = 'suppliers'

    id: Mapped[UUID] = mapped_column(PG_UUID, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    address: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    products: Mapped[list['Products']] = relationship('Products', back_populates='supplier')