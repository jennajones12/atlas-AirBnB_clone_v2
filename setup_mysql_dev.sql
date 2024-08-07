-- make a new database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- make a new user with all privileges on the database.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges to the new user on the database.
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- hbnb_dev should have SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
