from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
from app.models import Funcao

class EditUserForm(FlaskForm):
    nome = StringField('Nome completo', validators=[
        DataRequired(),
        Length(min=3, max=40)
    ])
    nome_usuario = StringField('Nome de usuário', validators=[
        DataRequired(),
        Length(min=3, max=50)
    ])
    email = StringField('E-mail', validators=[
        DataRequired(),
        Length(min=5, max=50)
    ])
    data_nasc = DateField('Data de nascimento')
    endereco = StringField('Endereço', validators=[ DataRequired() ])
    numero = IntegerField('Número', default=0)
    complemento = StringField("Complemento")
    bairro =  StringField("Bairro", validators=[ DataRequired() ])
    cidade = StringField("Cidade", validators=[ DataRequired() ])
    estado = StringField("Estado", validators=[ DataRequired() ])
    pais = StringField("País", validators=[ DataRequired() ])
    funcao = SelectField("Selecione uma função", coerce=int, validators=[ DataRequired() ])
    alterar = SubmitField('OK')

    def __init__(self, usuario, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.choices = [(f.id_funcao, f.nome_funcao) for f in Funcao.query.all()]
        self.usuario = usuario

        self.nome.data = self.usuario.nome
        self.nome_usuario.data = self.usuario.nome_usuario
        self.email.data = self.usuario.email
        self.data_nasc.data = self.usuario.data_nasc
        self.endereco.data = self.usuario.endereco
        self.numero.data = self.usuario.numero
        self.complemento.data = self.usuario.complemento
        self.bairro.data = self.usuario.bairro
        self.cidade.data = self.usuario.cidade
        self.estado.data = self.usuario.estado
        self.pais.data = self.usuario.pais
        self.funcao.data = self.usuario.id_funcao
        self.funcao.choices = self.choices

    def itemSelecionado(self, id):
        return int([tupla[0] for tupla in self.choices if tupla[0]==id][0])
