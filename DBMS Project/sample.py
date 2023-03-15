
import psycopg2
import pandas as pd

user = "postgres",  # username that you use
# password that you use, you don't need to include your password when submiting your code
password = "Soham@123",
host = "localhost",
port = "5432",
database = "postgres"

try:

    connection = psycopg2.connect(
        user="postgres",  # username that you use
        # password that you use, you don't need to include your password when submiting your code
        password="Soham@123",
        host="localhost",
        port="5432",
        database="postgres"
    )
    connection.close()
except Execption as error:
    print(error)


#     def main():
#     conn = initialize()
#     createTable(conn)
#     insertTable(conn)
#     runQuery(conn)


# if __name__ == "__main__":
#     main()