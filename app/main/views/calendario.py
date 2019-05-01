from app.main import main
from flask import render_template

@main.route('/calendario')
def calendario():
    return render_template('calendario.html')
