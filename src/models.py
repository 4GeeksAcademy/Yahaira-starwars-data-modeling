import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    name = Column(String(50), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(70), nullable=False)
    password = Column(String(15), nullable=False)
    is_active = Column(Boolean)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    temperature = Column(Float)
    image_url = Column(String(250))
class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float)
    image_url = Column(String(250))

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = (String(200))
    birthday = Column(DateTime, nullable=False)
    image_url = Column(String(250))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)

class Favourite(Base):
    __tablename__ = "favourite"
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))



#class Person(Base):
   # __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
   # id = Column(Integer, primary_key=True)
    #name = Column(String(250), nullable=False)

#class Address(Base):
   # __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    #id = Column(Integer, primary_key=True)
   # street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
