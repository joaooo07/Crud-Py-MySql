#Primeiro Passo é Importar o MYSQL
import mysql.connector
#Precisamos ter uma tabela criada. 
#Agora podemos criar uma conexão com 4 valores obrigatorios: 
# Host | user | password | database (tabela que você está mexendo )
#Host - Caso esteja usando um banco de dados local, usamos localhost
#Caso seja um link, colocamos o link 
#user - Usuário do banco de dados
#password - Senha do banco de dados
#database - Nome da tabela que você está mexendo
#Isso é apenas Um exemplo de formatação. O codigo não esta funcionando!
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456',
    database = 'bdyoutube'
)
#Apos isso devemos criar um Cursor. 
#O cursor é usado para executar os comandos sql 
cursor = conexao.cursor()

#CRUD 
#C - Criar | R - Ler  |U - Atualizar | D - Deletar
#Comandos em Aspas '' | necessidades dentro do comando em aspas duplas. como um texto.
#cursor execute(comando)
#conexao.commit() - edita o banco de dados. 
#resultado = cursor.fetchall() ler banco de dados 
#ETAPAS 1 - CRIAR O COMANDO | 2 EXECUTAR O COMANDO |
#  3 - SE O COMANDO EXECUTADO EDITA ALGO - COMMIT | ELSE -FETCHALL


#Create 
nome_produto = "Toddynho"
valor = 3
#comando = f'INSERT  INTO TABELA QUE VOCÊ QUER INSERIR (COMPONENTES DA TABELA) VALUES (OQ VOCÊ QUER INSERIR )'
#PRECISAMOS CRIAR UMA VARIAVEL COM OS NOMES DO PRODUTO QUE DESEJA INSERIR. COMO MOSTRADO NA LINHA 33 | 34
comando = f'INSERT INTO vendas (nome_produto,valor) VALUES ("{nome_produto}", {valor})'
#COLOCAMOS ASPAS DUPLAS NO NOME_PRODUTO POIS É UM TEXTO
cursor.execute(comando)
conexao.commit()


#READ 
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
nome_produto = "toddynho"
valor = 6
#   ATUALIZAR A TABELA VENDAS , SETANDO UM NOVO VALOR PARA 6 ONDE NOME DO PRODUTO FOR TODDYNHO
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#DELETE 
nome_produto = "toddynho"
#DELETAR A MINHA TODAS AS LINHAS DA MINHA TABELA ONDE O NOME DO PRODUTO FOR TODDYNHO
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()


#Para encerrar a Conexão 
cursor.close()
conexao.close()