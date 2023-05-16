DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS users;

CREATE TABLE items(
    id integer primary key autoincrement not null,
    item_name char(30) not null unique,
    price int(200) not null,
    photo_url char(100) not null
);

CREATE TABLE users(
    id integer primary key autoincrement not null,
    username char(30) not null unique,
    password char(50) not null
);

INSERT INTO users VALUES (1,'Administrator_0x1','b37e022b66b74977f9be5cf355d065dce7ab5935');
INSERT INTO items VALUES (1,'Hat',10,'hat.jpg'),(2,'Goofy ahh glasses',20,'goofyahh.jpg'),(3,'Self Portrait',50,'dread.png'),(4,'fish.',100,'fish.png'),(5,'pandas',100,'pandas.jpg'),(6,'rock climbing experience',150,'rock_climbing.jpg');