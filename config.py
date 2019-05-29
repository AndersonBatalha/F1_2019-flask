import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'zRJAtM7VBAs2QtO2Hx5lYdBuHzVOiwzp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')

    # Flask-Mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'andersonpbatalha@gmail.com'
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = '"F1" <noreply@example.com>'

    # Flask-User
    USER_APP_NAME = "F1 App"
    USER_ENABLE_EMAIL = True
    USER_ENABLE_USERNAME = False
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"

    DEBUG = True

    @staticmethod
    def init_app(app):
        pass
