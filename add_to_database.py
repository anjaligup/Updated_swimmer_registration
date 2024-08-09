import psycopg2
from psycopg2 import sql
from tabulate import tabulate 


def insert_into_database(swimmer_name, user_email, phone, class_selected, experience_selected):

    class_name = class_selected + ' ' + experience_selected 
    print(class_name)

    conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    host = 'localhost',
    password = "Lbchariji@1873",
    port = 5432
    )

    cur = conn.cursor()

    query = "INSERT INTO swimmers (swimmer_name, class_name, email, phone_number) VALUES (%s, %s, %s, %s)"

    newphone = str(phone)

    #execute the command
    cur.execute(query, (swimmer_name, class_name, user_email, newphone))
    
    #cur.execute("INSERT INTO swimmers(swimmer_name, class_name, email) VALUES( " + swimmer_name + ', ' + class_name + ', ' + user_email + ');' )

    #make changes to the database 
    conn.commit()

    #close cursor and communication with database
    cur.close()
    conn.close()


def display_database():
    db = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        host = 'localhost',
        password = "Lbchariji@1873",
        port = 5432
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM SWIMMERS")
    result = cursor.fetchall()

    print(tabulate(result, headers=["Swimmer", "Class", "Email", "Phone"], tablefmt="psql"))


