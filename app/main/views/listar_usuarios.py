from app.main import main
from flask import render_template
from app.models import Usuario

@main.route('/usuarios')
def listar_usuarios():
    u = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=u)
