'''
=============
audit_logs.py
=============

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, JSON, ForeignKey, Enum as EnumAlchemy, DateTime

from app.models.base_model import Base
from app.models.users import Users

from enum import Enum
from datetime import datetime

class Actions(str, Enum):
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'

class AuditLogs(Base):
    __tablename__ = 'audit_logs'

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    user_id: MappedColumn[int] = mapped_column(
        ForeignKey('users.id')
    )
    action: MappedColumn[Actions] = mapped_column(EnumAlchemy(Actions), nullable=False)
    entity: MappedColumn[str] = mapped_column(String, nullable=False)
    entity_id: MappedColumn[int] = mapped_column(Integer, nullable=False)
    ip: MappedColumn[str] = mapped_column(String, nullable=True)
    old_values: MappedColumn[dict] = mapped_column(JSON, nullable=False)
    new_values: MappedColumn[dict] = mapped_column(JSON, nullable=False)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    user: MappedColumn[Users] = relationship(back_populates='logs')