#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db_name)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
