import sqlite3
from pathlib import Path

# Criar arquivo da base de dados
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
BD_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

# Conectar a base de dados
con = sqlite3.connect(BD_FILE)
cursor = con.cursor()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
con.commit()

# Inserir valores na tabela
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "Leonardo Rocha", 80.5)'
)
con.commit()

# Deletar valores
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
con.commit()

# Deletar a sequência dos ids
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name ="{TABLE_NAME}"'
)

# Inserir novamente alguns valores
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES '
    '(NULL, "Leonardo", 80.5), '
    '(NULL, "Luana", 60.5)'
)
con.commit()

# Forma de evitar 'sql injection'
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES '
    '(?, ?)' # ? -> placeholders, parâmetros, bindings
)
cursor.execute(sql,['Carlos', 90])
# Inserir vários valores
cursor.executemany(sql, (('Chicão', 78.4), ('Danilo', 30.5)))
con.commit()

if __name__ == '__main__':
    print(sql)

    # Deletar os valores do id = 3
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = "3"')
    # Atualizar o peso do id = 4
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET weight = 200.50 '
        'WHERE id = 4'
    )
    con.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    # Fechar a conexão
    cursor.close()
    con.close()