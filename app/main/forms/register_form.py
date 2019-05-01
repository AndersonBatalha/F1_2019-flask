from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo

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