from app import db

class Permissoes:
    ADMINISTRADOR = 0
    MODERADOR = 1
    COMENTAR = 2
    SEGUIR = 3

class Funcao(db.Model):
    __tablename__= 'funcao'
    id_funcao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_funcao = db.Column(db.String(50), nullable=False)
    permissoes = []

    def __repr__(self):
        return "%s" % self.nome_funcao

    def tem_permissao(self, p):
        return p in self.permissoes

    def adicionar_permissao(self, p):
        if not self.tem_permissao(p):
            self.permissoes.append(p)

    def remover_permissao(self, p):
        if self.tem_permissao(p):
            self.permissoes.remove(p)

    def apagar_permissoes(self):
        self.permissoes.clear()

    def permissoes_(self):
        return self.permissoes

    def inserir_funcoes(self):
        f = {
            "Usuário": [
                Permissoes.COMENTAR,
                Permissoes.SEGUIR
            ],
            "Moderador": [
                Permissoes.MODERADOR,
                Permissoes.COMENTAR,
                Permissoes.SEGUIR
            ],
            "Administrador": [
                Permissoes.ADMINISTRADOR,
                Permissoes.MODERADOR,
                Permissoes.COMENTAR,
                Permissoes.SEGUIR
            ]
        }
        for (funcao, permissoes) in f.items():
            funcao = Funcao.query.filter_by(nome_funcao=funcao).first()
            if not funcao:
                funcao = Funcao(nome_funcao=funcao)
            funcao.apagar_permissoes()
            for p in permissoes:
                funcao.adicionar_permissao(p)

            db.session.add(funcao)
            db.session.commit()

