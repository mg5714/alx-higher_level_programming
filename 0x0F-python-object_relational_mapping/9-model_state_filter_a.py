#!/usr/bin/python3
"""lists all State objects contain letter a from database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_name),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()


    states_with_a = session.query(State)\
                    .filter(State.name.like('%a%'))\
                    .order_by(State.id)\
                    .all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
