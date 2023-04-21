import psycopg2

# Conectando ao banco de dados
conn = psycopg2.connect(
    host="127.0.0.1",
    database="doevida",
    user="postgres",
    password="doevida"
)

# Criando um cursor
cur = conn.cursor()

# Executando a consulta SQL
cpf = "55560677788"

# Executando a consulta SQL para verificar se o CPF existe
cur.execute("SELECT * FROM usuariosdoevida WHERE cpf = %s", (cpf,))
row = cur.fetchone()

# Verificando se o CPF existe
if row is None:
    print("CPF não encontrado na tabela.")
else:
    print("CPF encontrado na tabela.")
    print(row)

# Fechando o cursor e a conexão
cur.close()
conn.close()