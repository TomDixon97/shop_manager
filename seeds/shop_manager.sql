-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS items;
DROP SEQUENCE IF EXISTS items_id_seq;
DROP TABLE IF EXISTS orders;
DROP SEQUENCE IF EXISTS orders_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS items_id_seq;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    quantity INTEGER
);

CREATE SEQUENCE IF NOT EXISTS orders_id_seq;
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    item_name VARCHAR(255),
    item_id INTEGER,
    amount INTEGER,
    date_placed VARCHAR(255)
);


INSERT INTO items (name, quantity) VALUES ('Apples', 1000);
INSERT INTO items (name, quantity) VALUES ('Oranges', 10);



