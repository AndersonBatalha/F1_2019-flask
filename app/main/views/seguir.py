from app.models import Usuario, Relacionamento
from app.main import main
from flask_login import login_required, current_user
from flask import redirect, url_for
from app import db
from app.main.decorators import tem_permissao
from populate_db import Permissoes

@main.route('/seguir/<usuario>')
@login_required
@tem_permissao(Permissoes.SEGUIR, msg_erro="O usuário não pode seguir outros usuários")
def seguir(usuario):
    u = Usuario.query.filter_by(nome_usuario=usuario).first()
    s = Usuario.query.get(current_user.id)
    if u.nome_usuario != s.nome_usuario:
        r = Relacionamento(
            id_usuario = u.id,
            usuario = u,
            id_seguidor = current_user.id,
            seguidor = s,
        )
        if r.existe_relacionamento(u,s) == False:
            db.session.add(r)
            db.session.commit()
    return redirect(url_for('.perfil_usuario', nome=u.nome_usuario))
