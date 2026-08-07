'''
========
users.py
========

'''

from sqlalchemy.orm import Mapped, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime, UUID as PG_UUID

from datetime import datetime

from app.models.base_model import Base
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from app.models.orders import Orders
    from app.models.autid_logs import AuditLogs
    from app.models.user_roles import UserRoles

class Users(Base):

    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(PG_UUID, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    orders: Mapped[list['Orders']] = relationship('Orders', back_populates='user')
    logs: Mapped[list['AuditLogs']] = relationship('AuditLogs', back_populates='user')
    roles: Mapped[list['UserRoles']] = relationship('UserRoles', back_populates='users')