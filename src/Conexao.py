import pymysql.cursors 
import os
def conectar_erp():
    connection = pymysql.connect(host = os.getenv("DB_HOST"),user = os.getenv("DB_USER"),database = os.getenv("DB_NAME"),
                         password = os.getenv("DB_PASS"),charset='utf8mb4',cursorclass = pymysql.cursors.DictCursor)
    return connection









    
