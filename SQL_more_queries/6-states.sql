-- Create database and table
CREATE DATABASE TF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(245) NOT NULL
);
