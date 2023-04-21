import psycopg2

# conectando ao banco de dados DoeVida
conn = psycopg2.connect(
    host="127.0.0.1",
    database="doevida",
    user="postgres",
    password="doevida"
)

# criando um cursor
cur = conn.cursor()

# mudando de volta para autocommit false
conn.autocommit = False

# criando a tabela
cur.execute("CREATE TABLE IF NOT EXISTS usuariosdoevida (cpf VARCHAR(14) PRIMARY KEY, nome VARCHAR(100), idade INTEGER)")
conn.commit()

# Verificar se a tabela foi criada
if cur.rowcount > 0:
    print("Tabela criada com sucesso.")
else:
    print("A tabela já existe.")

cur.close()
conn.close()