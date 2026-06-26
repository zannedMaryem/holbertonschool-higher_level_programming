# SQL More Queries - Learning Objectives

This README summarizes the main SQL concepts covered in this project.

## 1. Managing privileges for users on databases and tables

Privileges control what a user is allowed to do.

### Grant privileges
```sql
GRANT SELECT, INSERT, UPDATE ON database_name.table_name TO 'user_name'@'localhost';
```

### Revoke privileges
```sql
REVOKE UPDATE ON database_name.table_name FROM 'user_name'@'localhost';
```

### Create a user
```sql
CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'password';
```

### Apply privileges to a database
```sql
GRANT ALL PRIVILEGES ON database_name.* TO 'user_name'@'localhost';
```

> Use `FLUSH PRIVILEGES;` after changing permissions in some MySQL setups.

## 2. What is a PRIMARY KEY?

A `PRIMARY KEY` uniquely identifies each row in a table.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

Rules:
- It must contain unique values.
- It cannot contain `NULL` values.

## 3. What is a FOREIGN KEY?

A `FOREIGN KEY` links a column in one table to the primary key in another table.

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

This enforces a relationship between the two tables.

## 4. Using NOT NULL and UNIQUE constraints

### NOT NULL
Ensures a column cannot contain `NULL` values.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

### UNIQUE
Ensures all values in a column are distinct.

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    email VARCHAR(100) UNIQUE
);
```

## 5. Retrieving data from multiple tables in one request

You can query data from several tables using joins or subqueries.

Example:
```sql
SELECT users.name, orders.id
FROM users
JOIN orders ON users.id = orders.user_id;
```

## 6. What are subqueries?

A subquery is a query inside another query.

```sql
SELECT name
FROM users
WHERE id IN (
    SELECT user_id
    FROM orders
);
```

Subqueries are useful for filtering, calculating, or retrieving related values.

## 7. What are JOIN and UNION?

### JOIN
A `JOIN` combines rows from two or more tables based on a related column.

Common types:
- `INNER JOIN`
- `LEFT JOIN`
- `RIGHT JOIN`

Example:
```sql
SELECT users.name, orders.id
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

### UNION
`UNION` combines the result sets of two queries into one result.

```sql
SELECT name FROM users
UNION
SELECT name FROM employees;
```

## Summary

By the end of this project, you should be able to:
- Manage user privileges on databases and tables.
- Understand and use `PRIMARY KEY` and `FOREIGN KEY`.
- Apply `NOT NULL` and `UNIQUE` constraints.
- Retrieve data from multiple tables.
- Use subqueries, `JOIN`, and `UNION` effectively.
