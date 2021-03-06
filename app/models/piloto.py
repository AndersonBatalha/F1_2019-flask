from app import db
from . import Equipe, Cidade

class Piloto(db.Model):
    __tablename__ = 'piloto'
    id_piloto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_piloto = db.Column(db.String(100), unique=True, nullable=False)
    slug = db.Column(db.String)
    numero_piloto = db.Column(db.Integer)
    pontos_ganhos = db.Column(db.Integer, default=0)
    data_nasc = db.Column(db.Date)
    corridas_disputadas = db.Column(db.Integer)
    numero_podios = db.Column(db.Integer)
    numero_titulos = db.Column(db.Integer, default=0)
    pos_melhor_resultado = db.Column(db.Integer)
    nr_melhor_resultado = db.Column(db.Integer)
    img = db.Column(db.String(30))
    flag_icon = db.Column(db.String(5))

    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    cidade = db.relationship(Cidade, backref=db.backref('piloto', lazy=True))

    id_equipe = db.Column(db.Integer, db.ForeignKey('equipe.id_equipe'))
    equipe = db.relationship(Equipe, backref=db.backref('piloto', lazy=True))

    def __repr__(self):
        return "%s" % self.nome_piloto
