from app import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

#TODO
# Permitir que usuários possam seguir outros usuários
# Permitir que usuários comentem nas postagens de outros usuários