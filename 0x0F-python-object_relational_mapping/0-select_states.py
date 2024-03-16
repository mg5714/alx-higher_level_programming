#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=password, db=database)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
