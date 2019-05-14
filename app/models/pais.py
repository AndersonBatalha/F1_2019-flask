from app import db

class Pais(db.Model):
    __tablename__ = 'pais'
    id_pais = db.Column(db.Integer, primary_key=True)
    nome_pais = db.Column(db.String(65), nullable=False, unique=True)

    def __repr__(self):
        return "<País: %d - %r>" % (self.id_pais, self.nome_pais)