from os import getenv
from dotenv import load_dotenv
import sqlite3

# load environment variables from .env file
load_dotenv()

# establish connection
conn =sqlite3.connect("Database.db")

# create cursor
cursor = conn.cursor()

# excecute SQL query
""" cursor.execute('''CREATE TABLE borrowers(
    id integer primary key autoincrement,
    name text,
    book_title text,
    book_return_at date)''') """

cursor.execute('''SELECT * from borrowers''')

# commit transaction
conn.commit()

# close cursor and connection 
cursor.close()
conn.close()
print(getenv("FIRST_NAME"))