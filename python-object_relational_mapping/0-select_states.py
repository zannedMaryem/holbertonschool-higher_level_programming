#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cur = db.cursor()
    # Query states sorted by id ascending
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Print results exactly as tuples
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
