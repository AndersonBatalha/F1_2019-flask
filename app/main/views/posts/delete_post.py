from app.models import Post
from app.main.decorators import tem_permissao
from populate_db import Permissoes
from app.main import main
from app import db
from flask import redirect, flash, url_for

@main.route('/delete_post/<slug>')
@tem_permissao(Permissoes.MODERAR, msg_erro="Apenas moderadores podem excluir postagens")
def delete_post(slug):
    post = Post.query.filter_by(slug=slug).first()
    db.session.delete(post)
    db.session.commit()
    flash("Postagem removida!", category='info')
    return redirect(url_for('main.posts'))