import sqlite3

connection = sqlite3.connect('posts.db')

with open('./db/migration/init_schema.up.sql') as f:
    connection.executescript(f.read())
