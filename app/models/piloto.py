from app import db
from . import Equipe, Cidade

class Piloto(db.Model):
    __tablename__ = 'piloto'
    id_piloto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_piloto = db.Column(db.String(100), unique=True, nullable=False)
    pontos_ganhos = db.Column(db.Integer, default=0)
    data_nasc = db.Column(db.Date)
    numero_piloto = db.Column(db.Integer)
    corridas_disputadas = db.Column(db.Integer)
    numero_podios = db.Column(db.Integer)
    numero_titulos = db.Column(db.Integer, default=0)
    melhor_resultado = db.Column(db.String(30))

    id_equipe = db.Column(db.Integer, db.ForeignKey('equipe.id_equipe'), nullable=False)
    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)

    equipe = db.relationship(Equipe, backref=db.backref('piloto', lazy=True))
    cidade = db.relationship(Cidade, backref=db.backref('piloto', lazy=True))

    def __repr__(self):
        return "<Piloto: %r>" % self.nome_piloto
