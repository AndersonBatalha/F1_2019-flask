from app.main import main
from flask import render_template
from app.models import Equipe

@main.route('/equipes')
def equipes():
    e = Equipe.query.all()
    return render_template('equipes.html', equipes=e)
