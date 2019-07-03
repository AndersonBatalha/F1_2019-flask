from app.main import main
from flask import render_template
from app.main.decorators import tem_permissao
from populate_db import Permissoes

@main.route('/admin')
@tem_permissao(Permissoes.ADMINISTRAR, msg_erro="Acesso restrito a administradores do sistema")
def admin_page():
    return render_template('admin.html')