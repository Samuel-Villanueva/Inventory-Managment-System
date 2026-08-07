'''
===========
products.py
===========

'''

from app.models.base_model import Base
from sqlalchemy import String, Integer, Numeric, DateTime, Boolean, Text, ForeignKey, UUID as PG_UUID
from sqlalchemy.orm import Mapped, Mapped, mapped_column, relationship

from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from app.models.categories import Categories
    from app.models.suppliers import Suppliers
    from app.models.inventory_movements import InventoryMovements
    from app.models.order_details import OrderDetails

from datetime import datetime

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[UUID] = mapped_column(PG_UUID, primary_key=True)
    sku: Mapped[str] = mapped_column(String, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    purchase_price: Mapped[float] = mapped_column(Numeric, nullable=False)
    sale_price: Mapped[float] = mapped_column(Numeric, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    minimum_stock: Mapped[int] = mapped_column(Integer, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    category_id: Mapped[UUID] =  mapped_column(
        ForeignKey('categories.id')
    )
    supplier_id: Mapped[UUID] =  mapped_column(
        ForeignKey('suppliers.id')
    )
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    category: Mapped['Categories'] = relationship('Categories', back_populates='products')
    supplier: Mapped['Suppliers'] = relationship('Suppliers', back_populates='products')
    inventory_movements: Mapped['InventoryMovements'] = relationship('InventoryMovements', back_populates='product')

    orders_details: Mapped['OrderDetails'] = relationship('OrderDetails', back_populates='product')