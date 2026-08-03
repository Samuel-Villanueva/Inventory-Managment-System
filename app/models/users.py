'''
========
users.py
========

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime

from datetime import datetime

from app.models.base_model import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.orders import Orders
    from app.models.autid_logs import AuditLogs

class Users(Base):

    __tablename__ = 'users'

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    username: MappedColumn[str] = mapped_column(String, nullable=False, unique=True)
    email: MappedColumn[str] = mapped_column(String, nullable=False, unique=True)
    password: MappedColumn[str] = mapped_column(String, nullable=False)
    is_active: MappedColumn[bool] = mapped_column(Boolean, nullable=False)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=True)

    orders: MappedColumn['Orders'] = relationship(back_populates='user')
    logs: MappedColumn['AuditLogs'] = relationship(back_populates='user')