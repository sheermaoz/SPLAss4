import inspect
from dto import *
       

class Vaccines:
    def __init__(self, conn):
        self._conn = conn
        self._table_name = 'vaccines'
 
    def insert(self, vaccine):
        ins_dict = vars(vaccine)
        ins_dict.pop('id')
        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))
 
        stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table_name, column_names, qmarks)
        self._conn.execute(stmt, list(params))
 
    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {}'.format(self._table_name))
        return [Vaccine(*row) for row in c.fetchall()]
    
    def find_all_by_date(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {} ORDER BY date DESC'.format(self._table_name))
        return [Vaccine(*row) for row in c.fetchall()]
 
    def find(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'SELECT * FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, list(params))
        return [Vaccine(*row) for row in c.fetchall()]
    
    def delete(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'DELETE FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, list(params))

    def update(self, set_values, cond):
        set_column_names = set_values.keys()
        set_params = set_values.values()
 
        cond_column_names = cond.keys()
        cond_params = cond.values()
 
        params = list(set_params) + list(cond_params)
 
        stmt = 'UPDATE {} SET {} WHERE {}'.format(self._table_name,
                                                      ', '.join([set + '=?' for set in set_column_names]),
                                                      ' AND '.join([cond + '=?' for cond in cond_column_names]))
 
        self._conn.execute(stmt, list(params))
    
class Clinics:
    def __init__(self, conn):
        self._conn = conn
        self._table_name = 'clinics'
 
    def insert(self, vaccine):
        ins_dict = vars(vaccine)
 
        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))
 
        stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table_name, column_names, qmarks)
        self._conn.execute(stmt, list(params))
 
    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {}'.format(self._table_name))
        return [Clinic(*row) for row in c.fetchall()]
    
 
    def find(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'SELECT * FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
        c = self._conn.cursor()
        c.execute(stmt, list(params))
        return [Clinic(*row) for row in c.fetchall()]
    
    def delete(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'DELETE FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, params)

    def update(self, set_values, cond):
        set_column_names = set_values.keys()
        set_params = set_values.values()
 
        cond_column_names = cond.keys()
        cond_params = cond.values()
 
        params = list(set_params) + list(cond_params)
 
        stmt = 'UPDATE {} SET {} WHERE {}'.format(self._table_name,
                                                      ', '.join([set + '=?' for set in set_column_names]),
                                                      ' AND '.join([cond + '=?' for cond in cond_column_names]))
        self._conn.execute(stmt, params)
    
class Logistics:
    def __init__(self, conn):
        self._conn = conn
        self._table_name = 'logistics'
 
    def insert(self, vaccine):
        ins_dict = vars(vaccine)
 
        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))
 
        stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table_name, column_names, qmarks)
        self._conn.execute(stmt, list(params))
 
    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {}'.format(self._table_name))
        return [Logistic(*row) for row in c.fetchall()]
    
 
    def find(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'SELECT * FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, list(params))
        return [Logistic(*row) for row in c.fetchall()]
    
    def delete(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'DELETE FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, params)

    def update(self, set_values, cond):
        set_column_names = set_values.keys()
        set_params = set_values.values()
 
        cond_column_names = cond.keys()
        cond_params = cond.values()
 
        params = list(set_params) + list(cond_params)
 
        stmt = 'UPDATE {} SET {} WHERE {}'.format(self._table_name,
                                                      ', '.join([set + '=?' for set in set_column_names]),
                                                      ' AND '.join([cond + '=?' for cond in cond_column_names]))
 
        self._conn.execute(stmt, list(params))
    
class Suppliers:
    def __init__(self, conn):
        self._conn = conn
        self._table_name = 'suppliers'
 
    def insert(self, vaccine):
        ins_dict = vars(vaccine)
 
        column_names = ','.join(ins_dict.keys())
        params = ins_dict.values()
        qmarks = ','.join(['?'] * len(ins_dict))
 
        stmt = 'INSERT INTO {} ({}) VALUES ({})'.format(self._table_name, column_names, qmarks)
        self._conn.execute(stmt, list(params))
 
    def find_all(self):
        c = self._conn.cursor()
        c.execute('SELECT * FROM {}'.format(self._table_name))
        return [Supplier(*row) for row in c.fetchall()]
 
    def find(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'SELECT * FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, list(params))
        return [Supplier(*row) for row in c.fetchall()]
    
    def delete(self, **keyvals):
        column_names = keyvals.keys()
        params = keyvals.values()
 
        stmt = 'DELETE FROM {} WHERE {}'.format(self._table_name, ' AND '.join([col + '=?' for col in column_names]))
 
        c = self._conn.cursor()
        c.execute(stmt, params)

    def update(self, set_values, cond):
        set_column_names = set_values.keys()
        set_params = set_values.values()
 
        cond_column_names = cond.keys()
        cond_params = cond.values()
 
        params = list(set_params) + list(cond_params)
 
        stmt = 'UPDATE {} SET {} WHERE {}'.format(self._table_name,
                                                      ', '.join([set + '=?' for set in set_column_names]),
                                                      ' AND '.join([cond + '=?' for cond in cond_column_names]))
 
        self._conn.execute(stmt, list(params))
    