from app.main import main
from app.main.decorators import tem_permissao
from populate_db import Permissoes
from app.models import Grupo
from app import db
from flask import flash, redirect, url_for
from flask_login import login_required

@main.route('/<slug>/remover')
@login_required
@tem_permissao(Permissoes.ADMINISTRAR, msg_erro="Apenas administradores podem excluir grupos")
def excluir_grupo(slug):
    grupo = Grupo.query.filter_by(slug=slug).first()
    if grupo is not None:
        db.session.delete(grupo)
        db.session.commit()
        flash("Excluído com sucesso", category='success')
    return redirect(url_for('main.criar_grupo'))