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
    sn = sys.argv[4]

    db = MySQLdb.connect(
            host=host, port=port, user=user, passwd=passwd, db=db_name)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.name FROM cities INNER JOIN states ON
            cities.state_id = states.id WHERE states.name = %s""", (sn,))

    cities = cursor.fetchall()

    qu = list(row[0] for row in cities)
    print(*qu, splet=", ")

    cursor.close()
    db.close()
