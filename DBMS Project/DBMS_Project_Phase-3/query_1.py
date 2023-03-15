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

# query execution
cur.execute("SELECT COUNT(DISTINCT match_no) FROM match_details WHERE win_loss = 'D' AND goal_score = '0'")
match_info = pd.DataFrame(columns = ['match_no'])

table = cur.fetchall()

for r in table:
    output_table_df ={'match_no':r[0]}
    match_info = match_info.append(output_table_df, ignore_index = True)
print(match_info)
   

# close the curesor
cur.close()

# close the connection
con.close()

