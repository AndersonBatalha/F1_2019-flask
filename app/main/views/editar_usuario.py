from app import db
from app.main import main
from app.main.decorators import tem_permissao
from populate_db import Permissoes
from app.models import Usuario, Funcao
from ..forms import EditUserForm
from flask import redirect, url_for, render_template, flash, request
from flask_login import login_required
from populate_db import Populate_DB

@main.route('/editar/<u>', methods=['GET', 'POST'])
@tem_permissao(Permissoes.ADMINISTRAR + Permissoes.EDITAR,
               msg_erro="Apenas administradores podem editar perfis de usuário")
@login_required
def editar_usuario(u):
    usuario = Usuario.query.filter_by(nome_usuario=u).first()
    form = EditUserForm(usuario=usuario)
    if form.validate_on_submit():
        if request.method == 'POST' and (
            form.nome.data != request.form['nome'] or \
            form.nome.data != request.form['nome'] or \
            form.nome_usuario.data != request.form['nome_usuario'] or \
            form.email.data != request.form['email'] or \
            form.data_nasc.data != request.form['data_nasc'] or \
            form.endereco.data != request.form['endereco'] or \
            form.numero.data != request.form['numero'] or \
            form.complemento.data != request.form['complemento'] or \
            form.bairro.data != request.form['bairro'] or \
            form.cidade.data != request.form['cidade'] or \
            form.estado.data != request.form['estado'] or \
            form.pais.data != request.form['pais'] or \
            form.funcao.data != int(request.form['funcao'])
        ):

                usuario.nome = form.nome.data = request.form['nome']
                usuario.nome_usuario = form.nome_usuario.data = request.form['nome_usuario']
                usuario.email = form.email.data = request.form['email']
                dia, mes, ano = str(request.form['data_nasc'])[8:10], \
                str(request.form['data_nasc'])[5:7], \
                str(request.form['data_nasc'])[0:4]
                usuario.data_nasc = form.data_nasc.data = \
                    Populate_DB().str_to_date(dia=dia, mes=mes, ano=ano)
                usuario.endereco = form.endereco.data = request.form['endereco']
                usuario.numero = form.numero.data = request.form['numero']
                usuario.complemento = form.complemento.data = request.form['complemento']
                usuario.bairro = form.bairro.data = request.form['bairro']
                usuario.cidade = form.cidade.data = request.form['cidade']
                usuario.estado = form.estado.data = request.form['estado']
                usuario.pais = form.pais.data = request.form['pais']
                usuario.id_funcao = form.funcao.data = int(request.form['funcao'])
                usuario.funcao = Funcao.query.get(form.itemSelecionado(form.funcao.data))

                db.session.commit()

                flash('As informações do usuário \'%s\' foram alteradas.' %(usuario.nome_usuario),
                      category='info')

                return redirect(url_for('main.listar_usuarios'))
    elif form.errors:
        flash('Verifique as informações inseridas!', category='warning')

    return render_template('forms/editar_usuario.html', form=form)
