from app.models import Post
from app.main import main
from flask import render_template
from populate_db import Permissoes
from app.main.decorators import tem_permissao

@main.route('/posts')
@tem_permissao(Permissoes.ESCREVER + Permissoes.POSTAR,
               msg_erro="O usuário atual não tem permissão para adicionar posts")
def posts():
    posts = Post.query.order_by(Post.data.desc()).all()
    return render_template('posts.html', posts=posts)
