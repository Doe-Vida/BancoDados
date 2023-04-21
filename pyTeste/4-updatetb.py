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

# Executando o comando UPDATE
cpf = "55566677788"
novo_nome = "Bob"
nova_idade = 23
cur.execute("UPDATE usuariosdoevida SET nome = %s, idade = %s WHERE cpf = %s", (novo_nome, nova_idade, cpf))

# Confirmando a operação
conn.commit()

# Fechando o cursor e a conexão
cur.close()
conn.close()
