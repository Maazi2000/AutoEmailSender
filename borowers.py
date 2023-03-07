from collections import namedtuple
from database import Database

# Tuple that will hold the database result row
Entity = namedtuple('Entity', 'name email book_title book_return_at')

def get_borowers_by_date(connection, book_return_at):
    '''Retrieve a list of borrowers whose book return date is before the specified date'''
    # List that holds tuples
    entities = []
    # Connect to the database and execute the query
    with Database(connection) as database:
        database.cursor.execute('''SELECT
            name,
            email, 
            book_title, 
            book_return_at 
        FROM borows 
        WHERE book_return_at < ?''', (book_return_at,))

        # Iterate through the database result and add them to the list as namedtuples
        for name, email, book_title, book_return_at in database.cursor.fetchall():
            entities.append(Entity(name, email, book_title, book_return_at))

    return entities
