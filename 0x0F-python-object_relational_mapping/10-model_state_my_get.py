#!/usr/bin/python3
"""
 a script that prints the State object
  with the name passed as argument from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    passed_name = session.query(State).filter(State.name.like(sys.argv[4]))\
        .order_by(State.id).first()
    if passed_name:
        print("{}".format(passed_name.id))
    else:
        print("Not found")
    session.close()
