'''
===================
role_permissions.py
===================

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey, UUID as PG_UUID

from app.models.base_model import Base
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from app.models.roles import Roles
    from app.models.permissions import Permissions

class RolePermissions(Base):
    __tablename__ = 'role_permissions'

    role_id: MappedColumn[UUID] = mapped_column(
        ForeignKey('roles.id'), primary_key=True
    )

    permission_id: MappedColumn[UUID] = mapped_column(
        ForeignKey('permissions.id'), primary_key=True
    )

    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    role: MappedColumn['Roles'] = relationship(back_populates='role_permissions')
    permission: MappedColumn['Permissions'] = relationship(back_populates='role_permissions')