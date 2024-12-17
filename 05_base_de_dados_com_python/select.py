import sqlite3
from main import BD_FILE, TABLE_NAME

# Conectar a base de dados
con = sqlite3.connect(BD_FILE)
cursor = con.cursor()

# Imprimir valores da tabela
cursor.execute(f'SELECT * FROM {TABLE_NAME} ORDER BY id')
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

# Fechar a conexão
cursor.close()
con.close()