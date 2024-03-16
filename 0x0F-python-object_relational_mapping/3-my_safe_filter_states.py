#!/usr/bin/python3
from sys import argv
import MySQLdb
import sqlalchemy

if __name__ == "__main__":

    host = "localhost"
    port = 3306
    search_name = sys.argv[4]

    db = MySQLdb.connect(
            host=host, port=port, user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (search_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
