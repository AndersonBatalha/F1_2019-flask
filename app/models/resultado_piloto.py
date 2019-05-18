from app import db
from .pontuacao import Pontuacao
from .piloto import Piloto
from .evento import Evento

class Resultado_Piloto(db.Model):
    __tablename__ = 'resultado_piloto'
    id_resultado_piloto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_resultado = db.Column(db.Integer, db.ForeignKey('pontuacao.id_resultado'))
    id_piloto = db.Column(db.Integer, db.ForeignKey('piloto.id_piloto'))
    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id_evento'))

    resultado = db.relationship(Pontuacao, backref=db.backref('resultado_piloto', lazy=True))
    piloto = db.relationship(Piloto, backref=db.backref('resultado_piloto', lazy=True))
    evento = db.relationship(Evento, backref=db.backref('resultado_piloto', lazy=True))

    def __repr__(self):
        return "\n%s\n%d - %d pontos\nGrande Prêmio: %s" %(self.piloto.nome_piloto,
                                                    self.resultado.posicao,
                                       self.resultado.pontuacao_corrida, self.evento.local)
