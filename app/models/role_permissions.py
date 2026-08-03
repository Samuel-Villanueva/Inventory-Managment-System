'''
===================
role_permissions.py
===================

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey

from app.models.base_model import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.roles import Roles
    from app.models.permissions import Permissions

class RolePermissions(Base):
    __tablename__ = 'role_permissions'

    role_id: MappedColumn[int] = mapped_column(
        ForeignKey('roles.id'), primary_key=True
    )

    permission_id: MappedColumn[int] = mapped_column(
        ForeignKey('permissions.id'), primary_key=True
    )

    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    role: MappedColumn['Roles'] = relationship(back_populates='role_permissions')
    permission: MappedColumn['Permissions'] = relationship(back_populates='role_permissions')