from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Books API", version="1.0.0")

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"msg": "Books API is running"}
