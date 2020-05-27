# READ CSV
import os
import pandas as pd

titanic = os.path.join(
    os.path.dirname(__file__), "data", "titanic.csv"
)
df = pd.read_csv(titanic)
print(df.head())

# CONNECT TO PG DATABASE
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")


connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

# CREATE TABLE

titanic_query = '''
CREATE TABLE IF NOT EXISTS Passengers (
  id SERIAL PRIMARY KEY,
  Survived INTEGER,
  Pclass INTEGER,
  Name VARCHAR NOT NULL,
  Gender VARCHAR NOT NULL,
  Age FLOAT,
  Sib_Spou_Count INTEGER,
  Par_Chi_Count INTEGER,
  Fare FLOAT
'''


# INSERT DATA IN THE TABLE

list_of_tuples = tuple(df.itertuples(index=False, name=None))

insertion_query = "INSERT INTO passengers (Survived, Pclass, Name, Gender, Age, Sib_Spou_Count, Par_Chi_Count, Fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples)


cursor.execute(titanic_query)
connection.commit()
cursor.close()
connection.close()