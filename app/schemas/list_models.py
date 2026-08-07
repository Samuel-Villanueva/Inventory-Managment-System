'''
==============
list_models.py
==============

'''

from pydantic import Field, BaseModel
from typing import Generic, TypeVar

T = TypeVar('T', bound=BaseModel)

class ListModels(BaseModel, Generic[T]):

    items: list[T]
    page: int = Field(..., examples=[2])
    size: int = Field(..., examples=[10])
    total: int = Field(..., examples=[1500])