

USE sales;

CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item_id INT,
    quantity INT NOT NULL,
    delivery_address VARCHAR(255) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Foreign Key (user_id) REFERENCES customers(user_id)
    
);


DESC orders;
alter table orders add item_name VARCHAR(225)

TRUNCATE orders;
select * from orders;


CREATE TABLE IF NOT EXISTS categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);


INSERT INTO categories (category_name) VALUES
('Vegetarian'),
('Non-Vegetarian'),
('Vegan');


CREATE TABLE IF NOT EXISTS items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT
);


INSERT INTO items (item_name, price, category_id) VALUES
('Biriyani', 150.00, 2),  -- Non-Vegetarian
('Paneer', 100.00, 1),    -- Vegetarian
('Butter Chicken', 200.00, 2);  -- Non-Vegetarian

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    item_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2),
    FOREIGN KEY (item_id) REFERENCES items(item_id)
);


INSERT INTO order_items (order_id, item_id, quantity, price) VALUES
(1, 1, 2, 150.00),
(2, 2, 1, 100.00),
(3, 3, 3, 200.00);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    amount DECIMAL(10, 2),
    paid_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO payments (order_id, payment_method, payment_status, amount) VALUES
(1, 'Credit Card', 'Paid', 300.00),
(2, 'Debit Card', 'Paid', 100.00),
(3, 'GPay', 'Pending', 600.00);


CREATE TABLE IF NOT EXISTS customers (
    user_id INT UNIQUE NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone_number VARCHAR(15),
    email VARCHAR(255)
);
alter TABLE customers MODIFY user_id int UNIQUE NOT NULL AUTO_INCREMENT;
DESC customers;
select * from customers;

select * from orders;