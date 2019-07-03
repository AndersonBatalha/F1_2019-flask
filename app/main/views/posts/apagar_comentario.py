from app.main import main
from app.main.decorators import tem_permissao
from populate_db import Permissoes
from app.models import Comentario, Post, Usuario
from app import db
from flask import flash, redirect, url_for
from flask_login import login_required

@main.route('/comentario/<autor>/<post_slug>/remover')
@login_required
@tem_permissao(Permissoes.MODERAR, msg_erro="Apenas moderadores podem excluir comentários")
def apagar_comentario(autor, post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    usuario = Usuario.query.filter_by(nome_usuario=autor).first()
    comentario = Comentario.query.filter_by(post=post, autor=usuario).first()
    if comentario != None:
        db.session.delete(comentario)
        db.session.commit()
        flash("Comentário excluído", category='success')
    return redirect(url_for('main.post_detail', autor=post.autor.nome_usuario,
                            slug=post.slug))