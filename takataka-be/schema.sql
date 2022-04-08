DROP DATABASE IF EXISTS `takataka`;

CREATE DATABASE `takataka`;

USE `takataka`;

CREATE TABLE `user` (
	`id` INTEGER(25) NOT NULL AUTO_INCREMENT,
	`username` VARCHAR(25) NOT NULL,
	`email` VARCHAR(30) NOT NULL,
	`phone` VARCHAR(15) NOT NULL,
	`address` VARCHAR(100) NOT NULL,
	`password` VARCHAR(1000) NOT NULL,

	PRIMARY KEY(id)
);

CREATE TABLE `product` (
	`id` INTEGER(25) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(25) NOT NULL,
	`category` VARCHAR(10) NOT NULL,
	`price` FLOAT(10) NOT NULL,
	`quantity` INTEGER(10) NOT NULL,
	`description` VARCHAR(500) NOT NULL,

	PRIMARY KEY(id)
);

CREATE TABLE `orders` (
	`id` INTEGER(25) NOT NULL AUTO_INCREMENT,
	`user_id` INTEGER(25) NOT NULL,
	`number` INTEGER(10) NOT NULL,
	`description` VARCHAR(2000) NOT NULL,
	`credit` FLOAT(10) NOT NULL,
	`debit` FLOAT(10) NOT NULL,
	`balance` FLOAT(10) NOT NULL,

	PRIMARY KEY(id)
);


CREATE TABLE `announcements` (
	`id` INTEGER(25) NOT NULL AUTO_INCREMENT,
	`content` VARCHAR(256) NOT NULL,
	`time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`status` INT(2) NOT NULL DEFAULT 1,

	PRIMARY KEY(id)
);

INSERT INTO announcements (content) VALUES ('Hello, welcome to our platform!'), ('Would you like a tour?');

INSERT INTO product (name, category, price, quantity, description) VALUES 
("Product 1", "category 1", 100.0, 100, "Brief description"), 
("Product 2", "category 1", 100.0, 100, "Brief description"), 
("Product 3", "category 1", 100.0, 100, "Brief description"), 
("Product 4", "category 1", 100.0, 100, "Brief description"), 
("Product 5", "category 1", 100.0, 100, "Brief description"),
("Product 1", "category 1", 100.0, 100, "Brief description");