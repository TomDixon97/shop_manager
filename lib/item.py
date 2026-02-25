class Item:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.id}  - {self.name} - {self.quantity}"
