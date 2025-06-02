import sqlite3
from main import app
from flask import render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def listar_postagens():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("index.html", posts=posts)

@app.route('/<int:post_id>')
def abrir_postagem(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return render_template('postagem.html', post=post)

@app.route('/criar_postagem', methods=('GET', 'POST'))
def criar_postagem():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('listar_postagens'))

    return render_template('nova_postagem.html')

@app.route('/<int:post_id>/editar_postagem', methods=('GET', 'POST'))
def editar_postagem(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()

    if request.method == 'POST':
        id = post_id
        title = request.form['title']
        content = request.form['content']

        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ?'
                        ' WHERE id = ?',
                        (title, content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('listar_postagens'))
    return render_template('edicao_postagem.html', post=post)

@app.route('/<int:post_id>/deletar_postagem', methods=('GET',))
def deletar_postagem(post_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('listar_postagens'))