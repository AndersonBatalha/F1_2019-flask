# TODO
## Permitir que o usuário adicione e edite notícias, que serão exibidas na página inicial (X)
## Permitir que usuários possam seguir outros usuários (X)
## Permitir que usuários comentem nas postagens de outros usuários (X)
## Permissões de usuário (X)
## Deve possuir um padrão de apresentação, com cabeçalho e rodapé, que se repete em todas as
## páginas; (X)
## Deve utilizar algum framework CSS, como Bootstrap, SemanticUI, ou outro framework a sua
## escolha; (X)
## Uma das páginas deve apresentar um formulário funcional para inserção de dados,
## com armazenamento em um banco de dados. (X)
## A página principal deve conter diversos blocos de conteúdo, para facilitar o acesso às demais
## páginas. (X)
## O site deve ter uma funcionalidade de cadastro de usuário (X)
## O site deve ter uma funcionalidade de autenticação (X)
## O site deve ter páginas com acesso restrito a usuários autenticados (X)
## O site deve possuir o gerenciamento de grupos ou funções de usuários (X)
## O site deve ter páginas com acesso restrito a usuários com funções específicas (X)
## Permitir que o usuário com função de moderador possa excluir comentários (X)


from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

