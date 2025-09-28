from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="OrderFlow Backend", version="1.0.0", lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome to OrderFlow Backend"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}