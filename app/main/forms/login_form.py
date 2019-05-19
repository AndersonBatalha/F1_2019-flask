from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    nome_usuario = StringField('Nome de usuário', [
        DataRequired(),
        Length(min=3, max=50),
    ])
    senha = PasswordField('Senha', [
        DataRequired(),
        Length(min=3, max=30),
    ])
    sessao = BooleanField('Manter conectado')
    enviar = SubmitField('Login')