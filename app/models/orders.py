'''
=========
orders.py
=========

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, Numeric, DateTime, ForeignKey, UUID as PG_UUID

from datetime import datetime
from app.models.base_model import Base
from app.models.users import Users

from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from app.models.order_details import OrderDetails

class Orders(Base):
    __tablename__ = 'orders'

    id: MappedColumn[UUID] = mapped_column(PG_UUID, primary_key=True)
    customer_name: MappedColumn[str] = mapped_column(String, nullable=False)
    total: MappedColumn[float] = mapped_column(Numeric, nullable=False)
    status: MappedColumn[str] = mapped_column(String, nullable=False)
    created_by: MappedColumn[UUID] = mapped_column(
        ForeignKey('users.id')
    )
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    user: MappedColumn[Users] = relationship(back_populates='orders')
    orders_details: MappedColumn['OrderDetails'] = relationship(back_populates='order')