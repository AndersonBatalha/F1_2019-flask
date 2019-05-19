from app import db

class Funcao(db.Model):
    __tablename__= 'funcao'
    id_funcao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcao = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "%s" % self.nome_funcao