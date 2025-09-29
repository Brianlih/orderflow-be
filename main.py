from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.configs.database import init_db
from app.routers.v1 import restaurant_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="OrderFlow Backend", version="1.0.0", lifespan=lifespan)

# Include API routers
app.include_router(restaurant_router, prefix="/api/v1/restaurants", tags=["restaurants"])


@app.get("/")
async def root():
    return {"message": "Welcome to OrderFlow Backend"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}