/*
class Person():
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = None
        self.income = 0.0
        self.status = None
*/

CREATE TABLE customers (
    `id` INT NOT NULL AUTO_INCREMENT, 
    `fname` VARCHAR(20) NOT NULL, 
    `lname` VARCHAR(20) NOT NULL, 
    `age` INT NOT NULL, 
    `gender` VARCHAR(20), 
    `income` DECIMAL, 
    `status` VARCHAR(20), 
    PRIMARY KEY (`id`)
);