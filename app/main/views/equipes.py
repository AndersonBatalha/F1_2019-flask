from app.main import main
from flask import render_template

@main.route('/equipes')
def equipes():
    return render_template('equipes.html')
