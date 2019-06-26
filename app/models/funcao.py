from app import db

class Permissoes:
    ADMINISTRADOR = 0
    MODERAR = 1
    COMENTAR = 2
    SEGUIR = 3
    POSTAR = 4

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
        funcoes = {
            "Usuário": [
                Permissoes.COMENTAR,
                Permissoes.SEGUIR,
                Permissoes.POSTAR
            ],
            "Moderador": [
                Permissoes.MODERAR,
                Permissoes.COMENTAR,
                Permissoes.SEGUIR,
                Permissoes.POSTAR
            ],
            "Administrador": [
                Permissoes.ADMINISTRADOR,
                Permissoes.MODERAR,
                Permissoes.COMENTAR,
                Permissoes.SEGUIR,
                Permissoes.POSTAR
            ]
        }
        for (f, permissoes) in funcoes.items():
            funcao = Funcao.query.filter_by(nome_funcao=f).first()
            if funcao == None:
                funcao = Funcao()
                funcao.nome_funcao = f
            funcao.apagar_permissoes()

            for p in permissoes:
                funcao.adicionar_permissao(p)
            db.session.add(funcao)
            db.session.commit()
            print(funcao, funcao.permissoes)

    def remover_funcoes(self):
        for item in Funcao.query.all():
            db.session.delete(item)
            db.session.commit()
