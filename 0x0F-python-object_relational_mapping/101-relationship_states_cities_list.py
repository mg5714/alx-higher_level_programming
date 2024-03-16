#!/usr/bin/python3
"""Lists all State objects and corresponding City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_cities = session.query(State).order_by(State.id).all()

    for state in states_with_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
