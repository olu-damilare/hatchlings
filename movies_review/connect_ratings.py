import mysql.connector
from mysql.connector import Error


def connect_run():
    conn = None

    try: 
        conn = mysql.connector.connect(host = 'localhost', database = 'movie_review', user = input('Enter your username: '), password = input('Enter your password: '))

        if conn.is_connected:
            print('Connected to the database server\n')
            list_vals = []
            cursor = conn.cursor(dictionary = True)
            menu = "Press 1 to insert into ratings table \nPress 2 to update ratings table \nPress 3 to delete row from ratings table\n"
            user_selection = int(input(menu))

            while user_selection < 1 or user_selection > 3:
                print("\nInvalid selection.")
                user_selection = int(input(menu))
                
            if user_selection == 1:
                row_num = int(input('How many rows do you want to insert? '))           
                sql_query = "Insert into ratings (rating, movie_id, reviewer_id) Values (%s, %s, %s);"  
                for i in range(row_num):
                    print('Row', i+1)
                    movie_id = input("Enter the movie id: ")
                    reviewer_id = input("Enter the reviewer id: ")
                    rating = input("Enter the rating for the movie with the provided movie id: ")
                    
                    val = (rating, movie_id, reviewer_id)
                    list_vals.append(val)
                    print()

                cursor.executemany(sql_query, list_vals)
                conn.commit()
                print(cursor.rowcount, ' row was inserted')
                
            elif user_selection == 2:
                number_of_columns = int(input("How many fields do you want to update? "))
                list = []
                for i in range(number_of_columns):
                    movie_id = input("Enter the movie id: ")
                    reviewer_id = input("Enter the reviewer id: ")
                    new_value = input("Enter the new value of the rating: ")
                    sql_query = "Update ratings set rating =  \'" + new_value + "\' where movie_ID = \'" + movie_id + "\' and reviewer_ID = \'" + reviewer_id + "\'"
                    cursor.execute(sql_query)
                    conn.commit() 
                print(cursor.rowcount, "row successfully updated in movies table") 

            elif user_selection == 3:
                number_of_rows = int(input("How many rows do you want to delete? "))
                list = []
                for i in range(number_of_rows):
                    movie_id = input("Enter the movie id: ")
                    reviewer_id = input("Enter the reviewer id: ")
                    sql_query = "delete from ratings where movie_ID = \'" + movie_id + "\' and reviewer_ID = \'" + reviewer_id + "\'"
                    cursor.execute(sql_query)
                    conn.commit() 
                print(cursor.rowcount, "row successfully deleted from reviewers table")    

            cursor.close()        
            
    except Error as e:
        print("Failed to connect due to ", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Disconnected from the database')
   

connect_run()
