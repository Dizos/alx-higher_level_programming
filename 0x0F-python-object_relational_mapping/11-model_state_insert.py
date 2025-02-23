#!/usr/bin/python3
"""
Script that adds the State object "Louisiana" to the database hbtn_0e_6_usa
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

    # Create new State object
    new_state = State(name="Louisiana")

    # Add new state to session and commit
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close session
    session.close()
