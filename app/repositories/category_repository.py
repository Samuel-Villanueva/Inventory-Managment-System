'''
======================
category_repository.py
======================

'''

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.repositories.base_repository import BaseRepository
from app.models.categories import Categories

class CategoryRepository(BaseRepository):

    def __init__(self, session: Session):
        super().__init__(session, Categories)

    def create(self, entity: Categories) -> Categories | None:
        return super().create(entity)

    def get_by_id(self, id: int) -> Categories | None:
        return super().get_by_id(id)