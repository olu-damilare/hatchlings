import mysql.connector
from mysql.connector import Error


def connect_insert():
    conn = None

    try: 
        conn = mysql.connector.connect(host = 'localhost', database = 'demo', user = input('Enter your username: '), password = input('Enter your password: '))

        if conn.is_connected:
            print('Connected to the datatbase server')

            cursor = conn.cursor(dictionary = True)
            sql_query = "Insert into Human (humanID, name, color, Gender, bloodgroup) Values (%s, %s, %s, %s, %s)"

            row_num = int(input('How many rows do you want to insert? '))
            list_vals = []

            for i in range(row_num):
               print('Row', i+1)
               humanID = input("Enter the Human ID: ")
               name = input("Enter the name: ")
               color = input("Enter the color: ")
               gender = input("Enter the gender: ")
               blood_group = input("Enter the blood group: ")
               
               val = (humanID, name, color, gender, blood_group)
               list_vals.append(val)
               print()

            cursor.executemany(sql_query, list_vals)

            conn.commit()

            print(cursor.rowcount, ' row was inserted')

            cursor.close()

            
    except Error as e:
        print("Failed to connect due to ", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')


connect_insert()
