import mysql.connector
from mysql.connector import Error


def connect_fetch():
    pass
    conn = None

    try:
        conn = mysql.connector.connect(host='localhost', database='cape_codd',
                                       user='olu', password='root')
        print('Connecting to the database server')
        if conn.is_connected:
            print('Connected to the datatbase server')

            cursor = conn.cursor(dictionary=True)
            cursor.execute("select * from buyer")
            records = cursor.fetchall()
            print("Total number of rows in buyer is ", cursor.rowcount)
            # print('Total number of columns is ', cursor.columncount)
            print('Printing each buyer record')

            for row in records:
                for i in row:
                    print(i, "-", row[i])
                print()

    except Error as e:
        print('Failed to connect to database server due to ', e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database shutdown')


connect_fetch()
