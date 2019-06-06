from app import db
from . import Usuario
from slugify import slugify

class Post(db.Model):
    __tablename__ = 'post'
    id_post = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    texto = db.Column(db.String)
    imagem = db.Column(db.String)

    id_autor = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    autor = db.relationship(Usuario, backref=db.backref('post', lazy=True))

    def __repr__(self):
        return "Post: %s"% (str(self.titulo))

    @property
    def slug(self):
        return slugify(self.titulo)