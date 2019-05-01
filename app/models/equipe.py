class Equipe(db.Model):
    __tablename__ = 'equipe'
    id_equipe = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_equipe = db.Column(db.String(50), nullable=False, unique=True)
    nome_oficial = db.Column(db.String(125), nullable=False, unique=True)
    numero_titulos = db.Column(db.Integer)
    nr_voltas_mais_rapidas = db.Column(db.Integer)
    nr_pole_positions = db.Column(db.Integer)
    unidade_potencia = db.Column(db.String(75))
    chassi = db.Column(db.String(15))
    melhor_resultado = db.Column(db.String(25))

    id_cidade = db.Column(db.Integer, db.ForeignKey('cidade.id_cidade'), nullable=False)
    cidade = db.relationship(Cidade, backref=db.backref('equipe', lazy=True))

    def __repr__(self):
        return "<Equipe: %r>" % self.nome_equipe
