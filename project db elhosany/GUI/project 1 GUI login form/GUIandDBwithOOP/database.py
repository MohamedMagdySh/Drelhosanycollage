import mysql.connector
import sys

def Connect():
    conn=None
    try:
        conn=mysql.connector.Connect(
            host='localhost',
            username='root',
            password='01023904417',
            database='logintest'
        )


    except:
        print('Error', sys.exc_info())

    finally:
        return conn