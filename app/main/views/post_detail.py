from ..forms import CommentForm
from app.models import Post, Comentario, Usuario
from app.main import main
from app import db
from flask import render_template, flash, redirect, request
from .errors import page_not_found

from flask_login import login_required, current_user
from werkzeug.http import HTTP_STATUS_CODES
from datetime import datetime

@main.route('/post/<autor>/<slug>', methods=['GET', 'POST'])
@login_required
def post_detail(autor, slug):
    form = CommentForm()
    autor_post = Usuario.query.filter_by(nome_usuario=autor).first()
    p = Post.query.filter_by(slug=slug, autor=autor_post).first()
    comentarios = Comentario.query.filter_by(post=p).all()
    u = Usuario.query.get(current_user.id)

    if not p:
        return page_not_found(e=HTTP_STATUS_CODES[404])
    if form.validate_on_submit():
        c = Comentario(
            texto=form.comment.data,
            data=datetime.now(),
            post=p,
            autor=u
        )
        db.session.add(c)
        db.session.commit()

        flash('Comentário adicionado', category='success')
        return redirect(request.url)
    return render_template('post_detail.html', post=p, usuario=u, comentarios=comentarios,
                           form=form)
