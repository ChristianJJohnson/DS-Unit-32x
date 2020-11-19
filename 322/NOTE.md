# SQL for Analysis

#### At the end of this module, you should be able to:
* deploy and use a simple PostgreSQL database
* 
create a data pipeline with SQL

Example of a table creation
```
CREATE TABLE test_table_name (
  id        SERIAL PRIMARY KEY, -- if your table has a primary key it's best to specify it in table creation
  col1  varchar(40) NOT NULL,
  col2    JSONB
);
```

Example of adding data to test_table_name

```
INSERT INTO test_table_name (col1, col2) VALUES -- column names match those in the table creation
(
    'Column One String', null),
(
  'Another row, with JSON',
  '{ "a": 1, "b": ["dog", "cat", 42], "c": true }'::JSONB -- allows you to store json dict like objects
);
```