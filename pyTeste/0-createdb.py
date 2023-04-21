import psycopg2

# Conectando ao banco de dados padrão
conn = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="doevida"
)

# Criando um cursor
cur = conn.cursor()

# Mudando para autocommit
conn.autocommit = True

# Executando a consulta SQL para listar os databases existentes
cur.execute("SELECT datname FROM pg_database")

# Obtendo os resultados da consulta
rows = cur.fetchall()

# Verificando se o database doevida já existe
db_exists = False
for row in rows:
    if row[0] == 'doevida':
        db_exists = True
        break

# Caso o database doevida não exista, criar o mesmo
if not db_exists:
    cur.execute("CREATE DATABASE doevida")
    print("O database doevida foi criado com sucesso.")
else:
    print("O database doevida já existe.")

# Fechando o cursor e a conexão
cur.close()
conn.close()
