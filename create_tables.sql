-- create the sites table
CREATE TABLE sites (
    site_id SERIAL PRIMARY KEY,
    location TEXT NOT NULL,
    contact_info TEXT,
    priority INTEGER
);

-- create the alarms table 
CREATE TABLE alarms (
    alarm_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    site_id INTEGER REFERENCES sites(site_id),
    alarm_code TEXT NOT NULL,
    severity TEXT CHECK (severity IN ('Critical', 'Major', 'Minor', 'Warning')),
    past_occurrences INTEGER DEFAULT 0,
    time_of_day TEXT CHECK (time_of_day IN ('Morning', 'Afternoon', 'Night')),
    day_of_week TEXT CHECK (day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
    weather_condition TEXT
);

-- create a table to store the predicted alarm severities
CREATE TABLE predicted_alarms (
    prediction_id SERIAL PRIMARY KEY,
    alarm_id INTEGER REFERENCES alarms(alarm_id),
    predicted_severity TEXT CHECK (predicted_severity IN ('Critical', 'Major', 'Minor', 'Warning')),
    confidence_score FLOAT,
    prediction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);