import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'zRJAtM7VBAs2QtO2Hx5lYdBuHzVOiwzp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass
