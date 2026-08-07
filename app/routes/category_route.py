'''
=================
category_route.py
=================

'''

from fastapi import APIRouter, Depends, Query

from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.dependencies.services import get_category_service
from app.services.category_service import CategoryService
from app.schemas.list_models import ListModels

from typing import Annotated

category_route = APIRouter(
    prefix='/categories',
    tags=['Categories']
)

@category_route.post(
    path='/',
    name='create category',
    status_code=201,
    response_model=CategoryResponse
)
def create_category_route(
    data: CategoryCreate, 
    service: CategoryService = Depends(get_category_service)
) -> CategoryResponse:
    return service.create_category(data)

@category_route.get(
    path='/',
    name='list categories',
    status_code=200,
    response_model=ListModels[CategoryResponse]
)
def list_all_categories(
    page: Annotated[int, Query(ge=1)] = 1,
    size: Annotated[int, Query(ge=1, le=100)] = 10,
    service: CategoryService = Depends(get_category_service)
) -> ListModels[CategoryResponse]:
    return service.list_categories(page, size)