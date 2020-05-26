import sqlite3

try:
    connection = sqlite3.connect("Path\\to\\database")
except sqlite3.Error as e:
    print(e, "\nMake sure to specify database location in connection.py")
