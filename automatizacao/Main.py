from Conexao import connection
from Ultimo_valor_planilha import Ultima_linha
import pymysql.cursors
import pymysql
from openpyxl import load_workbook
import openpyxl 


with connection.cursor() as c:
        c.execute(f"SELECT * FROM ordem_serviço where id >{Ultima_linha}")
        res= c.fetchall()   
        print(res)   
connection.close()

