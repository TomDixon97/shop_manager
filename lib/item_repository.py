from lib.item import Item

class ItemRepository:

    #Initialise class with db connection
    def __init__(self, connection):
        self._connection = connection


    #Return all items in the inventory

    def all(self):
        rows = self._connection.execute('SELECT * FROM items')
        items = []

        for row in rows:
            item = Item(row['id'], row['name'], row['quantity'])
            items.append(item)

        return items


    def add_item(self, name, quantity):
        item = Item(None, name, quantity)
        self._connection.execute('INSERT INTO items (name, quantity) VALUES (%s, %s)',
                                 [item.name, item.quantity])
        return None


    def delete_item(self, name):
        self._connection.execute('DELETE FROM items WHERE name = %s', [name])
        return None