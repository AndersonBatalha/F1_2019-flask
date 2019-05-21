from flask_login import login_required, current_user
from werkzeug.http import HTTP_STATUS_CODES

from app.main import main
from flask import flash, redirect, url_for

from .errors import not_authorized
from app.models import Funcao
from app import db

@main.route('/remover/<funcao>')
@login_required
def remover_funcao(funcao):
    if current_user.is_authenticated and not current_user.nome_usuario.startswith('adm'):
        return not_authorized(HTTP_STATUS_CODES[401])
    else:
        f = Funcao.query.filter_by(nome_funcao=funcao).first()
        db.session.delete(f)
        db.session.commit()
        flash('Função removida!', category='success')
        return redirect(url_for('main.criar_funcao'))
