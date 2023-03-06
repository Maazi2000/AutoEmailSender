import sqlite3
from database import Database

connection = sqlite3.Connection('Database.db')

with Database(connection) as database:
    database.cursor.execute('''CREATE TABLE borows(
        id integer primary key autoincrement,
        name text,
        book_title text,
        book_return_at date)''')
