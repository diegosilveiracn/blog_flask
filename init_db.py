import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Primeiro Postagem', 'Conteúdo da primeira postagem.'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Segundo Postagem', 'Conteúdo da segunda postagem.'))

connection.commit()
connection.close()