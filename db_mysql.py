import mysql.connector
from mysql import connector
from mysql.connector import MySQLConnection, CMySQLConnection, errorcode

# db = 'mysqlsampledatabase.sql'

try:
    config = {
        'user': 'root', 'password': 'rootroot',
        'host': '127.0.0.1',
        'port': '3306',
        'database': 'mysql',
        # 'socket': '/tmp/mysql.sock'
    }
    cnx = mysql.connector.connect(**config)
except connector.Error as err:
    if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DV_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = cnx.cursor()
    query = {"SHOW COLUMNS from user"}
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    cnx.close()
