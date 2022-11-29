import sqlite3
banco = sqlite3.connect('banco2.db')

#CRIANDO TABELA COM AS VARIAVEIS DO BANCO

tabela1 = """CREATE TABLE fornecedor (id_fornecedor INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome_fornecedor TEXT NOT NULL,
cnpj VARCHAR(18) NOT NULL, 
cidade TEXT,
estado VARCHAR(2) NOT NULL,
cep VARCHAR(9) NOT NULL,
data_cadastro DATE NOT NULL);
"""

#criando objeto para fazer os comandos crud no banco

cursor = banco.cursor()
cursor.execute(tabela1)

#Inserindo elemento na tabela

dados = [('Empresa A', '44.444.444/4444-44', 'São Paulo', 'SP','44444-444', '2020-01-01' ),
         ('Empresa B', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2020-01-01'),
         ('Empresa C', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2020-01-01')]
cursor.executemany("""INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro) 
VALUES(?, ?, ?, ?, ?, ?)""", dados)
banco.commit()
print("Dados inseridos!")

print("Descrição do cursor: ", cursor.description)

print("Linhas afetadas: ", cursor.rowcount)

cursor.close()

banco.close()
