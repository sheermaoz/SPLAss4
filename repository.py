from dao import *
import sqlite3
import atexit
from dto import *

class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.vaccines = Vaccines(self._conn)
        self.logistics = Logistics(self._conn)
        self.clinics = Clinics(self._conn)
        self.suppliers = Suppliers(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()
    
   
    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE IF NOT EXISTS logistics (
            id      INTEGER  PRIMARY KEY,
            name    TEXT        NOT NULL,
            count_sent INTEGER NOT NULL,
            count_received INTEGER NOT NULL
        );
 
        CREATE TABLE IF NOT EXISTS suppliers (
            id                 INT     PRIMARY KEY,
            name     TEXT    NOT NULL,
            logistic INT REFERENCES logistics(id)
        );
 
        CREATE TABLE IF NOT EXISTS clinics (
            id INT PRIMARY KEY,
            location STRING NOT NULL,
            demand INT NOT NULL,
            logistic INT REFERENCES logistic(id)
        );

        CREATE TABLE IF NOT EXISTS vaccines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            supplier INT REFERENCES suppliers(id),
            quantity INT NOT NULL
        );
    """)

repo = _Repository()
atexit.register(repo._close)