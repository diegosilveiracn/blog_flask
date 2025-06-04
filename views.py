from main import app, db
from models import Post
from flask import render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

@app.route("/")
def listar_postagens():
    posts = db.session.query(Post).all()
    return render_template("index.html", posts=posts)

@app.route('/criar_postagem', methods=('GET', 'POST'))
def criar_postagem():
    if request.method == 'POST':
        post = Post(title=request.form['title'], content= request.form['content'])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('listar_postagens'))
    return render_template('nova_postagem.html')

@app.route('/<int:post_id>')
def abrir_postagem(post_id):
    post = db.session.query(Post).filter_by(id=post_id).first()
    return render_template('postagem.html', post=post)

@app.route('/<int:post_id>/editar_postagem', methods=('GET', 'POST'))
def editar_postagem(post_id):
    if request.method == 'POST':
        post = db.session.query(Post).filter_by(id=post_id).first()
        post.title = request.form['title']
        post.title = content= request.form['content']
        db.session.commit()
        return redirect(url_for('listar_postagens'))
    post = db.session.query(Post).filter_by(id=post_id).first()
    return render_template('edicao_postagem.html', post=post)

@app.route('/<int:post_id>/deletar_postagem', methods=('GET',))
def deletar_postagem(post_id):
    post = db.session.query(Post).filter_by(id=post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('listar_postagens'))