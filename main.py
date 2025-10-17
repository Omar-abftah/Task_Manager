from fastapi import FastAPI
from config.settings import settings

from routers import tasks

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug
)

app.include_router(tasks.router)

@app.get('/')
def home():
    return {'message': 'Hello World'}
