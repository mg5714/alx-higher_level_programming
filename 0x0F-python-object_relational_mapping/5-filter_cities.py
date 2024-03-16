#!/usr/bin/python3
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

    lt = []
    for city in cities:
        lt.append(city[1])
    print(", ".join(lt))

    cursor.close()
    db.close()
