from app.main import main
from flask import render_template

@main.route('/pilotos')
def pilotos():
    return render_template('pilotos.html')
