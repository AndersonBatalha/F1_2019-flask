from app.main import main
from flask import render_template
from app.models import Piloto, Titulo

@main.route('/pilotos')
def pilotos():
    p = Piloto.query.all()

    return render_template('pilotos.html', pilotos=p)
