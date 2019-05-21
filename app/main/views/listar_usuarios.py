from app.main import main
from app.models import Usuario
from flask import render_template
from flask_login import login_required

@main.route('/usuarios')
@login_required
def listar_usuarios():
    u = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=u)
