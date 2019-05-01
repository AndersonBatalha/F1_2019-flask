class Circuito(db.Model):
    __tablename__ = 'circuito'
    id_circuito = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_circuito = db.Column(db.String(100), unique=True, nullable=False)
    percurso = db.Column(db.Integer)
    numero_voltas = db.Column(db.Integer)
    distancia_total = db.Column(db.Integer)
    primeira_corrida = db.Column(db.Integer)
    piloto_recorde_pista = db.Column(db.String(50))
    ano_recorde_pista = db.Column(db.Integer)
    tempo_recorde_pista = db.Column(db.Time)

    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    cidade = db.relationship(Cidade, backref=db.backref('circuito', lazy=True))

    def __repr__(self):
        return "<Circuito: %r>" % self.nome_circuito
