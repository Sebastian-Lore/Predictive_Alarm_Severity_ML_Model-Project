# This file transforms the data in the alarm_data.csv file into a format that ML models can learn from effectively by doing four key things.
#   1) Handles Missing Values.
#   2) Encodes Categorical Variables.
#   3) Converts severity into a Numeric Target Variable.
#   4) Scales Numeric Features.

# imports
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

df = pd.read_csv("alarm_data.csv") # load the dataset

df.ffill(inplace=True) # handle missing values by forward filling them

# encode the target variable (severity)
severity_mapping = {"Critical": 3, "Major": 2, "Minor": 1, "Warning": 0}
df["severity"] = df["severity"].map(severity_mapping)

# use One-hot encoding to encode categorical features
categorical_features = ["alarm_code", "time_of_day", "day_of_week", "weather_condition"]
df = pd.get_dummies(df, columns=categorical_features, drop_first=True)
df = df.astype(int)  # convert True/False to 1/0

# scale numeric features (past_occurrences)
scaler = StandardScaler()
df["past_occurrences"] = scaler.fit_transform(df[["past_occurrences"]])

df.to_csv("preprocessed_alarm_data.csv", index=False) # put the preprocessed data into a csv file

print("Preprocessing complete!")