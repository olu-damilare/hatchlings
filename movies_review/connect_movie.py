import mysql.connector
from mysql.connector import Error


def connect_insert():
    conn = None

    try: 
        conn = mysql.connector.connect(host = 'localhost', database = 'movie_review', user = input('Enter your username: '), password = input('Enter your password: '))

        if conn.is_connected:
            print('Connected to the database server')
            
            list_vals = []
            cursor = conn.cursor(dictionary = True)
            user_selection = int(input("Press 1 to insert into movie table \nPress 2 to update movie table \nPress 3 to delete row from movie table\n"))

            if user_selection == 1:
                row_num = int(input('How many rows do you want to insert? '))           
                sql_query = "Insert into movies(title, release_year, genre, collection_in_mil) Values (%s, %s, %s, %s);"  
                for i in range(row_num):
                    print('\nRow', i+1)
                    title = input("Enter the title of the movie: ")
                    release_year = input("Enter the year which the movie was released: ")
                    genre = input("Enter the genre of the movie: ")
                    collection_in_mil = input("Enter the sales value of the movie in million: ")
                    
                    val = (title, release_year, genre, collection_in_mil)
                    list_vals.append(val)
                    print()

                cursor.executemany(sql_query, list_vals)
                conn.commit()
                print(cursor.rowcount, ' row was inserted')
                
            elif user_selection == 2:
                number_of_columns = int(input("How many fields do you want to update? "))
                list = []
                for i in range(number_of_columns):
                    column_name = input("Enter column name: ")
                    new_value = input("Enter the new value: ")
                    sql_query = "Update movies set " + column_name + " = " + "\'" + new_value + "\' where id = " + str(id)
                    cursor.execute(sql_query)
                    conn.commit() 
                print(cursor.rowcount, "fields successfully updated in movies table")  

            if user_selection == 3:
                number_of_rows = int(input("How many rows do you want to delete? "))
                list = []
                for i in range(number_of_rows):
                    value = input("Enter the key value of the row(s) to be deleted: ")
                    column_name = input("Enter column name where the column exists: ")
                    sql_query = "delete from movies where " + column_name + " = " + "\'" + value + "\'"
                    cursor.execute(sql_query)
                    conn.commit()      
                print(cursor.rowcount, "row successfully deleted from movies table")    

            cursor.close()    
            
    except Error as e:
        print("Failed to connect due to ", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')
   

connect_insert()
