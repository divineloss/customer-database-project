CREATE TABLE addresses (
    `id` INT NOT NULL AUTO_INCREMENT, 
    `address1` VARCHAR(50) NOT NULL, 
    `address2` VARCHAR(50), 
    `city` VARCHAR(50) NOT NULL, 
    `state` VARCHAR(20) NOT NULL, 
    `postalCode` VARCHAR(20) NOT NULL, 
    PRIMARY KEY (`id`)
);