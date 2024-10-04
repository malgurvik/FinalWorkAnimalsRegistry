CREATE DATABASE Human_Friends;
USE Human_Friends;
CREATE TABLE Cats (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250)
);

CREATE TABLE Dogs (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250)
);

CREATE TABLE Hamsters (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250)
);

CREATE TABLE Horses (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250)
);

CREATE TABLE Camels (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250)
);

CREATE TABLE Donkeys (
ID INT PRIMARY KEY AUTO_INCREMENT,
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250)
);

INSERT Cats (Name, Birthday, Commands)
VALUES
('Whiskers', '2019-05-15', 'Sit, Pounce'),
('Smudge', '2020-02-20', 'Sit, Pounce, Scratch'),
('Oliver', '2020-06-30', 'Meow, Scratch, Jump'),
('Tomas','2022-10-09', 'Sit, Meow');

INSERT Dogs (Name, Birthday, Commands)
VALUES
('Fido', '2020-01-01', 'Sit, Stay, Fetch'),
('Buddy', '2018-12-10', 'Sit, Paw, Bark'),
('Bella', '2019-11-11', 'Sit, Stay, Roll'),
('Pups','2022-07-09', 'Paw, Bark');

INSERT Hamsters (Name, Birthday, Commands)
VALUES
('Hammy', '2021-03-10', 'Roll, Hide'),
('Peanut', '2021-08-01', 'Roll, Spin');

INSERT Horses (Name, Birthday, Commands)
VALUES
('Thunder', '2015-07-21', 'Trot, Canter, Gallop'),
('Storm', '2014-05-05', 'Trot, Canter'),
('Blaze', '2016-02-29', 'Trot, Jump, Gallop');

INSERT Camels (Name, Birthday, Commands)
VALUES
('Sandy', '2016-11-03', 'Walk, Carry Load'),
('Dune', '2018-12-12', 'Walk, Sit'),
('Dune', '2018-12-12', 'Walk, Sit');

INSERT Donkeys (Name, Birthday, Commands)
VALUES
('Eeyore', '2017-09-18', 'Walk, Carry Load, Bray'),
('Burro', '2019-01-23', 'Walk, Bray, Kick');

SELECT * FROM Cats;

SELECT * FROM Horses;

DROP TABLE Camels;


CREATE TABLE Horses_and_Donkeys (
ID INT PRIMARY KEY AUTO_INCREMENT,
Type VARCHAR(50),
Name VARCHAR(50) NOT NULL,
Birthday DATE NOT NULL,
Commands VARCHAR(250));

INSERT Horses_and_Donkeys(Type, Name, Birthday, Commands)
SELECT 'Horse', Name, Birthday, Commands FROM Horses
UNION
SELECT 'Donkey', Name, Birthday, Commands FROM Donkeys;

SELECT * FROM Horses_and_Donkeys;

CREATE TABLE Young_animals AS
SELECT ID, Name, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_months
FROM Cats WHERE TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) BETWEEN 12 AND 36
UNION
SELECT ID, Name, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_months
FROM Dogs WHERE TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) BETWEEN 12 AND 36
UNION
SELECT ID, Name, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_months
FROM Hamsters WHERE TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) BETWEEN 12 AND 36
UNION
SELECT ID, Name, Birthday, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age_in_months
FROM Horses_and_Donkeys WHERE TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) BETWEEN 12 AND 36;

SELECT * FROM Young_animals;

CREATE TABLE All_animals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(50),
    Name VARCHAR(50) NOT NULL,
    Birthday DATE NOT NULL,
    Commands VARCHAR(200),
    Age_in_months INT
);

INSERT All_animals(Type, Name, Birthday, Commands, Age_in_months)
SELECT Type, Name, Birthday, Commands, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) FROM Horses_and_Donkeys
UNION
SELECT 'Cat', Name, Birthday, Commands, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) FROM Cats
UNION
SELECT 'Dog', Name, Birthday, Commands, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) FROM Dogs
UNION
SELECT 'Hamster', Name, Birthday, Commands, TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) FROM Hamsters;

SELECT * FROM All_animals;


