from flask import Flask
from flask_babelex import Babel
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_user import UserManager

from config import Config

bootstrap = Bootstrap()
db = SQLAlchemy()
config = Config()
login_manager = LoginManager()
babel = Babel()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    config.init_app(app)

    bootstrap.init_app(app)

    db.init_app(app)

    babel.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'main.login'
    login_manager.login_message = "É preciso fazer login para continuar"
    login_manager.login_message_category = 'warning'

    from app.models import Usuario

    user_manager = UserManager(app, db, Usuario)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .main.views.errors import not_authorized, page_not_found
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, not_authorized)

    return app

