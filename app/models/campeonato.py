from app import db
from . import Piloto

class Titulo(db.Model):
    __tablename__ = 'titulo'
    id_titulo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ano_titulo = db.Column(db.Integer)

    id_piloto = db.Column(db.Integer, db.ForeignKey('piloto.id_piloto'))
    piloto = db.relationship(Piloto, backref=db.backref('titulo', lazy=True))

    def __repr__(self):
        return "%d" % self.ano_titulo
