'''
==================
base_repository.py
==================

'''

from app.models.base_model import Base
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError

class BaseRepository:

    def __init__(self, session: Session, model: type[Base]):
        self._session = session
        self._model = model

    def create(self, entity: Base) -> Base | None:
        try:
            self._session.add(entity)
            self._session.commit()
            self._session.refresh(entity)

            return entity
        except IntegrityError:
            self._session.rollback()

    def get_all(self, offset: int, limit: int) -> list[Base]:
        query = select(self._model).offset((offset - 1) * limit).limit(limit)

        return self._session.execute(query).scalars().all()

    def get_by_id(self, id: int):
        query = select(self._model).where(self._model.id == id)
        return self._session.execute(query).scalar_one_or_none()

    def count(self) -> int:
        query = select(func.count()).select_from(self._model)

        return self._session.execute(query).scalar_one()