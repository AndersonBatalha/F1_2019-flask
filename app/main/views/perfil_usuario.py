from app.models import Usuario, Relacionamento
from app.main import main
from flask import render_template
from flask_login import login_required, current_user
from .errors import page_not_found
from app.models import Relacionamento

@main.route('/usuario/<nome>')
@login_required
def perfil_usuario(nome):
    u = Usuario.query.filter_by(nome_usuario=nome).first()
    s = Usuario.query.get(current_user.id)
    seguidores = Relacionamento.query.filter_by(usuario=u).all()
    if not u:
        return page_not_found(e='O usuário não existe')
    r = Relacionamento.query.filter_by(usuario=u, seguidor=s).first()
    return render_template('perfil_usuario.html', usuario=u,
                           seguidor=s, s=seguidores, relacionamento=r)
