import psycopg2
import pandas as pd
import warnings

warnings.filterwarnings('ignore')


# connecting to db
con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Soham@123",
    port="5432"
)

# cursor
cur = con.cursor()

# Print PostgreSQL details
print("PostgreSQL server information")
print(con.get_dsn_parameters(), "\n")

# Executing a SQL query
cur.execute("SELECT version();")

# Fetch result
record = cur.fetchone()
print("You are connected to - ", record, "\n")


# close the curesor
cur.close()

# close the connection
con.close()
