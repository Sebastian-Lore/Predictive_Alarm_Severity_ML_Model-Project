# imports
import psycopg2
import random

# database connection variables
db_name = "predictive_alarm_db" 
db_user = "postgres"
db_password = "Red123"
db_host = "localhost"
db_port = "5432"

# connect to the database
connect_db = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

cursor = connect_db.cursor()  # create db cursor

# insert sample site data into db
sites = [
    ("New York", "contact@nyc.com", 1),
    ("Los Angeles", "contact@la.com", 2),
    ("Chicago", "contact@chi.com", 3),
]

cursor.executemany("INSERT INTO sites (location, contact_info, priority) VALUES (%s, %s, %s)", sites)

# Sample alarm codes and features
alarm_codes = ["ALM001", "ALM002", "ALM003"]
severities = ["Critical", "Major", "Minor", "Warning"]
time_of_day_options = ["Morning", "Afternoon", "Night"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weather_conditions = ["Clear", "Rain", "Storm", "Fog", "Snow"]

# Total alarms
total_alarms = 1000
alarms_per_severity = total_alarms // len(severities)  # 1000 / 4 = 250 alarms per severity

# Insert sample alarm data into db with balanced severity
for severity in severities:  # Loop through each severity level
    for _ in range(alarms_per_severity):  # Insert exactly 250 alarms for each severity
        site_id = random.randint(1, len(sites))
        alarm_code = random.choice(alarm_codes)
        past_occurrences = random.randint(0, 50)  # Random past occurrences
        time_of_day = random.choice(time_of_day_options)
        day_of_week = random.choice(days_of_week)
        weather_condition = random.choice(weather_conditions)

        cursor.execute(
            """
            INSERT INTO alarms (site_id, alarm_code, severity, past_occurrences, time_of_day, day_of_week, weather_condition) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (site_id, alarm_code, severity, past_occurrences, time_of_day, day_of_week, weather_condition)
        )

connect_db.commit()  # Commit changes to db

# Close the db cursor and connection
cursor.close()
connect_db.close()

print("Balanced sample data inserted successfully into predictive_alarm_db!")  # Confirmation message
