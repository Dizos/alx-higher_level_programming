#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state from the database hbtn_0e_4_usa
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
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    # Fetch all rows
    cities = cursor.fetchall()

    # Print the cities in the required format
    print(", ".join([city[0] for city in cities]))

    # Close cursor and database connection
    cursor.close()
    db.close()
