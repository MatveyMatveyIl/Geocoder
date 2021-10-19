from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
import os

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'address.db'))
session = Session(bind=engine)

Base = declarative_base()


class Address(Base):
    __tablename__ = 'full_address'
    id = Column(Integer(), primary_key=True)
    country = Column(String(50), default='Россия')
    region = Column(String(50))
    city = Column(String(100), index=True)
    street = Column(String(100), index=True)
    house_number = Column(String(25))
    latitude = Column(String(50))
    longitude = Column(String(50))


# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
