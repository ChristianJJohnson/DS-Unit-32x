 import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import json 

load_dotenv() # loads the contents of the .env file

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

### An example query
my_dict = {"a": 1, "b": ["dog", "cat", 42], "c": "true"}

insertion_query = f"INSERT INTO table1 (col1, col2) VALUES %s"
execute_values(cur, insertion_query, [
    ("row 1", 'null'),
    ("row two with JSON", json.dumps(my_dict)),
    ("row 3", "3")
])

conn.commit()  
cur.close()
conn.close()

exit()