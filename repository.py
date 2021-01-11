from dao import *
import sqlite3
import atexit

class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('vaccines.db')
        self.vaccines = Dao(Vaccine, self._conn)
        self.logistics = Dao(Logistic, self._conn)
        self.clinics = Dao(Clinic, self._conn)
        self.suppliers = Dao(Supplier, self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()
    
   
    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE IF NOT EXISTS logistics (
            id      INTEGER         PRIMARY KEY,
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
            id INT PRIMARY KEY,
            date DATE NOT NULL,
            supplier INT REFERENCES suppliers(id),
            quantity INT NOT NULL
        );
    """)

repo = _Repository()
atexit.register(repo._close)