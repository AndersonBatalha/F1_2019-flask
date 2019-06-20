from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    comment = TextAreaField("Comentário", validators=[ DataRequired() ])
    submit = SubmitField('Enviar')
