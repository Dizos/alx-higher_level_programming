#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
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

    # Format and execute the query using the provided state name
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(
        sys.argv[4])
    cursor.execute(query)

    # Fetch all rows
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
