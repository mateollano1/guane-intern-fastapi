from sqlalchemy.orm import Session

from models import dog as dog_model
from schema import dog as dog_schema

def create_dog(db: Session, dog: dog_schema.DogCreate):
    db_dog = dog_model.Dog(name=dog.name, picture = dog.picture, create_date = dog.create_date, is_adopted = dog.is_adopted )
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def get_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dog_model.Dog).offset(skip).limit(limit).all()

def get_dog_by_id(db: Session, id):
    return db.query(dog_model.Dog).filter(dog_model.Dog.id == id).first()

def get_dog_by_name(db: Session, name):
    return db.query(dog_model.Dog).filter(dog_model.Dog.name == name).first()

def get_dogs_adopted(db: Session):
    return db.query(dog_model.Dog).filter(dog_model.Dog.is_adopted == False).all()