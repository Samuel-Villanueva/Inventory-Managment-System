'''
===========
services.py
===========

'''

from app.repositories.category_repository import CategoryRepository
from app.services.category_service import CategoryService
from fastapi import Depends

from app.dependencies.repositories import get_category_repository

def get_category_service(
    repository: CategoryRepository = Depends(get_category_repository)
    
):
    return CategoryService(repository)