'''
=========
router.py
=========
'''

from fastapi import APIRouter

from app.routes.category_route import category_route

router = APIRouter()

router.include_router(category_route)