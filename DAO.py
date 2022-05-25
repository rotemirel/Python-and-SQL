import DTO


class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
        INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)""",
                           [hat.id, hat.topping, hat.supplier, hat.quantity])

    def find_by_id(self, hat_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id, topping, supplier, quantity FROM hats WHERE id = ? """, [hat_id])
        return DTO.Hat(*c.fetchone())

    def update_quantity(self, hat_id):
        curr_quantity = self.find_by_id(hat_id).quantity - 1
        c = self._conn.cursor()
        if curr_quantity > 0:
            c.execute("""
            UPDATE hats SET quantity = quantity-1 WHERE id = ? """, [hat_id])
            # change quantity-1
        else:
            c.execute(""" DELETE From hats WHERE id = ?""", [hat_id])

    def find_by_topping(self, curr_topping):
        c = self._conn.cursor()
        options = c.execute(""" SELECT id, topping, supplier, quantity FROM hats Where topping = ?""",
                            [curr_topping]).fetchall()

        options.sort(key=lambda x: x[2])
        return DTO.Hat(*options[0])


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
        INSERT INTO suppliers (id, name) VALUES (?, ? )""",
                           [supplier.id, supplier.name])

    def find(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id, name FROM suppliers WHERE id = ? """, [supplier_id])
        return DTO.Supplier(*c.fetchone())


class Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
        INSERT INTO orders (id, location, hat) VALUES (?, ?, ?)""", [int(order.id), str(order.location), order.hat])

    def find(self, order_id):
        c = self._conn.cursor()
        c.execute("""
        SELECT id, location, hat FROM suppliers WHERE id = ? """, [order_id])
        return DTO.Order(*c.fetchone())

