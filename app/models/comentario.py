from app import db
from . import Post, Usuario

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id_comentario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    texto = db.Column(db.String)
    data = db.Column(db.DateTime)

    id_post = db.Column(db.Integer, db.ForeignKey('post.id_post'), nullable=False)
    post = db.relationship(Post, backref=db.backref('comentario', lazy=True, cascade='all,delete'))

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    autor = db.relationship(Usuario, backref=db.backref('comentario', lazy=True))

    def __repr__(self):
        return "%s" % self.texto
