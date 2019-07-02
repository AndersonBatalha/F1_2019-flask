from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired
from app.models import Usuario

class CriarGrupoForm(FlaskForm):
    nome_grupo = StringField("Nome do grupo", validators=[
        DataRequired()
    ])
    desc = TextAreaField("Descreva o grupo")
    usuarios = SelectMultipleField(coerce=int)
    submit = SubmitField('Enviar')

    def __init__(self, *args, **kwargs):
        super(CriarGrupoForm, self).__init__(*args, **kwargs)
        self.membros_grupo = []
        self.usuarios.choices = [(usuario.id, usuario.nome_usuario) for usuario in
                                 Usuario.query.all()]

    def usuarios_selecionados(self):
        for id in self.usuarios.data:
            usuario = Usuario.query.get(id)
            if usuario not in self.membros_grupo:
                self.membros_grupo.append(usuario)

        return self.membros_grupo

