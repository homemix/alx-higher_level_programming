#!/usr/bin/python3

"""
 a python file that contains the
 class definition of a State and an instance Base = declarative_base()
"""
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}')


class State(Base):
    """
    class State that inherits from Base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,unique=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
