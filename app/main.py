from fastapi import FastAPI
from app.routers import oauth
from . import models
from app.db.database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(oauth.router)