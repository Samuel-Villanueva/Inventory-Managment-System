'''
========
roles.py
========

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, Text, DateTime, UUID as PG_UUID

from app.models.base_model import Base
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from app.models.user_roles import UserRoles
    from app.models.role_permissions import RolePermissions

class Roles(Base):
    __tablename__ = 'roles'

    id: MappedColumn[UUID] = mapped_column(PG_UUID, primary_key=True)
    name: MappedColumn[str] = mapped_column(String, unique=True)
    description: MappedColumn[str] = mapped_column(Text, nullable=True)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    user_roles: MappedColumn['UserRoles'] = relationship(back_populates='role')
    role_permissions: MappedColumn['RolePermissions'] = relationship(back_populates='role')