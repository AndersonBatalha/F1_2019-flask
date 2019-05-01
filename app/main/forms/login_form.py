from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired, Length

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