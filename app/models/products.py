'''
===========
products.py
===========

'''

from app.models.base_model import Base
from sqlalchemy import String, Integer, Numeric, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import MappedColumn, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.categories import Categories
    from app.models.suppliers import Suppliers
    from app.models.inventory_movements import InventoryMovements
    from app.models.order_details import OrderDetails

from datetime import datetime

class Products(Base):
    __tablename__ = 'products'

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    sku: MappedColumn[str] = mapped_column(String, unique=True)
    name: MappedColumn[str] = mapped_column(String, nullable=False)
    description: MappedColumn[str] = mapped_column(Text, nullable=True)
    purchase_price: MappedColumn[float] = mapped_column(Numeric, nullable=False)
    sale_price: MappedColumn[float] = mapped_column(Numeric, nullable=False)
    stock: MappedColumn[int] = mapped_column(Integer, nullable=False)
    minimum_stock: MappedColumn[int] = mapped_column(Integer, nullable=False)
    is_active: MappedColumn[bool] = mapped_column(Boolean, nullable=False)
    category_id: MappedColumn[int] =  mapped_column(
        ForeignKey('categories.id')
    )
    supplier_id: MappedColumn[int] =  mapped_column(
        ForeignKey('suppliers.id')
    )
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=True)

    category: MappedColumn['Categories'] = relationship(back_populates='products')
    supplier: MappedColumn['Suppliers'] = relationship(back_populates='products')
    inventory_movements: MappedColumn['InventoryMovements'] = relationship(back_populates='product')

    orders_details: MappedColumn['OrderDetails'] = relationship(back_populates='product')