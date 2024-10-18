create database digiembroidery;
use digiembroidery;
-- Create table for 'Customer'

CREATE TABLE Customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT UNIQUE,
    name VARCHAR(100) NOT NULL,
    profile_pic VARCHAR(100),
    address VARCHAR(40),
    mobile VARCHAR(20) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES auth_user(id) ON DELETE CASCADE
) ENGINE=InnoDB;
-- Create table for 'Product'
CREATE TABLE Product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    product_image VARCHAR(100),
    price INT UNSIGNED NOT NULL,
    description VARCHAR(200)
);

-- Create table for 'Orders'
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    email VARCHAR(50),
    address VARCHAR(500),
    mobile VARCHAR(20),
    order_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES Customer(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Product(id) ON DELETE CASCADE
);

-- Create table for 'Feedback'
CREATE TABLE Feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    feedback VARCHAR(500) NOT NULL,
    date DATE
);

CREATE TABLE payments (
    id INT AUTO_INCREMENT,
    card_number VARCHAR(20) NOT NULL,
    expiry_month VARCHAR(2) NOT NULL,
    expiry_year VARCHAR(2) NOT NULL,
    cv_code VARCHAR(3) NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (id)
);

desc Customer;