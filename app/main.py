from fastapi import FastAPI
from app.routers import dogs

app = FastAPI()

app.include_router(dogs.router)
app.include_router(
    dogs.router,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)