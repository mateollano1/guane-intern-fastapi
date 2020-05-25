from time import sleep
from sqlalchemy.orm import Session
from app.models import dog as dog_model
from app.schema import dog as dog_schema
from celery import current_task
from app.workers.celery_app import celery_app
from app.database.database import SessionLocal, engine
from app.crud import dog as dog_crud


@celery_app.task(acks_late=True)
def create_dog( name) -> str:
    db = SessionLocal()
    dog_crud.create_dog(name,db)
    db.close()
    sleep(5)
    return None