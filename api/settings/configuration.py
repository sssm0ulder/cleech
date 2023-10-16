import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


ORIGINS = [
    'http://localhost',
    'https://localhost',
    'http://localhost',
    'http://127.0.0.1',
    'https://127.0.0.1',
    'http://localhost:8080',
    'https://localhost:8080',
]

TORTOISE_ORM = {
    'connections': {
        'default': os.environ.get('DATABASE_URL')
    },
    'apps': {
        'models': {
            'models': [
                'models.__init__', 'aerich.models'
            ],
            'default_connection': 'default',
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get('DATABASE_URL'),
        modules={'models': ['models.__init__']},
        generate_schemas=False,
        add_exception_handlers=True,
    )
