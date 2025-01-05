#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument,
safe from MySQL injections
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query with parameterized query to prevent SQL injection
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                  (sys.argv[4],))

    # Fetch all rows
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
