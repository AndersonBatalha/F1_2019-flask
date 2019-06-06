import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'app/static')


class Config:
    SECRET_KEY = 'zRJAtM7VBAs2QtO2Hx5lYdBuHzVOiwzp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    DEBUG = True

    # diretório onde estarão os uploads feitos pelo usuário
    UPLOAD_FOLDER = os.path.join(STATIC_DIR, 'uploads')
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER) # cria uma pasta para uploads, se não existir

    # extensões permitidas
    ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif'])


    @staticmethod
    def init_app(app):
        pass
