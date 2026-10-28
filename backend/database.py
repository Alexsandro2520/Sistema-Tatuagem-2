import mysql.connector        #Biblioteca para conectar ao MySQL
from dotenv import load_dotenv  #Lê o arquivo .env
import os                      #Acessa as variáveis de ambiente

load_dotenv()                  #Carrega as variáveis do .env


def conectar():
    #Cria e retorna uma conexão com o banco de dados
    return mysql.connector.connect(
        host = os.getenv("DB_HOST"),          # endereço do servidor (localhost)
        user = os.getenv("DB_USER"),          # usuário do banco
        password = os.getenv("DB_PASSWORD"),  # senha do banco
        database = os.getenv("DB_NAME")       # nome do banco
)