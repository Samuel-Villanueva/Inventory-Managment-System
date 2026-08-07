'''
================
order_details.py
================

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, Numeric, ForeignKey, UUID as PG_UUID

from app.models.base_model import Base
from app.models.products import Products
from app.models.orders import Orders

from uuid import UUID

class OrderDetails(Base):
    __tablename__ = 'order_details'

    id: MappedColumn[UUID] = mapped_column(PG_UUID, primary_key=True)
    order_id: MappedColumn[UUID] = mapped_column(
        ForeignKey('orders.id')
    )
    product_id: MappedColumn[UUID] = mapped_column(
        ForeignKey('products.id')
    )
    quantity: MappedColumn[int] = mapped_column(Integer, nullable=False)
    unit_price: MappedColumn[float] = mapped_column(Numeric, nullable=False)
    subtotal: MappedColumn[float] = mapped_column(Numeric, nullable=False)

    product: MappedColumn[Products] = relationship(back_populates='orders_details')
    order: MappedColumn[Orders] = relationship(back_populates='orders_details')