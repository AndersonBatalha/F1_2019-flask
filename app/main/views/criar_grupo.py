from app.main import main
from app.main.decorators import tem_permissao
from populate_db import Permissoes
from ..forms import CriarGrupoForm
from app.models import Grupo, MembrosGrupo
from app import db
from flask import render_template, flash
from flask_login import login_required
from sqlalchemy.exc import IntegrityError
from slugify import slugify

@main.route('/novo_grupo', methods=['GET', 'POST'])
@login_required
@tem_permissao(Permissoes.ADMINISTRAR, msg_erro="Apenas administradores podem criar grupos")
def criar_grupo():
    form = CriarGrupoForm()
    if form.validate_on_submit():
        g = Grupo(
            nome_grupo=form.nome_grupo.data,
            descricao=form.desc.data,
            slug=slugify(form.nome_grupo.data)
        )
        if len(form.usuarios_selecionados()) > 0:
            db.session.add(g)
            print('membros',form.usuarios_selecionados())
            for usuario in form.usuarios_selecionados():
                membro = MembrosGrupo(
                    membro=usuario,
                    grupo=g
                )
                db.session.add(membro)

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            flash('Grupo adicionado!', category='success')
        else:
            flash('Selecione pelo menos um usuário para continuar', category='warning')
    return render_template('forms/criar_grupo.html', form=form, grupos=Grupo.query.all())