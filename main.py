# TODO
## Permitir que o usuário adicione e edite notícias, que serão exibidas na página inicial (X)
## Permitir que usuários possam seguir outros usuários (X)
## Permitir que usuários comentem nas postagens de outros usuários (X)
## Permissões de usuário

from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

