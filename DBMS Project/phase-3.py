import psycopg2
import pandas as pd


def initialize():
    connection = psycopg2.connect(
        user="postgres",  # username that you use
        # password that you use, you don't need to include your password when submiting your code
        password="Soham@123",
        host="localhost",
        port="5432",
        database="postgres"
    )
    connection.autocommit = True
    print(f"Connection established")
    return connection

# If you need to add new tables to your database you can use the following function to create the target table
# assuming that conn is a valid, open connection to a Postgres database
# def createTable(conn):
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


def main():
    conn = initialize()
    createTable(conn)
    insertTable(conn)
    runQuery(conn)


if __name__ == "__main__":
    main()
