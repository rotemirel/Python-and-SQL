import sqlite3
import DAO
import atexit


from DTO import Hat, Supplier


class _Repository:
    def __init__(self):
        # change name
        self.conn = None
        self.hats = None
        self.suppliers = None
        self.orders = None

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.conn.executescript(""" 
        CREATE TABLE IF NOT EXISTS hats (id INT PRIMARY KEY, topping TEXT NOT NULL, supplier INT REFERENCES 
        suppliers(id), quantity INT NOT NULL) ;
        CREATE TABLE IF NOT EXISTS suppliers (id INT PRIMARY KEY, name TEXT NOT NULL) ;
        CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY, location TEXT NOT NULL, hat INT REFERENCES hats(id)) 
        ;""")

    def set_fields(self, database):
        self.conn = sqlite3.connect(database)
        self.hats = DAO.Hats(self.conn)
        self.suppliers = DAO.Suppliers(self.conn)
        self.orders = DAO.Orders(self.conn)


repo = _Repository()
atexit.register(repo.close)



