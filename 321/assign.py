import os
import numpy
import pandas
import sqlite3

budmv = os.path.join(os.path.dirname(__file__), "data", "buddymove_holidayiq.csv")

# connects the SQL database
df = pandas.read_csv(budmv)
# print(df.head())
# print(df.isnull().sum())

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
curs = conn.cursor()

curs.execute('CREATE TABLE USERS(User Id number, Sports number, Religious number, Nature number, Theatre number, Shopping number, Picnic number)')
conn.commit()

df.to_sql('USERS', conn, if_exists='replace', index = False)

curs.execute('''  
SELECT * FROM USERS
          ''')

for row in curs.fetchall():
    print (row)