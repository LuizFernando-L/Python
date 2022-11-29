import sqlite3
banco = sqlite3.connect('BancoDeDados.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE fornecedor(id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
               " nome_fornecedor TEXT NOT NULL,"
               " cnpj VARCHAR(18) NOT NULL,"
               " cidade TEXT, "
               "estado VARCHAR(2) NOT NULL"
               ", cep VARCHAR(9) NOT NULL, "
               "data_cadastro DATE NOT NULL);")
