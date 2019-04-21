from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipes')
def equipes():
    return render_template('equipes.html')

@app.route('/pilotos')
def pilotos():
    return render_template('pilotos.html')

@app.route('/calendario')
def calendario():
    return render_template('calendario.html')

@app.route('/classificacao')
def classificacao():
    return render_template('classificacao.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')