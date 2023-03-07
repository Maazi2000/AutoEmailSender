import sqlite3
import pytest
from borowers import get_borowers_by_date

@pytest.fixture
def create_connection():
    """This fixture creates an in-memory SQLite database."""
    connection =sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE borows(
        id INTEGER primary key autoincrement,
        email TEXT,
        name TEXT,
        book_title text,
        book_return_at DATE)''')

    # List of tuples which contain data test
    sample_data = [
        (1, 'test_name1', 'test_mail1', 'test_book1', '13.04.2019'),
        (2, 'test_name2', 'test_mail2', 'test_book2', '13.04.2022'),
        (3, 'test_name3', 'test_mail3', 'test_book3', '13.04.2024')]

    cursor.executemany('INSERT INTO borows VALUES (? ,? , ?, ?, ?)',sample_data)

    return connection

def test_borowers(create_connection):
    """This function checks if the 'get_borowers_by_date()' function returns
        the correct results for a given date string."""
    borowers = get_borowers_by_date(create_connection, '13.04.2024')
    assert len(borowers) == 2
    assert borowers[0].name =='test_mail1'
