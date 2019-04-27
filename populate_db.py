import sqlalchemy

from views import *
import sqlite3, os

if 'data.sqlite' not in os.listdir(BASE_DIR):
    os.system('touch data.sqlite')
    os.system('flask db init')
    os.system('flask db migrate')
    os.system('flask db upgrade')

paises = ["Brasil", "Reino Unido", "França", "Finlândia", "Tailândia", "Dinamarca", "Austrália",
          "Canadá", "Alemanha", "Rússia", "Polônia", "Espanha", "Itália", "Países Baixos"]

cidades = {"São Paulo": "Brasil",
           "Stevenage": "Reino Unido",
           "Nastola": "Finlândia",
           "Ufa": "Rússia"}

for pais in paises:
    q = Pais.query.filter_by(nome_pais=pais).first()
    if not q:
        p = Pais(nome_pais=pais)
        db.session.add(p)
    try:
        db.session.commit()
    except sqlite3.IntegrityError:
        pass

print("Inseridos %d registros" %(int(len(paises))))

for cidade, pais in cidades.items():
    p = Pais.query.filter_by(nome_pais=pais).first()
    if p is None:
        p = Pais(nome_pais=pais)
        db.session.add(p)
        db.session.commit()
    c = Cidade(nome_cidade=cidade, pais=p)
    db.session.add(c)
    try:
        db.session.commit()
    except sqlite3.IntegrityError:
        pass

