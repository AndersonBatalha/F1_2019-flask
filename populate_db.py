import requests, json, os

from config import Config, BASE_DIR
from app.models import *
from main import create_app
from app import db

class Populate_DB():

    def __init__(self):
        self.url_data = 'https://api.myjson.com/bins/1d3eis'
        self.app = create_app()
        self.arquivos = os.listdir(BASE_DIR)

    def json_request(self):
        return requests.get(url=self.url_data).content

    def load_json(self):
        return json.loads(self.json_request(), encoding='utf-8')

    def app_config(self):
        self.app.app_context().push()
        self.app.config.from_object(Config)

    def db_config(self):
        db.init_app(self.app)
        db.create_all()

        if 'migrations' not in self.arquivos:
            os.system("""touch data.sqlite &&
export FLASK_APP=main.py && 
flask db init &&
flask db migrate &&
flask db downgrade""")

    def pais(self, **kwargs):
        r = Pais.query.filter_by(nome_pais=kwargs['pais']).first()
        if r:
            return r
        else:
            r = Pais()
            r.nome_pais = kwargs['pais']
            db.session.add(r)
            db.session.commit()
        print(r)

    def cidade(self, **kwargs):
        r = Cidade.query.filter_by(nome_cidade=kwargs['cidade']).first()
        if r:
            return r
        else:
            r = Cidade()
            r.nome_cidade = kwargs['cidade']
            r.pais = self.pais(**kwargs)
            db.session.add(r)
            db.session.commit()
        print(r)

if __name__ == '__main__':

    a = Populate_DB()
    a.app_config()
    a.db_config()
    data = a.load_json()

    corridas = data['calendario_temporada']
    equipes = data['equipes']

    for corrida in corridas:
        kwargs = {}

        for i in corrida:
            if type(corrida[i]).__name__ == 'dict':
                for j in corrida[i]:
                    kwargs[j] = corrida[i][j]
            else:
                kwargs[i] = corrida[i]

        a.pais(**kwargs)
        a.cidade(**kwargs)