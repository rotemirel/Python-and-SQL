

class Hat:
    def __init__(self, _id, topping, supplier, quantity):
        self.id = _id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity


class Supplier:
    def __init__(self, _id, name):
        self.id = _id
        self.name = name


class Order:
    def __init__(self, _id, location, hat):
        self.id = _id
        self.location = location
        self.hat = hat
