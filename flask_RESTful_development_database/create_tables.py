import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(table)

table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(table)

cursor.execute("INSERT INTO items VALUES ('piano', 10.99)")

connection.commit()

connection.close()