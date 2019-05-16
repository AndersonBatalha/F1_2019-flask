from app import db
from . import Circuito

class Evento(db.Model):
    __tablename__ = 'evento'
    id_evento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_evento = db.Column(db.String, nullable=True, unique=True)
    local = db.Column(db.String)
    data_inicio = db.Column(db.Date)
    data_termino = db.Column(db.Date)
    url = db.Column(db.String)
    img_evento = db.Column(db.String)
    flag_icon = db.Column(db.String(5))

    id_circuito = db.Column(db.Integer, db.ForeignKey('circuito.id_circuito'), nullable=False)
    circuito = db.relationship(Circuito, backref=db.backref('evento', lazy=True))

    def __repr__(self):
        return "%s" % self.nome_evento

