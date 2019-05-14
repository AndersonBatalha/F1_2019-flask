import requests, json, os, datetime
from sqlalchemy.exc import IntegrityError

from config import Config, BASE_DIR
from app.models import *
from main import create_app
from app import db

class Populate_DB():
    def __init__(self):
        self.url_data = 'https://api.myjson.com/bins/131uha'
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

    def str_to_time(self, hora, minuto, segundo, milissegundo):
        self.hora = 0
        self.minuto = minuto
        self.segundo = segundo
        self.milissegundo = milissegundo

        return datetime.time(hour=self.hora, minute=self.minuto, second=self.segundo,
                             microsecond=self.milissegundo)

    def str_to_date(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

        return datetime.date(int(ano), int(mes), int(dia))

    def pais(self, **kwargs):
        r = Pais.query.filter_by(nome_pais=kwargs['pais']).first()
        if r is None:
            r = Pais()
            r.nome_pais = kwargs['pais']
        db.session.add(r)
        db.session.commit()
        print(r)
        return r

    def cidade(self, **kwargs):
        r = Cidade.query.filter_by(nome_cidade=kwargs['cidade']).first()
        if r is None:
            r = Cidade()
            r.nome_cidade = kwargs['cidade']
            r.pais = self.pais(**kwargs)
        db.session.add(r)
        db.session.commit()
        print(r)
        return r

    def circuito(self, **kwargs):
        r = Circuito.query.filter_by(nome_circuito=kwargs['nome_circuito']).first()
        if r is None:
            r = Circuito()
            r.nome_circuito = kwargs['nome_circuito']
            r.percurso = kwargs['percurso']
            r.numero_voltas = kwargs['numero_voltas']
            r.distancia_total = kwargs['distancia_total']
            r.primeira_corrida = kwargs['primeira_corrida']
            r.piloto_recorde_pista = kwargs['piloto_recorde']
            r.ano_recorde_pista = kwargs['ano_recorde']
            m, s, ms = int(kwargs['tempo_recorde'][0]), int(kwargs['tempo_recorde'][2:4]), \
                       int(kwargs['tempo_recorde'][5:8])
            r.tempo_recorde_pista = self.str_to_time(0, m, s, ms)
            r.cidade = self.cidade(**kwargs)
        db.session.add(r)
        db.session.commit()
        print(r)
        return r

    def evento(self, **kwargs):
        r = Evento.query.filter_by(nome_evento=kwargs['nome_oficial_evento']).first()
        if r is None:
            r = Evento()
            r.nome_evento = kwargs['nome_oficial_evento']
            d, M, A = kwargs['data_inicio'][0:2], kwargs['data_inicio'][3:5], \
                      kwargs['data_inicio'][6:]
            r.data_inicio = self.str_to_date(d, M, A)
            d, M, A = kwargs['data_termino'][0:2], kwargs['data_termino'][3:5], \
                      kwargs['data_termino'][6:]
            r.data_termino = self.str_to_date(d, M, A)

            r.circuito = self.circuito(**kwargs)

        db.session.add(r)
        db.session.commit()
        print(r)
        return r

    def equipe(self, **kwargs):
        r = Equipe.query.filter_by(nome_equipe=kwargs['equipe']).first()
        if r is None:
            r = Equipe()
            r.nome_equipe = kwargs['equipe']
            r.nome_oficial = kwargs['nome_oficial']
            r.numero_titulos = kwargs['titulos_mundiais']
            r.nr_voltas_mais_rapidas = kwargs['voltas_mais_rapidas']
            r.nr_pole_positions = kwargs['pole_positions']
            r.unidade_potencia = kwargs['unidade_potencia']
            r.chassi = kwargs['chassis']
            r.posicao_melhor_resultado = kwargs['posicao']
            r.nr_melhor_resultado = kwargs['quantidade']

            r.cidade = self.cidade(**kwargs)

        db.session.add(r)
        db.session.commit()
        print(r)
        return r

    def piloto(self, **kwargs):
        r = Piloto.query.filter_by(nome_piloto=kwargs['nome']).first()
        if r is None:
            r = Piloto()
            r.nome_piloto = kwargs['nome']
            r.numero_piloto = kwargs['#']
            r.pontos_ganhos = kwargs['pontos_ganhos']
            dia, mes, ano = kwargs['data_nascimento'][0:2], kwargs['data_nascimento'][3:5], \
                      kwargs['data_nascimento'][6:]
            r.data_nasc = self.str_to_date(dia, mes, ano)
            r.corridas_disputadas = kwargs['gps_disputados']
            r.numero_podios = kwargs['podios']
            r.numero_titulos = kwargs['nr_titulos']
            r.pos_melhor_resultado = kwargs['posicao']
            r.nr_melhor_resultado = kwargs['quantidade']

            r.cidade = self.cidade(**kwargs)
            r.equipe = self.equipe(**kwargs)

        print(r)
        return r

if __name__ == '__main__':

    os.system("rm -rf migrations/ data.sqlite")

    a = Populate_DB()
    a.app_config()
    a.db_config()
    data = a.load_json()

    corridas = data.get('calendario_temporada')
    equipes = data.get('equipes')
    pilotos = data.get('pilotos')

    kwargs = {}

    print("\n\nCorridas")
    for corrida in corridas:
        for i in corrida:
            if type(corrida[i]).__name__ == 'dict':
                for j in corrida[i]:
                    kwargs[j] = corrida[i][j]
            else:
                kwargs[i] = corrida[i]
        a.pais(**kwargs)
        a.cidade(**kwargs)
        a.circuito(**kwargs)
        a.evento(**kwargs)

    kwargs = {}

    print("\n\nEquipes")
    for equipe in equipes:
        for i in equipe:
            if type(equipe[i]).__name__ == 'dict':
                for j in equipe[i]:
                    kwargs[j] = equipe[i][j]
            else:
                kwargs[i] = equipe[i]
        a.pais(**kwargs)
        a.cidade(**kwargs)
        a.equipe(**kwargs)

    kwargs = {}

    print("\n\nPilotos")
    for piloto in pilotos:
        for i in piloto:
            if type(piloto[i]).__name__ == 'dict':
                for j in piloto[i]:
                    kwargs[j] = piloto[i][j]
            else:
                kwargs[i] = piloto[i]
        a.pais(**kwargs)
        a.cidade(**kwargs)
        a.equipe(**kwargs)
        a.piloto(**kwargs)
