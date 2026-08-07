'''
=================
category_route.py
=================

'''

from fastapi import APIRouter, Depends
from app.schemas.category_schema import CategoryCreate, CategoryResponse
from app.dependencies.services import get_category_service

from app.services.category_service import CategoryService

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