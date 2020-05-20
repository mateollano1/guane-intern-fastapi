from sqlalchemy.orm import Session

from models import dog
from schema import dog as dog_schema

def create_dog(db: Session, dog: dog_schema.DogCreate):
    db_dog = dog.Dog(name=dog.name, picture = dog.picture, create_date = dog.create_date, is_adopted = dog.is_adopted )
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def get_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(dog.Dog).offset(skip).limit(limit).all()

def get_dog_by_id(db: Session, id):
    return db.query(dog.Dog).filter(dog.Dog.id == id).first()

def get_dog_by_name(db: Session, name):
    return db.query(dog.Dog).filter(dog.Dog.name == name).first()

def get_dogs_adopted(db: Session):
    return db.query(dog.Dog).filter(dog.Dog.is_adopted == False).all()