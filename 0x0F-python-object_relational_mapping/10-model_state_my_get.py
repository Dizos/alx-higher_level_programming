#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create connection to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                         pool_pre_ping=True)

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query State object with given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Display result
    if state is None:
        print("Not found")
    else:
        print(state.id)

    # Close session
    session.close()
