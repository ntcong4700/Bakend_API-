import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import engine

from api.v1.router import router as api_v1_router
from database.connection import Base
from database.models import Base

Base.metadata.create_all(bind=engine)

logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    level=logging.DEBUG
)

tags_metadata = [
    {
        'name': 'users',
        'description': 'Operations related to user management.',
    },
    {
        'name': 'pictures',
        'description': 'Operations related to user pictures.',
    },
]

app = FastAPI(
    title="User & Picture API",
    version="1.0.0",
    openapi_tags=tags_metadata
)

origins = [
    'http://localhost',
    'http://localhost:8000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# route tất cả API version 1 vào /v1
app.include_router(
    api_v1_router,
    prefix='/v1',
)

if __name__ == '__main__':
    logging.info('App is up and running')
    uvicorn.run('app.main:app', host='0.0.0.0', port=8000, reload=True)
