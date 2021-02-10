import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='s217.goserver.host',
                                       database='web357_db35',
                                       user='web357_35',
                                       password='XfJbuWNoVCpdnx5l')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()



connect()