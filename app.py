from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository
from lib.item import Item

connection = DatabaseConnection()

connection.connect()

order_repo = OrderRepository(connection)


order_repo.add_order("Tom", 1,'1000', "20-02-1997")
order_repo.add_order("Boris", 5,'200', "22042")
orders = order_repo.all()
for order in orders:
    print(order)