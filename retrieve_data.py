# imports
import psycopg2
import pandas as pd

# database connection variables
db_name = "predictive_alarm_db"
db_user = "postgres"
db_password = "Red123"
db_host = "localhost"
db_port = "5432"

# connect to the database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# query to fetch alarm data
query = """
SELECT alarm_id, site_id, alarm_code, severity, past_occurrences, time_of_day, day_of_week, weather_condition
FROM alarms;
"""

df = pd.read_sql(query, conn) # load data into a Pandas DataFrame

conn.close() # close the connection

# save data to CSV
df.to_csv("alarm_data.csv", index=False)
print("Data saved to alarm_data.csv!")
