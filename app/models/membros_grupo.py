from app import db
from . import Usuario, Grupo

class MembrosGrupo(db.Model):
    __tablename__ = 'membros_grupo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    membro = db.relationship(Usuario, backref=db.backref('membros_grupo', lazy=True))

    id_grupo = db.Column(db.Integer, db.ForeignKey('grupo.id_grupo'))
    grupo = db.relationship(Grupo, backref=db.backref('membros_grupo', lazy=True, cascade='all,delete'))

    def __repr__(self):
        return "%s - %s" %(self.grupo.nome_grupo, self.membro.nome_usuario)