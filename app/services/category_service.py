'''
===================
category_service.py
===================

'''

from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.models.categories import Categories
from app.repositories.category_repository import CategoryRepository

from uuid import uuid4
from datetime import datetime
from zoneinfo import ZoneInfo
from app.core.config import config

class CategoryService:

    def __init__(self, repository: CategoryRepository):
        self._repository = repository

    def create_category(self, data: CategoryCreate) -> CategoryResponse:

        category = Categories(
            id=uuid4(),
            name=data.name,
            description=data.description,
            is_active=True,
            created_at=datetime.now(ZoneInfo(config.TIME_ZONE)),
        )

        category = self._repository.create(category)

        return CategoryResponse.model_validate(category)