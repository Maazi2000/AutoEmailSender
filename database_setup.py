"""Class which create table"""
from database import Database

def setup(connection):
    """creating database and table items"""
    with Database(connection) as database:
        database.cursor.execute('''CREATE TABLE borows(
        id INTEGER primary key autoincrement,
        email TEXT,
        name TEXT,
        book_title text,
        book_return_at DATE)''')
