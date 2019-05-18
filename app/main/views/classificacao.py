from app.main import main
from flask import render_template
from app.models import *
from sqlalchemy import select, func, and_
from app import db

@main.route('/classificacao')
def classificacao():
    conn = db.engine.connect()
    query = select([Piloto.nome_piloto, Equipe.nome_equipe, Piloto.flag_icon,
                    func.sum(Pontuacao.pontuacao_corrida).label('total_pontos')]) \
        .where(and_(Piloto.id_piloto == Resultado_Piloto.id_piloto,
                    Evento.id_evento == Resultado_Piloto.id_evento,
                    Pontuacao.id_resultado == Resultado_Piloto.id_resultado,
                    Piloto.id_equipe == Equipe.id_equipe)) \
        .group_by(Piloto.nome_piloto) \
        .order_by(func.sum(Pontuacao.pontuacao_corrida).desc())
    res = conn.execute(query).fetchall()

    q = select([Equipe.nome_equipe, Equipe.flag_icon,
                func.sum(Pontuacao.pontuacao_corrida).label('total_pontos')]) \
        .where(and_(Piloto.id_piloto == Resultado_Piloto.id_piloto,
                    Evento.id_evento == Resultado_Piloto.id_evento,
                    Pontuacao.id_resultado == Resultado_Piloto.id_resultado,
                    Piloto.id_equipe == Equipe.id_equipe)) \
        .group_by(Equipe.nome_equipe) \
        .order_by(func.sum(Pontuacao.pontuacao_corrida).desc())
    r = conn.execute(q).fetchall()

    return render_template('classificacao.html', classificacao=res, classificacao_=r)
