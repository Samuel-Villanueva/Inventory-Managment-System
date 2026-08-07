'''
==================
category_schema.py
==================

'''

from pydantic import Field, BaseModel, ConfigDict
from uuid import UUID
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str = Field(..., examples=['Samuel', 'Jacqueline'])
    description: str = Field(default=None, examples=['Dairy is...'])

class CategoryResponse(CategoryCreate):
    id: UUID = Field(...)
    is_active: bool = Field(..., examples=[True, False])
    created_at: datetime = Field(...)

    model_config = ConfigDict(from_attributes=True)