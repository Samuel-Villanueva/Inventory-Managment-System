'''
==============
permissions.py
==============

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, String, Text, DateTime

from app.models.base_model import Base
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.role_permissions import RolePermissions

class Permissions(Base):
    __tablename__ = 'permissions'

    id: MappedColumn[int] = mapped_column(Integer, primary_key=True)
    name: MappedColumn[str] = mapped_column(String, unique=True)
    description: MappedColumn[str] = mapped_column(Text, nullable=True)
    created_at: MappedColumn[datetime] = mapped_column(DateTime, nullable=False)

    role_permissions: MappedColumn['RolePermissions'] = relationship(back_populates='permission')