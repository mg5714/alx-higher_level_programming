#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host=host, port=port, user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
