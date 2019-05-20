from app.main import main
from flask import flash, redirect, url_for
from app.models import Funcao
from app import db

@main.route('/remover/<funcao>')
def remover_funcao(funcao):
    f = Funcao.query.filter_by(nome_funcao=funcao).first()
    db.session.delete(f)
    db.session.commit()
    flash('Função removida!', category='success')
    return redirect(url_for('main.criar_funcao'))
