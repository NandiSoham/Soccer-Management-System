
#!/usr/bin/env python
# coding: utf-8

# Insatlling libraries
# For Mac you may use the following to install psycopg2-binary:
# pip3 install psycopg2-binary
# And in your code use:
# import psycopg2
# To use pandas install it like:
# pip3 install pandas

import psycopg2
import pandas as pd

def initialize():
    connection = psycopg2.connect(
        user = "postgres", #username that you use
        password = "yourpassword", #password that you use, you don't need to include your password when submiting your code
        host = "localhost", 
        port = "5432", 
        database = "postgres"
    )
    connection.autocommit = True
    return connection
    
# If you need to add new tables to your database you can use the following function to create the target table 
# assuming that conn is a valid, open connection to a Postgres database
def createTable(conn):
    with conn.cursor() as cursor:
        cursor.execute(f"""
            DROP TABLE IF EXISTS editions;
            CREATE TABLE editions (
                bookid         NUMERIC,
                date           DATE,
                edition        TEXT,
                lang           TEXT,
                pubid          INTEGER
            );
            ALTER TABLE editions ADD PRIMARY KEY (bookid, date);
        """)
    print(f"Created editions table")
   
# If you need created and added a new table to your database you can use the following function to insert data into your target table
def insertTable(conn):
    #You can import your data from a CSV file by pg_insert_v1
    pg_insert_v1 = '''COPY editions(bookid,date,edition,
            lang,pubid)
            FROM 'editions.csv'
            DELIMITER ','
            CSV HEADER;'''
    #Or You can get the get the column name of a table inside the database and enter some values by using the following commented lines
    # pg_insert_v2 = """ INSERT INTO editions
    #             VALUES (%s,%s,%s,%s,%s)"""
    # inserted_values = (1, '05/16/2022', '4th edition', 'English', '101')


##Execute the the insert SQL string
    with conn.cursor() as cursor:
        cursor.execute(pg_insert_v1)
        count = cursor.rowcount
        print (count, "Successfully inserted")

def runQuery(conn):
    select_Query = "select * from editions"
    editions_df = pd.DataFrame(columns = ['Book ID', 'Date', 'Edition', 'Language', 'Pub ID'])
    with conn.cursor() as cursor:
        cursor.execute(select_Query)
        records = cursor.fetchall()
        for row in records:
            output_df = {'Book ID': row[0], 'Date': row[1], 'Edition': row[2], 'Language': row[3], 'Pub ID':row[4]}
#             print("Book Id = ", row[0], )
#             print("Date = ", row[1])
#             print("Edition  = ", row[2])
#             print("Language = ", row[3])
#             print("Pub Id = ", row[4])
            editions_df = editions_df.append(output_df, ignore_index=True)
    
        print(editions_df)

def main():
    conn = initialize()
    createTable(conn)
    insertTable(conn)
    runQuery(conn)


if __name__ == "__main__":
    main()

sample_code.py
Displaying sample_code.py.