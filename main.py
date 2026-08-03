'''
=======
main.py
=======


'''

from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    datefmt='%d-%m-%Y %H:%M:$S',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@asynccontextmanager
async def life_span(app: FastAPI):
    logging.info('Up server...')

    yield

    logging.info('Down server...')

app = FastAPI(lifespan=life_span)

@app.get(path='/')
def root():
    return {'message': 'welcome to root path'}