from app.main import main
from flask import render_template
from app.models import Evento

@main.route('/calendario')
def calendario():
    e = Evento.query.all()
    return render_template('calendario.html', eventos=e)
