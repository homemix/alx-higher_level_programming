#!/usr/bin/python3

"""
a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa 
where name matches the argument
"""

import MySQLdb
import sys

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))

rows = cursor.fetchall()
for row in rows:
    print(row)