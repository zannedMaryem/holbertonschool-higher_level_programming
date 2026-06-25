# SQL Introduction

## Objective

Learn the fundamentals of SQL and MySQL commands for managing databases, creating tables, querying data, and performing basic data definition and data manipulation tasks.

## What You Will Learn

- How to create and manage databases and tables
- How to list and describe database objects
- Basic Data Definition Language (DDL) commands
- Basic Data Manipulation Language (DML) commands
- How to insert, update, delete, and query records

## Basic MySQL Workflow

1. Start the MySQL client:
   ```sql
   mysql -u username -p
   ```
2. Select a database:
   ```sql
   USE database_name;
   ```
3. Run SQL commands.

## Creating Databases and Tables

### Create a database

```sql
CREATE DATABASE school;
```

- Always check if the database exists before creating it:

```sql
CREATE DATABASE IF NOT EXISTS school;
```

### Use a database

```sql
USE school;
```

### Create a table

```sql
CREATE TABLE students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  age INT,
  grade VARCHAR(10)
);
```

## Listing and Describing Tables

### Show databases

```sql
SHOW DATABASES;
```

### Show tables

```sql
SHOW TABLES;
```

### Describe a table structure

```sql
DESCRIBE students;
```

### Show create table statement

```sql
SHOW CREATE TABLE students;
```

## Basic DDL Commands

### Drop a table

```sql
DROP TABLE students;
```

### Drop a database

```sql
DROP DATABASE school;
```

- Drop a database if exixts

```sql
DROP DATABASE IF EXISTS school;
```

### Alter a table

Add a column:

```sql
ALTER TABLE students ADD COLUMN email VARCHAR(100);
```

Modify a column:

```sql
ALTER TABLE students MODIFY COLUMN age SMALLINT;
```

Drop a column:

```sql
ALTER TABLE students DROP COLUMN grade;
```

## Basic DML Commands

### Insert data

```sql
INSERT INTO students (first_name, last_name, age, grade)
VALUES ('Alice', 'Johnson', 18, 'A');
```

### Batch insert

```sql
INSERT INTO students (first_name, last_name, age, grade)
VALUES
  ('Bob', 'Smith', 17, 'B'),
  ('Carmen', 'Lee', 19, 'A');
```

### Select data

```sql
SELECT * FROM students;
```

### Select specific columns

```sql
SELECT first_name, last_name, grade FROM students;
```

### Filter rows

```sql
SELECT * FROM students WHERE age > 17;
```

### Order results

```sql
SELECT * FROM students ORDER BY last_name ASC;
```

### Update data

```sql
UPDATE students
SET grade = 'A+'
WHERE id = 1;
```

### Delete data

```sql
DELETE FROM students
WHERE id = 2;
```

### Truncate a table

```sql
TRUNCATE TABLE students;
```

## Useful Tips

- Use `;` to end every SQL statement.
- Use `SHOW TABLES;` after creating tables to confirm they exist.
- Use `DESCRIBE table_name;` to check column names and types.
- Back up data before running `DROP`, `TRUNCATE`, or mass `DELETE` commands.

## Summary

This guide covers essential SQL and MySQL commands for working with databases and tables, including:
- creating and using databases
- defining tables with DDL
- inserting, querying, updating, and deleting rows with DML
- listing and inspecting schema objects

Keep practicing by creating more tables, inserting sample data, and writing queries to explore result sets.
