# TODO
## Permitir que o usuário adicione e edite notícias, que serão exibidas na página inicial (X)
## Permitir que usuários possam seguir outros usuários (X)
## Permitir que usuários comentem nas postagens de outros usuários (X)
## Permissões de usuário (X)
## O site deve ter páginas com acesso restrito a usuários autenticados (X)
## O site deve possuir o gerenciamento de grupos ou funções de usuários
## O site deve ter páginas com acesso restrito a usuários com funções específicas


from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

