#Can run this to make a new database, only for testing
from database_connection import DatabaseConnection

class Seed:

    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/shop_manager.sql')



if __name__ == '__main__':
    seed = Seed()