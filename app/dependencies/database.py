'''
=============
session_db.py
=============
'''

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

from typing import Generator
from app.core.config import config

engine = create_engine(
    url=config.DATABASE_URL,
    pool_size=10
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False
)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()