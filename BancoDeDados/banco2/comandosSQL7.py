import sqlite3

conn = sqlite3.connect('banco2.db')

cursor = conn.cursor()

# Lista as tabelas do banco de dados

cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name""")

print('Tabelas:')

for tabela in cursor.fetchall():

    print(tabela)
#Captura a ddl usada para criar a tabela

tabela = 'fornecedor'

cursor.execute(f""" SELECT sql FROM sqlite_master WHERE type = 'table' AND name='{tabela}'""")
print(f'\n DDL da tabela {tabela}: ')
for schema in cursor.fetchall():

    print("%s" % (schema))

    cursor.close()
conn.close()

tabela: ('fornecedor', 'sqlite_sequence')
DDL: ("CREATE TABLE fornecedor id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT",

    "nome_fornecedor TEXT NOT NULL",

    "cnpj VARCHAR(18) NOT NULL",

    "cidade TEXT",

    "estado VARCHAR(2) NOT NULL",

    "cep VARCHAR(9) NOT NULL",
    "data_cadastro DATE NOT NULL")
