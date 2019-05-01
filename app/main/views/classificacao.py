from app.main import main
from flask import render_template

@main.route('/classificacao')
def classificacao():
    return render_template('classificacao.html')
