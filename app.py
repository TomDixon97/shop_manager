from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository
from lib.item import Item



class Application:

    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()

    

    def run(self):
        item_repo = ItemRepository(self._connection)
        order_repo = OrderRepository(self._connection)

        choice = None

        while choice != "5":
            print("\nWhat would you like to do?")
            print("1. List all shop items ")
            print("2. Create a new item")
            print("3. List all orders")
            print("4. Create a new order")
            print("5. Quit")
            choice = input("Choice: ")

            if choice == "1":
                items = item_repo.all()
                for item in items:
                    print(item)

            elif choice == "2":
                name = input("Item name:")
                quantity = input("Amount: ")
                item_repo.add_item(name, quantity)
                print("Item added")

            elif choice == "3":
                orders = order_repo.all()
                for order in orders:
                    print(order)

            elif choice == "4":
                name = input("Customer's name: ")
                item = input("Item ordered: ")
                amount = input("Amount ordered: ")
                date = input("date order placed (DD-MM-YYYY): ")
                order_repo.add_order(name, item, amount, date)
                
            elif choice == "5":
                break

            else:
                print("Invalid Choice\n")

if __name__ == '__main__':
    app = Application()
    app.run()