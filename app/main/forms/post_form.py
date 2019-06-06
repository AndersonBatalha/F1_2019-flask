from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    titulo = StringField("Título do post", validators=[
        DataRequired()
    ])
    texto = TextAreaField("Texto")
    imagem = FileField('Arquivo de imagem')
    submit = SubmitField('Enviar')

