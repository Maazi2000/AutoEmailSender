import sqlite3

with sqlite3.connect("Database.db") as connection:
    cursor = connection.cursor()
    cursor.execute()