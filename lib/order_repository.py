from lib.order import Order
from datetime import datetime
from lib.item import Item

class OrderRepository:

    def __init__(self, connection):
        self._connection = connection


    def all(self):
        rows = self._connection.execute('SELECT * FROM orders')
        orders = []

        for row in rows:
            order = Order(row['id'], row['name'], row['item_name'], row['item_id'], row['amount'], row['date_placed'] )
            orders.append(order)

        return orders
    
    def add_order(self, name, item, amount, date):

        if not self._check_item_in_database(item):
            print('Item is not in stock')
            return None


        item_id = self._get_item_id(item)

        try:
            datetime.strptime(date, "%d-%m-%Y")


        #Use today's date if invalid format 
        except ValueError as e:
            print("Date not in valid format. Using today's date")
            date = datetime.today()
            date = date.strftime("%d-%m-%Y")

        order = Order(None, name, item, item_id, amount, date)
        self._connection.execute('INSERT INTO orders (name, item_name, item_id, amount, date_placed) VALUES (%s, %s, %s, %s, %s)',
                                 [order.name, order.item_name, order.item_id, order.amount, order.date_placed])
        self._remove_item_amount(item, amount)
        return None
        
    
    
    
    
    
    def _get_item_name(self, item_id:int):

        try:
            rows = self._connection.execute('SELECT name from items WHERE id = %s', [item_id])
            row = rows[0]
            
        except IndexError as e:
            return 'No item found with this id'
        return row['name']
    

    def _get_item_id(self, item_name:str):
        try:
            rows = self._connection.execute('SELECT id from items WHERE name = %s', [item_name])
            row = rows[0]
            
        except IndexError as e:
            return 'No item found with this name'
        return row['id'] 


    def _check_item_in_database(self, item_name):
        
        try:
            rows = self._connection.execute('SELECT id from items where name = %s', [item_name])
            row = rows[0]
            return True
        except IndexError as e:
            return False
            
    def _remove_item_amount(self, item, amount):
        self._connection.execute('UPDATE items SET quantity = quantity - %s WHERE name = %s', [amount, item])
        return None
        