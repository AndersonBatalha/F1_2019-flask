from app import db
from . import Circuito

class Evento(db.Model):
    __tablename__ = 'evento'
    id_evento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_evento = db.Column(db.String, nullable=True, unique=True)
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)

    id_circuito = db.Column(db.Integer, db.ForeignKey('circuito.id_circuito'), nullable=False)
    circuito = db.relationship(Circuito, backref=db.backref('evento', lazy=True))

    def __repr__(self):
        return "<Evento: %r>" % self.nome_evento

