from fastapi import FastAPI

app = FastAPI(title="OrderFlow Backend", version="1.0.0")


@app.get("/")
async def root():
    return {"message": "Welcome to OrderFlow Backend"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}