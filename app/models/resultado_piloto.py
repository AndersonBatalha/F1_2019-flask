from app import db
from .resultados import Resultados
from .piloto import Piloto

class Resultado_Piloto(db.Model):
    __tablename__ = 'resultado_piloto'
    id_resultado_piloto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_resultado = db.Column(db.Integer, db.ForeignKey('resultados.id_resultado'),
                             nullable=False)
    id_piloto = db.Column(db.Integer, db.ForeignKey('piloto.id_piloto'),
                             nullable=False)

    resultado = db.relationship(Resultados, backref=db.backref('resultado_piloto', lazy=True))
    piloto = db.relationship(Piloto, backref=db.backref('resultado_piloto', lazy=True))
