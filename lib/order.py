from datetime import datetime

class Order:

    def __init__(self, id, name, item_name, item_id, amount, date_placed):
        self.id = id
        self.name = name
        self.item_name = item_name
        self.item_id = item_id
        self.amount = amount
        self.date_placed = date_placed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Customer {self.name} - ordered {self.amount} of {self.item_name} (id: {self.item_id}) on {self.date_placed}"
    

