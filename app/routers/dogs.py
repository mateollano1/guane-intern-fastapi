from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, FastAPI, HTTPException, BackgroundTasks
from app.database.database import SessionLocal, engine
from app.models import dog as dog_model
from app.schema import dog as dog_schema
from app.crud import dog as dog_crud
from pydantic import BaseModel
from app.workers.celery_app import celery_app

dog_model.Base.metadata.create_all(bind=engine)
router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def celery_on_message(body):
    print(body)

def background_on_message(task):
    print(task.get(on_message=celery_on_message, propagate=False))

@router.post("/dogs/{name}",tags=["Dogs"])
def create_dog(name: str,db: Session = Depends(get_db)):
    task = celery_app.send_task(
        "app.workers.post_worker.create_dog", args=[name])
    return {"message": "dog information received"}


@router.get("/dogs",tags=["Dogs"],response_model=List[dog_schema.Dog])
async def get_dogs(db: Session = Depends(get_db)):
    dogs = dog_crud.get_dogs(db)
    return dogs

@router.get("/dogs/",tags=["Dogs"], response_model=dog_schema.Dog)
async def get_dog(id: str = "", name: str = "",db: Session = Depends(get_db)):
    if id != "":
        dogs = dog_crud.get_dog_by_id(db, id)
        return dogs
    elif name != "":
        dogs = dog_crud.get_dog_by_name(db, name)
        return dogs
    return

@router.get("/dogs/is_adopted",tags=["Dogs"], response_model=List[dog_schema.Dog])
async def get_dogs(db: Session = Depends(get_db)):
    dogs = dog_crud.get_dogs_adopted(db)
    return dogs

@router.put("/dogs/{id}/",tags=["Dogs"], response_model=dog_schema.Dog)
async def get_dog( dog:dog_schema.Dog, id,db: Session = Depends(get_db)):
    print (dog)
    dogs = dog_crud.update_dog_by_id(db, id,dog)
    return dogs

@router.delete("/dogs/",tags=["Dogs"], response_model=dog_schema.Dog)
async def get_dog(id: str = "", name: str = "",db: Session = Depends(get_db)):
    if id != "":
        dogs = dog_crud.delete_dog_by_id(db, id)
        return dogs
    elif name != "":
        dogs = dog_crud.delete_dog_by_name(db, name)
        return dogs
    return
