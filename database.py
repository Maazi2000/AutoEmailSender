'''Class that will be used to connect to the database'''

class Database:
    # Initializing the class with a connection object
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        # Method that will handle the closing and committing/rolling back the transactions
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()
