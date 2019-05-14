from app import db
from .pais import Pais

class Cidade(db.Model):
    __tablename__ = 'cidade'
    id_cidade = db.Column(db.Integer, primary_key=True)
    nome_cidade = db.Column(db.String(50), nullable=False, unique=True)

    id_pais = db.Column(db.Integer, db.ForeignKey('pais.id_pais'), nullable=False)
    pais = db.relationship(Pais, backref=db.backref('cidade', lazy=True))

    def __repr__(self):
        return "<Cidade: %r>" % (self.nome_cidade)
