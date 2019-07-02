from app.main import main
from flask import render_template
from app.models import Grupo, MembrosGrupo
from sqlalchemy import distinct

@main.route('/<slug>/membros')
def grupos(slug):
    g = Grupo.query.filter_by(slug=slug).first()
    usuarios = [u.membro for u in MembrosGrupo.query.filter_by(grupo=g).all()]
    return render_template('grupos.html', grupo=g, usuarios=usuarios)
