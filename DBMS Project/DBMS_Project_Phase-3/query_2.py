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
cur.execute("SELECT match_no, play_stage, audience FROM match_mast WHERE audience=(SELECT max(audience) FROM match_mast);")
match_info = pd.DataFrame(columns = ['match_no','play_stage','audience'])

table = cur.fetchall()

for r in table:
    output_table_df ={'match_no':r[0],'play_stage':r[1],'audience':r[2]}
    match_info = match_info.append(output_table_df, ignore_index = True)
print(match_info)
   

# close the curesor
cur.close()

# close the connection
con.close()

