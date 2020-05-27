# Intro into SQL


## Definitions:
* Database - Help store and retrieve data in a efficient way.

* Data Pipeline - Software used to eliminate many manual steps from the process and enables a smooth automated flow of data from one place to the next. It defines what, where and how data is collected.[more info](https://www.alooma.com/blog/what-is-a-data-pipeline)

;

* SQL - Structured Query Language - A language that communicates with databases. Used in varying degrees by data scientists, software engineers, DevOps, and MBAs, SQL is the beginning (and sometimes entirety) of many data pipelines.

* Schema Diagram - A Diagraph that shows relationships (columns, data types, views, stored procedures, primary keys, foreign keys, etc) between objects in a database.

* Primary Key - Uniquely identify a given row, ultimately helping pinpoint, locate, and reference the specific rows in a efficient way.

* Pointer/Foreign Key - identifier of a related row in another table.



### At the end of this module, you should be able to:
* write basic SQL queries to get specific subsets of data from a database and answer basic "business questions"
* understand the purpose of SQL join, and perform joins to access data from multiple tables

## Part 0
### Commands and clauses available for use in a SQL query, (c)clauses are in the order they are to be used:
* SELECT (c) - is used to select data from a database. The data returned is stored in a result table, called the result-set.

* AS - Aliases a selection

* "--" - Comment a row

* FROM (c) - is used to specify which table to select or delete data from (customers, artist, robots, ect).

* JOIN (c) - is used to combine rows from two or more tables, based on a related column between them.

* WHERE (c) - is used to filter records. The WHERE clause is used to extract only those records that fulfill a specified condition., used with conditions (=, in, AND, OR, <, >, ect) 

* GROUP BY (c) - Groups rows that have the same values into a summary.

* HAVING (c) - was added to SQL because the WHERE keyword could not be used with Often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

* ORDER BY (c) - is used to sort the result-set in ascending or descending order. The ORDER BY keyword sorts the records in ascending (ASC) order by default. To sort the records in descending order, use the DESC keyword.

* count(countSomething) - count number of rows

* count(distinct countSomething) - count unique values of rows.

* Limit (c) - return the specified value as the max number of rows.

## Guidance
SQL is arranged in various tables with a column and row like structure. We can view each table as representing another object class (sometimes these are known as entities). Each column viewed as another function/attribute and each row a instance of the object class.

When using GROUP BY clause we should usually look to also SELECT the item that's being grouped.

Whatever you don't GROUP BY combine it with what you are grouping by. If you are not wanting to combine them remove the item from the selection.

### Join
* (INNER) JOIN: Returns records that have matching values in both tables
* LEFT (OUTER) JOIN: Returns all records from the left table, and the matched records from the right table
* RIGHT (OUTER) JOIN: Returns all records from the right table, and the matched records from the left table
* FULL (OUTER) JOIN: Returns all records when there is a match in either left or right table

Make sure to join ON a like values for best  results
```SELECT *
FROM albums
JOIN artists on albums.ArtistID = artists.ArtistID
```

### Python

```# When working with sqlite3
import sqlite3

# connects the SQL database
conn = sqlite3.connect("pathToFile") 

# Allows you an to invoke methods that execute SQLite statements
curs = conn.cursor()


# SQL query you want to perform
query = "SELECT * FROM customers LIMIT 3"

result = curs.execute(query).fetchall()
print(result)
```

#### Best practice for connecting to file
```# interact with os
import os

# This string of characters joins together this line and can be used to reproduce pointing to a file in a location regardless of the os type
filePath = os.path.join(os.path.dirname(__file__), "..", "fileFolder", "someFile")
```