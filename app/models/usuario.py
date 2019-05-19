from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .funcao import Funcao

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(125), nullable=False)
    nome_usuario = db.Column(db.String(125), unique=True, nullable=False)
    email = db.Column(db.String(50))
    data_nasc = db.Column(db.Date)
    endereco = db.Column(db.String(150))
    numero = db.Column(db.Integer)
    complemento = db.Column(db.String(75))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(50))
    estado = db.Column(db.String(70))
    pais = db.Column(db.String(45))
    hash_senha = db.Column(db.String(120))

    id_funcao = db.Column(db.Integer, db.ForeignKey('funcao.id_funcao'))
    funcao = db.relationship(Funcao, backref=db.backref('usuario', lazy=True))

    def __repr__(self):
        return "%s" % (self.nome)

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def senha(self, _senha):
        self.hash_senha = generate_password_hash(_senha)

    def check_password(self, senha):
        return check_password_hash(self.hash_senha, senha)


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))