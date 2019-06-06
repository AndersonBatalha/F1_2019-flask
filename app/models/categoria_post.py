from app import db
from . import Post, Categoria

class Post_Categoria(db.Model):
    __tablename__ = 'post_categoria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_categoria = db.Column(db.Integer, db.ForeignKey('categoria.id_categoria'))
    categoria = db.relationship(Categoria, backref=db.backref('post_categoria', lazy=True))

    id_post = db.Column(db.Integer, db.ForeignKey('post.id_post'))
    post = db.relationship(Post, backref=db.backref('post_categoria', lazy=True))

    def __repr__(self):
        return "%s - %s" %(self.post.titulo, self.categoria.cat)