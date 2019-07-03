from app.main import main
from flask import render_template
from app.main.decorators import tem_permissao
from populate_db import Permissoes

@main.route('/moderate')
@tem_permissao(Permissoes.MODERAR, msg_erro="Acesso restrito a moderadores")
def moderator_page():
    return render_template('moderador.html')