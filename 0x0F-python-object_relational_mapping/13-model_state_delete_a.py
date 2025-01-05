#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing
the letter 'a' from the database hbtn_0e_6_usa
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

    # Query and delete states containing letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)

    # Commit the changes
    session.commit()

    # Close session
    session.close()
