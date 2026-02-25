from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.item import Item

connection = DatabaseConnection()

connection.connect()

item_repo = ItemRepository(connection)


item_repo.add_item('Bananas', 200)
item_repo.add_item('Bananas', 20)

items = item_repo.all()
for item in items:
    print(item)

item_repo.delete_item('Bananas')
item_repo.delete_item('Pears')

items = item_repo.all()
for item in items:
    print(item)