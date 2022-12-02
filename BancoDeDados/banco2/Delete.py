import sqlite3
banco = sqlite3.connect('banco2.db')
cursor = banco.cursor()
cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")

banco.commit()

cursor.execute("SELECT * FROM fornecedor")

for linha in cursor.fetchall():

    print(linha)

cursor.close()

banco.close()