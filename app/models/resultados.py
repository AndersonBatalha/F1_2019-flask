class Resultados(db.Model):
    __tablename__ = 'resultados'
    id_resultado = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    posicao = db.Column(db.Integer)
    pontuacao_corrida = db.Column(db.Integer)

    id_evento = db.Column(db.Integer, db.ForeignKey('evento.id_evento'), nullable=False)
    evento = db.relationship(Evento, backref=db.backref('resultados', lazy=True))

    def __repr__(self):
        return "<Resultado: %r - %r>" % (self.evento.nome_evento, self.posicao)
