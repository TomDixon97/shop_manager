from lib.order import Order
from datetime import datetime

class OrderRepository:

    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT * FROM orders')
        orders = []

        for row in rows:
            order = Order(row['id'], row['name'], row['item_id'], row['amount'], row['date_placed'] )
            orders.append(order)

        return orders
    
    def _get_item_id(self, item_name):
        pass

    
    def add_order(self, name, item, amount, date):

        try:
            datetime.strptime(date, "%d-%m-%Y")

        except ValueError as e:
            print(e)
            date = datetime.today()
            date = date.strftime("%d-%m-%Y")

        order = Order(None, name, item, amount, date)
        self._connection.execute('INSERT INTO orders (name, item_id, amount, date_placed) VALUES (%s, %s, %s, %s)',
                                 [order.name, order.item_id, order.amount, order.date_placed])

        

