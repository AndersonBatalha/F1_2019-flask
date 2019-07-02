from app import db

class Grupo(db.Model):

    __tablename__= 'grupo'
    id_grupo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_grupo = db.Column(db.String(50), nullable=False)
    slug = db.Column(db.String)
    descricao = db.Column(db.String)

    def __repr__(self):
        return "%s" % self.nome_grupo