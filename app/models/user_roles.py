'''
=============
user_roles.py
=============

'''

from sqlalchemy.orm import MappedColumn, mapped_column, relationship
from sqlalchemy import Integer, DateTime, ForeignKey

from app.models.base_model import Base

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.users import Users
    from app.models.roles import Roles

class UserRoles(Base):
    __tablename__ = 'user_roles'

    user_id: MappedColumn[int] = mapped_column(
        ForeignKey('users.id'), primary_key=True
    )

    role_id: MappedColumn[int] = mapped_column(
        ForeignKey('roles.id'), primary_key=True
    )

    users: MappedColumn['Users'] = relationship(back_populates='roles')
    role: MappedColumn['Roles'] = relationship(back_populates='user_roles')