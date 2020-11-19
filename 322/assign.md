## Assignment
Reproduce (debugging as needed) the live lecture task of setting up and inserting the RPG data into a PostgreSQL database, and add the code you write to do so.

Then, set up a new table for the Titanic data (titanic.csv) - spend some time thinking about the schema to make sure it is appropriate for the columns. Enumerated types may be useful. Once it is set up, write a insert_titanic.py script that uses psycopg2 to connect to and upload the data from the csv, and add the file to your repo. Then start writing PostgreSQL queries to explore the data!

## Resources and Stretch Goals
PostgreSQL is a real true powerful production database - explore the official documentation as well as larger hosted offerings such as Amazon RDS.

Try to install and use the actual psycopg2 package (as opposed to psycop2-binary) - this builds from source, so there are prerequisites you'll need. This may be good to do inside a container!

Want to try larger PostgreSQL databases? Check out these sample databases, but note you'll probably need a local installation of PostgreSQL to be able to use them.

And if you do all the above, you can revisit Django as briefly introduced yesterday. This is a complete stretch goal (i.e. it's not a core Data Science skill and is OK if you don't get to it at all), but it is a powerful and widely-used web application framework. Also, the Django ORM can connect to a variety of SQL backends, and a very typical setup is to use SQLite for (initial) local development but PostgreSQL for deployment.