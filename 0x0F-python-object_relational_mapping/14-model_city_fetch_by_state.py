#!/usr/bin/python3
"""
Fetches and displays all City objects from the database hbtn_0e_14_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Take MySQL credentials and database name from command-line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]

    # Create database engine
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{db_name}", pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for all cities, joined with their respective states
    results = session.query(State.name, City.id, City.name).join(City).order_by(City.id).all()

    # Display results in the required format
    for state_name, city_id, city_name in results:
        print(f"{state_name}: ({city_id}) {city_name}")

    # Close the session
    session.close()

