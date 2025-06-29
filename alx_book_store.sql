-- stores information about Books available in the store 
CREATE DATABASE IF NOT EXISTS alx_book_store;
CREATE TABLE (book_id PRIMARY KEY, title VARCHAR(130), author_id FOREIGN KEY, price DOUBLE, publication_date DATE);
CREATE TABLE Authors (author_id PRIMARY KEY, author_name VARCHAR(215));
CREATE TABLE (customer_id PRIMARY KEY, customer_name VARCHAR(215), email VARCHAR(215), address TEXT);
CREATE TABLE Orders (order_id PRIMARY KEY, customer_id FOREIGN KEY, order_date DATE);
CREATE TABLE Order_Details (orederdetailid PRIMARY KEY, order_id FOREIGN KEY, book_id FOREIGN KEY, quantity DOUBLE);
