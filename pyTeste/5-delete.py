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

# Definindo o CPF que você deseja excluir
cpf = "55566677788"

# Executando a instrução SQL de exclusão
cur.execute("DELETE FROM usuariosdoevida WHERE cpf = %s", (cpf,))

# Salvando as alterações no banco de dados
conn.commit()

# Fechando o cursor e a conexão
cur.close()
conn.close()
