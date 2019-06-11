from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired

class EditPostForm(FlaskForm):
    titulo = StringField("Título do post", validators=[
        DataRequired()
    ])
    texto = TextAreaField("Texto")
    imagem = FileField('Arquivo de imagem')
    submit = SubmitField('Enviar')

    def __init__(self, post, *args, **kwargs):
        super(EditPostForm, self).__init__(*args, **kwargs)
        self.post = post

        self.titulo.data = self.post.titulo
        self.texto.data = self.post.texto
        self.imagem.data = self.post.imagem
