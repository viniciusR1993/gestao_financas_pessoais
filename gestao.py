import pyodbc
from decimal import *

class ConectarAccess:
    def __init__(self, schema):
        self.schema = schema
        # Criando conexão.
        self.con = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                  r'DBQ=C:\Users\vinir\OneDrive\Documentos\BD\/' + schema + '.accdb;')
        # Criando cursor.
        self.cur = self.con.cursor()

    def exibir_tabelas(self):
        for tabela in self.cur.tables(tableType='TABLE'):
            print(tabela.table_name)

    def select(self, query):
        return self.cur.execute(query).fetchall()
    
    def insert(self, query):
        count = self.cur.execute(query).rowcount
        self.con.commit()

    def delete(self, query):
        count = self.cur.execute(query).rowcount
        self.con.commit()

    def close(self):
        self.con.close()

    def insertAcc(self, df, table):
        for i, row in df.iterrows():
            query = f"""
                    INSERT INTO
                    {table} ({','.join(df.columns.to_list())})
                    VALUES (
                """
            for r in row:
                if type(r) in (bool, float, int, Decimal):
                    query = f"{query}{str(r)},"
                else:
                    query = f"{query}'{str(r)}',"

            query = f"{query[:-1]})"
            #print(query)
            self.insert(query)
        

