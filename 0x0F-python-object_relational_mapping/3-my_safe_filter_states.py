#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    host = "localhost"
    port = 3306
    sch = sys.argv[4]

    db = MySQLdb.connect(
            host=host, port=port, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
            "SELECT * FROM states WHERE name LIKE %s", (sch, ))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
