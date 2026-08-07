'''
======================
inventory_movements.py
======================

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey, Enum as EnumAlchemy, UUID as PG_UUID

from datetime import datetime

from app.models.products import Products
from app.models.base_model import Base

from enum import Enum
from uuid import UUID

class MovementType(str, Enum):
    IN = "IN"
    OUT = "OUT"
    ADJUSTMENT = "ADJUSTMENT"

class MovementReason(str, Enum):
    PURCHASE = "PURCHASE"
    SALE = "SALE"
    RETURN = "RETURN"
    DAMAGE = "DAMAGE"
    ADJUSTMENT = "ADJUSTMENT"
    TRANSFER = "TRANSFER"

class ReferenceType(str, Enum):
    ORDER = "ORDER"
    PURCHASE = "PURCHASE"
    RETURN = "RETURN"
    MANUAL = "MANUAL"

class InventoryMovements(Base):
    __tablename__ = 'inventory_movements'

    id: MappedColumn[UUID] = mapped_column(PG_UUID, primary_key=True)
    product_id: MappedColumn[int] = mapped_column(
        ForeignKey('products.id')
    )
    user_id: MappedColumn[UUID] = mapped_column(
        ForeignKey('users.id')
    )
    movement_type: MappedColumn[MovementType] = mapped_column(EnumAlchemy(MovementType), nullable=False)
    quantity: MappedColumn[int] = mapped_column(Integer, nullable=True)
    previous_stock: MappedColumn[int] = mapped_column(Integer, nullable=False)
    new_stock: MappedColumn[int] = mapped_column(Integer, nullable=False)
    reason: MappedColumn[MovementReason] = mapped_column(EnumAlchemy(MovementReason), nullable=True)
    reference_type: MappedColumn[ReferenceType] = mapped_column(EnumAlchemy(ReferenceType), nullable=False)
    reference_id: MappedColumn[int] = mapped_column(Integer, nullable=True)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    product: MappedColumn[Products] = relationship(
        back_populates='inventory_movements'
    )