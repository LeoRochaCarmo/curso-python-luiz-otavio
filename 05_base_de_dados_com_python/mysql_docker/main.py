# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import os
from dotenv import load_dotenv

TABLE_NAME = 'customers'

load_dotenv()

con = pymysql.connect(
    host=os.environ['MYSQL_HOST'],    
    user=os.environ['MYSQL_USER'],    
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with con:
    with con.cursor() as cursor:
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ( '
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    con.commit()

    # Placeholder para evitar SQL Injection
    with con.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%s, %s) ' # Placeholder 
        )

        data = ('Leonardo', 31)
        result = cursor.execute(sql, data)
        # print(sql)
        # print(result) # Mostra quantas linhas foram adicionadas
    con.commit()

    # Inserindo valores usando dicionários
    with con.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%(name)s, %(age)s) ' # Placeholder para evitar SQL Injection
        )

        data2 = {
            'name': 'Samuel',
            'age': 27
        }
        # print(sql)
        # print(data2)
        result = cursor.execute(sql, data2)
    con.commit()

    # Inserindo vários valores usando um iterável
    with con.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%(name)s, %(age)s) '
        )

        data3 = (
            {'name': 'Bran', 'age': 14},
            {'name': 'Colin', 'age': 19},
            {'name': 'Gregory', 'age': 24},
        )
        cursor.executemany(sql, data3)
    con.commit()
