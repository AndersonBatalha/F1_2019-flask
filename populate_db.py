from main import *
import sqlite3, os, requests, json

print("Nome do app: {0}".format(app.name))

if 'data.sqlite' not in os.listdir(BASE_DIR):
    os.system('export FLASK_DEBUG=1 FLASK_ENV=development FLASK_APP={0}.py'.format(app.name))
    os.system('touch data.sqlite')
    os.system('flask db init')
    os.system('flask db migrate')
    os.system('flask db upgrade')

paises = ["Brasil", "Reino Unido", "França", "Finlândia", "Tailândia", "Dinamarca", "Austrália",
          "Canadá", "Alemanha", "Rússia", "Polônia", "Espanha", "Itália", "Países Baixos"]

cidades = {"São Paulo": "Brasil",
           "Stevenage": "Reino Unido",
           "Nastola": "Finlândia",
           "Ufa": "Rússia",
           "Rio de Janeiro": "Brasil",
           "Brasília": "Brasil"}

for pais in paises:
    if sqlite3.IntegrityError:
        pass
    else:
        q = Pais.query.filter_by(nome_pais=pais).first()
        if not q:
            p = Pais(nome_pais=pais)
            db.session.add(p)
            print(p)
        db.session.commit()

print("Inseridos %d registros" %(int(len(paises))))

for cidade, pais in cidades.items():
    if sqlite3.IntegrityError:
        pass
    else:
        p = Pais.query.filter_by(nome_pais=pais).first()
        if p is None:
            p = Pais(nome_pais=pais)
            db.session.add(p)
            db.session.commit()
        c = Cidade(nome_cidade=cidade, pais=p)
        db.session.add(c)
        db.session.commit()
        print(c)

print("Inseridos %d registros" %(int(len(cidades))))

json_data = requests.get('https://my-json-server.typicode.com/AndersonBatalha/json-data/db').content
data = json.loads(json_data)

