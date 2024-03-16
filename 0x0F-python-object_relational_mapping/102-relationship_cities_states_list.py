#!/usr/bin/python3
"""List all City objects and corresponding State objects from database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_with_states = session.query(City).order_by(City.id).all()

    for city in cities_with_states:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
