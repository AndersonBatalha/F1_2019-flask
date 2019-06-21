from app import db
from . import Usuario


class Relacionamento(db.Model):
    __tablename__ = 'relacionamento'
    id_relacionamento = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship(Usuario, foreign_keys=[id_usuario])

    id_seguidor = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    seguidor = db.relationship(Usuario, foreign_keys=[id_seguidor])

    seguindo = db.Column(db.Boolean)

    def __init__(self, *args, **kwargs):
        super(Relacionamento, self).__init__(*args, **kwargs)
        self.seguindo = True

    def __repr__(self):
        return "%s segue %s" % (self.usuario.nome_usuario, self.seguidor.nome_usuario)

    def existe_relacionamento(self, A, B):
        return Relacionamento().query.filter_by(usuario=A, seguidor=B).first() != None

"""

from app.models import *
from app import db
a = Usuario.query.get(30)
b = Usuario.query.get(80)
r = Relacionamento(usuario=a, seguidor=b)
r
"""