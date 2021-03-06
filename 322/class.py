 import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import sqlite3
import json 

load_dotenv() # loads the contents of the .env file

rpg_db = os.path.join(
    os.path.dirname(__file__), "data", "rpg_db.sqlite3"
)

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()

conn_sql = sqlite3.connect(rpg_db)
conn_sql.text_factory = lambda x: str(x, 'latin1')

cur_sql = conn_sql.cursor()

cur_sql.execute("SELECT * FROM armory_item")
cur_sql.fetchall()