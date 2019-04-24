# imports
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField
from wtforms.validators import Email, DataRequired, Length, EqualTo

# config
app = Flask(__name__)
bootstrap = Bootstrap(app)

# forms

app.config['SECRET_KEY'] = 'Z}hrdI2xFMN_xc]'

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
