import pyodbc

dados_conexao = (
    "Driver ={MYSQL Server};"
    "Server =WNB033880CPS;"
    "Database =pysql;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem sucedida')
