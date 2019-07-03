from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RoleForm(FlaskForm):
    nome_funcao = StringField('Função', [
        DataRequired(),
        Length(min=3, max=50),
    ])
    enviar = SubmitField('OK')