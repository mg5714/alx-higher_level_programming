#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    host = "localhost"
    port = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host=host, port=port, user=username, passwd=password, db=db_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
