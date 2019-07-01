from flask_login import login_required

from app.main import main
from flask import flash, redirect, url_for

from app.main.decorators import tem_permissao
from populate_db import Permissoes
from app.models import Funcao
from app import db

@main.route('/remover/<funcao>')
@tem_permissao(Permissoes.ADMINISTRAR,
               msg_erro="Apenas administradores podem remover funções")
@login_required
def remover_funcao(funcao):
    f = Funcao.query.filter_by(nome_funcao=funcao).first()
    db.session.delete(f)
    db.session.commit()
    flash('Função removida!', category='success')
    return redirect(url_for('main.criar_funcao'))
