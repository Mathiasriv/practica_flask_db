CREATE DATABASE IF NOT EXISTS db_flask_2;
USE db_flask_2;
CREATE TABLE IF NOT EXISTS person(
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    dni INT(8) NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
)

INSERT INTO person VALUES
(1,'juan', 'Alvarez', 1234, 'juan@gmail.com'),
(2,'ana', 'Perez', 5678, 'ana@gmail.com');





    


















        
    