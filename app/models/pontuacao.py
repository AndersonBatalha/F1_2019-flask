from app import db

class Pontuacao(db.Model):
    __tablename__ = 'pontuacao'
    id_resultado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    posicao = db.Column(db.Integer)
    pontuacao_corrida = db.Column(db.Integer)

    def __repr__(self):
        return "(%d) - %d pontos" % (self.posicao, self.pontuacao_corrida)
