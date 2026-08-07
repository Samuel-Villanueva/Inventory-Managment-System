'''
=============
audit_logs.py
=============

'''

from sqlalchemy.orm import Mapped, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, JSON, ForeignKey, Enum as EnumAlchemy, DateTime, UUID as PG_UUID

from app.models.base_model import Base
from app.models.users import Users

from enum import Enum
from datetime import datetime
from uuid import UUID

class Actions(str, Enum):
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'

class AuditLogs(Base):
    __tablename__ = 'audit_logs'

    id: Mapped[UUID] = mapped_column(PG_UUID, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey('users.id')
    )
    action: Mapped[Actions] = mapped_column(EnumAlchemy(Actions), nullable=False)
    entity: Mapped[str] = mapped_column(String, nullable=False)
    entity_id: Mapped[int] = mapped_column(Integer, nullable=False)
    ip: Mapped[str] = mapped_column(String, nullable=True)
    old_values: Mapped[dict] = mapped_column(JSON, nullable=False)
    new_values: Mapped[dict] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    user: Mapped['Users'] = relationship('Users', back_populates='logs')