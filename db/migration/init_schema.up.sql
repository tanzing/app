DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_name TEXT NOT NULL,
    user_type TEXT NOT NULL
);


INSERT INTO posts (user_name, user_type) 
VALUES 
    ('Vasu', 'blop'), 
    ('Sankar', 'blop'), 
    ('Nithsua', 'blop');