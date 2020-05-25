from sqlalchemy.orm import Session

from app.models import dog as dog_model
from app.schema import dog as dog_schema
from app.services import dog_picture_service as picture_service


def create_dog( name: str, db):
    dog = dog_schema.DogBase(name= name, picture = "")
    url_dog = picture_service.get_picture_url()
    db_dog = dog_model.Dog(name=dog.name, picture = url_dog, create_date = dog.create_date, is_adopted = dog.is_adopted )
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
    return db.query(dog_model.Dog).filter(dog_model.Dog.is_adopted == True).all()

def update_dog_by_id(db: Session, id, dog: dog_schema.DogCreate):
    dog_found = db.query(dog_model.Dog).filter(dog_model.Dog.id == id).first()
    dog_found.name = dog.name
    dog_found.is_adopted = dog.is_adopted
    dog_found.picture = dog.picture
    db.merge(dog_found)
    db.commit()
    return db.refresh(dog_found)

def delete_dog_by_id(db: Session, id):
    dog = db.query(dog_model.Dog).filter(dog_model.Dog.id== id).first()
    db.delete(dog)
    db.commit()
    return
    
def delete_dog_by_id(db: Session, id):
    dog = db.query(dog_model.Dog).filter(dog_model.Dog.id== id).first()
    db.delete(dog)
    db.commit()
    return

def delete_dog_by_name(db: Session, name):
    dog = db.query(dog_model.Dog).filter(dog_model.Dog.name== name).first()
    db.delete(dog)
    db.commit()
    return
    