#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cur = db.cursor()
    cur.excute("SELECT * FROM states WHERE name LIKE '%N' ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
