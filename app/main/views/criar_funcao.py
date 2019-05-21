from app.main import main
from .errors import not_authorized
from ..forms import FuncaoForm
from app.models import Funcao
from app import db
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import HTTP_STATUS_CODES

@main.route('/nova_funcao', methods=['GET', 'POST'])
@login_required
def criar_funcao():
    if current_user.is_authenticated and not current_user.nome_usuario.startswith('adm'):
        return not_authorized(HTTP_STATUS_CODES[401])
    else:
        funcoes = Funcao.query.all()
        form = FuncaoForm()
        if form.validate_on_submit():
            f = Funcao.query.filter_by(nome_funcao=form.nome_funcao.data).first()
            if f is None:
                f = Funcao()
                f.nome_funcao = form.nome_funcao.data
                db.session.add(f)
                db.session.commit()
                flash('Função adicionada!', category='success')
                return redirect(url_for('.criar_funcao'))
            else:
                flash('A função %s já existe!' %(form.nome_funcao.data), category='danger')
        return render_template('criar_funcao.html', form=form, funcoes=funcoes)

