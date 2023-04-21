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

# verificando se a tabela já existe
cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name='usuariosdoevida')")
exists = cur.fetchone()[0]

# se a tabela já existe, apenas insere os dados
if exists:
    cur.execute("INSERT INTO usuariosdoevida (cpf, nome, idade) VALUES ('11122233344', 'Alice', 25)")
    cur.execute("INSERT INTO usuariosdoevida (cpf, nome, idade) VALUES ('55566677788', 'Bob', 30)")
    cur.execute("INSERT INTO usuariosdoevida (cpf, nome, idade) VALUES ('55566607788', 'Bob', 39)")
else:
    # se a tabela não existe, cria e insere os dados
    cur.execute("CREATE TABLE usuariosdoevida (cpf VARCHAR(14) PRIMARY KEY, nome VARCHAR(100), idade INTEGER)")
    cur.execute("INSERT INTO usuariosdoevida (cpf, nome, idade) VALUES ('11122233344', 'Alice', 25)")
    cur.execute("INSERT INTO usuariosdoevida (cpf, nome, idade) VALUES ('55566677788', 'Bob', 30)")
    cur.execute("INSERT INTO usuariosdoevida (cpf, nome, idade) VALUES ('55566607788', 'Bob', 39)")

# lendo os dados da tabela
cur.execute("SELECT cpf, nome, idade FROM usuariosdoevida")
rows = cur.fetchall()
for row in rows:
    print(row)

# commitando a transação
conn.commit()

# fechando o cursor e a conexão
cur.close()
conn.close()
