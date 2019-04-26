# imports
import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField
from wtforms.validators import Email, DataRequired, Length, EqualTo

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# config
BASE_DIR = os.path.abspath(os.path.dirname(__name__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Z}hrdI2xFMN_xc]'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# forms

class RegisterForm(FlaskForm):
    nome = StringField('Nome completo', validators=[
        DataRequired(),
        Length(min=5, max=40)
    ])
    email = StringField('E-mail', validators=[
        DataRequired(),
        Length(min=5, max=30)
    ])
    data_nasc = DateField('Data de nascimento')
    endereco = StringField('Endereço', validators=[ DataRequired() ])
    numero = IntegerField('Número', default=0)
    complemento = StringField("Complemento")
    bairro =  StringField("Bairro", validators=[ DataRequired() ])
    cidade = StringField("Cidade", validators=[ DataRequired() ])
    estado = StringField("Estado", validators=[ DataRequired() ])
    pais = StringField("País", validators=[ DataRequired() ])
    senha = PasswordField("Senha", validators=[
        DataRequired(),
        Length(min=5, max=25)
    ])
    confirmacao_senha = PasswordField("Confirme a senha", validators=[
        DataRequired(),
        Length(min=5, max=25),
        EqualTo('senha'),
    ])
    cadastrar = SubmitField('Inscreva-se')


class LoginForm(FlaskForm):
    email = StringField('E-mail', [
        Email(),
        DataRequired(),
        Length(min=8, max=40),
    ])
    senha = PasswordField('Senha', [
        DataRequired(),
        Length(min=5, max=25),
    ])
    sessao = BooleanField('Manter conectado')
    enviar = SubmitField('Login')

# views

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

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('cadastro.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and  form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


# models

class Pais(db.Model):
    __tablename__ = 'pais'
    id_pais = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_pais = db.Column(db.String(65), nullable=False, unique=True)

    def __repr__(self):
        return "<País: %r>" % self.nome_pais

class Cidade(db.Model):
    __tablename__ = 'cidade'
    id_cidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_cidade = db.Column(db.String(50), nullable=False, unique=True)

    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id_pais'), nullable=False)
    pais = db.relationship('pais', backref=db.backref('cidade', lazy=True))

    def __repr__(self):
        return "<Cidade: %r>" % self.nome_cidade

class Equipe(db.Model):
    __tablename__ = 'equipe'
    id_equipe = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_equipe = db.Column(db.String(50), nullable=False, unique=True)
    nome_oficial = db.Column(db.String(125), nullable=False, unique=True)
    numero_titulos = db.Column(db.Integer)
    nr_voltas_mais_rapidas = db.Column(db.Integer)
    nr_pole_positions = db.Column(db.Integer)
    unidade_potencia = db.Column(db.String(75))
    chassi = db.Column(db.String(15))
    melhor_resultado = db.Column(db.String(25))

    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    cidade = db.relationship('cidade', backref=db.backref('equipe', lazy=True))

    def __repr__(self):
        return "<Equipe: %r>" % self.nome_equipe

class Circuito(db.Model):
    __tablename__ = 'circuito'
    id_circuito = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_circuito = db.Column(db.String(100), unique=True, nullable=False)
    percurso = db.Column(db.Integer)
    numero_voltas = db.Column(db.Integer)
    distancia_total = db.Column(db.Integer)
    primeira_corrida = db.Column(db.Integer)
    piloto_recorde_pista = db.Column(db.String(50))
    ano_recorde_pista = db.Column(db.Integer)
    tempo_recorde_pista = db.Column(db.Time)

    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    cidade = db.relationship('cidade', backref=db.backref('circuito', lazy=True))

    def __repr__(self):
        return "<Circuito: %r>" % self.nome_circuito

class Evento(db.Model):
    __tablename__ = 'evento'
    id_evento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_evento = db.Column(db.String, nullable=True, unique=True)
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)

    id_circuito = db.Column(db.Integer, db.ForeignKey('circuito.id_circuito'), nullable=False)
    circuito = db.relationship('circuito', backref=db.backref('evento', lazy=True))

    def __repr__(self):
        return "<Evento: %r>" % self.nome_evento

class Resultados(db.Model):
    __tablename__ = 'resultados'
    id_resultado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    posicao = db.Column(db.Integer)
    pontuacao_corrida = db.Column(db.Integer)

    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id_evento'), nullable=False)
    evento = db.relationship('evento', backref=db.backref('resultados', lazy=True))

    def __repr__(self):
        return "<Resultado: %r - %r>" % (self.evento.nome_evento, self.posicao)

class Piloto(db.Model):
    __tablename__ = 'piloto'
    id_piloto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_piloto = db.Column(db.String(100), unique=True, nullable=False)
    pontos_ganhos = db.Column(db.Integer, default=0)
    data_nasc = db.Column(db.Date)
    numero_piloto = db.Column(db.Integer)
    corridas_disputadas = db.Column(db.Integer)
    numero_podios = db.Column(db.Integer)
    numero_titulos = db.Column(db.Integer, default=0)
    melhor_resultado = db.Column(db.String(30))

    id_equipe = db.Column(db.Integer, db.ForeignKey('equipe.id_equipe'), nullable=False)
    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)

    equipe = db.relationship('equipe', backref=db.backref('piloto', lazy=True))
    cidade = db.relationship('cidade', backref=db.backref('piloto', lazy=True))

    def __repr__(self):
        return "<Piloto: %r>" % self.nome_piloto

class Resultado_Piloto(db.Model):
    __tablename__ = 'resultado_piloto'
    id_resultado_piloto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_resultado = db.Column(db.Integer, db.ForeignKey('resultados.id_resultado'),
                             nullable=False)
    id_piloto = db.Column(db.Integer, db.ForeignKey('piloto.id_piloto'),
                             nullable=False)

    resultado = db.relationship('resultados', backref=db.backref('resultado_piloto', lazy=True))
    piloto = db.relationship('piloto', backref=db.backref('resultado_piloto', lazy=True))
