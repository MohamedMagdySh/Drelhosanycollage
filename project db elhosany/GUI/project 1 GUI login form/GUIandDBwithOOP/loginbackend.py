from database import Connect
import sys

def login(id):
    conn=None
    sql="""SELECT * FROM clients WHERE username=%s AND password=%s"""
    values=(id.getUsername(), id.getPassword())
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del values, sql, conn
        return result
