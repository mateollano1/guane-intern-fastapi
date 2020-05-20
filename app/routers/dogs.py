from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, FastAPI, HTTPException
from database.database import SessionLocal, engine
from models import dog as dog_model
from schema import dog as dog_schema
from crud import dog as dog_crud

dog_model.Base.metadata.create_all(bind=engine)
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/can/")
async def root(skip: int = 0, limit: int = 10):
    return {"message": skip,
            "limite": limit}@router.get("/can/")


@router.post("/dogs/{name}", response_model=dog_schema.Dog)
def create_dog(name: str,db: Session = Depends(get_db)):
    dog = dog_schema.DogBase(name= name, picture = "") 
    return dog_crud.create_dog(db, dog)


@router.get("/dogs", response_model=List[dog_schema.Dog])
async def get_dogs(db: Session = Depends(get_db)):
    dogs = dog_crud.get_dogs(db)
    return dogs

@router.get("/dogs/{id}", response_model=dog_schema.Dog)
async def get_dog(id,db: Session = Depends(get_db)):
    dogs = dog_crud.get_dog(db, id)
    return dogs

@router.get("/dogs/{id}", response_model=dog_schema.Dog)
async def get_dog(id,db: Session = Depends(get_db)):
    dogs = dog_crud.get_dog(db, id)
    return dogs

@router.get("/dogs/adopted", response_model=List[dog_schema.Dog])
async def get_dogs(db: Session = Depends(get_db)):
    dogs = dog_crud.get_dogs_adopted(db)
    return dogs