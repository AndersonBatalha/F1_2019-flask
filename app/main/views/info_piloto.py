from app.models import Piloto, Titulo
from app.main import main
from flask import render_template
from .errors import page_not_found

@main.route('/piloto/<slug>')
def info_piloto(slug):
    p = Piloto.query.filter_by(slug=slug).first()
    t = Titulo.query.filter(Titulo.id_piloto==Piloto.id_piloto).add_column(Piloto.nome_piloto).all()
    if not p:
        return page_not_found(e='O nome solicitado não existe')
    return render_template('perfil_piloto.html', piloto=p, titulos=t)
