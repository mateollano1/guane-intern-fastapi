from fastapi import FastAPI,APIRouter
# from app.routers import dogs
# router = APIRouter()

app = FastAPI()


# app.include_router(dogs.router)
# app.include_router(
#     dogs.router,
#     prefix="/dog",
#     tags=["dog"],
#     responses={404: {"description": "Not found"}},
# )