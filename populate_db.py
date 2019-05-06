import os, requests, json

from app import db
from app.models import *


class Populate_DB():

    def __init__(self):
        self.url_data = 'https://api.myjson.com/bins/qowkk'

    def json_request(self):
        return requests.get(url=self.url_data).content

    def load_json(self):
        return json.loads(self.json_request(), encoding='utf-8')

    def pais(self, valor):
        r = Pais()
        r.nome_pais = valor
        db.session.add(r)
        db.session.commit()



a = Populate_DB()
data = a.load_json()

corridas = data['calendario_temporada']
equipes = data['equipes']

for corrida in corridas:
    a.pais(corrida['localização']['pais'])
#     print("\n")
#     for i in corrida:
#         if type(corrida[i]).__name__ == 'dict':
#             print(i)
#             for j in corrida[i]:
#                 print('\t', j, ":", corrida[i][j])
#         else:
#             print(i, ":", corrida[i])

