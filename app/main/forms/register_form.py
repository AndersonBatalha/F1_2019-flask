from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from app.models import Funcao

class RegisterForm(FlaskForm):
    nome = StringField('Nome completo', validators=[
        DataRequired(),
        Length(min=5, max=40)
    ])
    nome_usuario = StringField('Nome de usuário', validators=[
        DataRequired(),
        Length(min=5, max=25)
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
    funcao = SelectField("Selecione uma função", coerce=int)
    confirmacao_senha = PasswordField("Confirme a senha", validators=[
        DataRequired(),
        Length(min=5, max=25),
        EqualTo('senha'),
    ])
    cadastrar = SubmitField('Inscreva-se')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.choices = [(f.id_funcao, f.nome_funcao) for f in Funcao.query.all()]

        self.funcao.choices = self.choices
