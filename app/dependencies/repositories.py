'''
===============
repositories.py
===============

'''

from app.dependencies.database import get_db
from app.repositories.category_repository import CategoryRepository

from fastapi import Depends
from sqlalchemy.orm import Session

def get_category_repository(db: Session = Depends(get_db)):
    return CategoryRepository(db)