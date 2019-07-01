from app import db

class Funcao(db.Model):

    __tablename__= 'funcao'
    id_funcao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcao = db.Column(db.String(50), nullable=False)
    permissao = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Funcao, self).__init__(*args, **kwargs)
        if self.permissao is None:
            self.apagar_permissoes()

    def __repr__(self):
        return "%s" % self.nome_funcao

    def tem_permissao(self, p):
        return p & self.permissao == p

    def adicionar_permissao(self, p):
        if not self.tem_permissao(p):
            self.permissao += p

    def remover_permissao(self, p):
        if self.tem_permissao(p):
            self.permissao -= p

    def apagar_permissoes(self):
        self.permissao = 0