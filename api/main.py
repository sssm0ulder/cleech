from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from endpoints import task, user
from settings.configuration import init_db, ORIGINS


def create_application() -> FastAPI:
    application = FastAPI()
    return application


app = create_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(task.router)
app.include_router(user.router)

@app.get('/')
async def root():
    return {'message': 'Hello!'}


@app.on_event('startup')
async def startup_event():
    print('Starting up...')
    init_db(app)


@app.on_event('shutdown')
async def shutdown_event():
    print('Shutting down...')
