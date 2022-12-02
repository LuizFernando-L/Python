import sqlite3
banco = sqlite3.connect('banco2.db')
cursor = banco.cursor()

cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
banco.commit()
cursor.execute("SELECT * FROM fornecedor")
for linha in cursor.fetchall():
    print(linha)
cursor.close()
banco.close()
