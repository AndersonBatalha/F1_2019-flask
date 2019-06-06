from app.main import main
from ..forms import RegisterForm
from flask import redirect, url_for, render_template, flash
from app import db
from app.models import Usuario, Funcao

@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegisterForm()
    if form.validate_on_submit():
        usuario = Usuario()
        usuario.nome = form.nome.data
        usuario.nome_usuario = form.nome_usuario.data
        usuario.email = form.email.data
        usuario.data_nasc = form.data_nasc.data
        usuario.endereco = form.endereco.data
        usuario.numero = form.numero.data
        usuario.complemento = form.complemento.data
        usuario.bairro = form.bairro.data
        usuario.cidade = form.cidade.data
        usuario.estado = form.estado.data
        usuario.pais = form.pais.data
        usuario.senha = form.senha.data
        usuario.funcao = Funcao.query.get(form.itemSelecionado(form.funcao.data))

        db.session.add(usuario)
        db.session.commit()

        flash('Usuário registrado!', category='success')

        return redirect(url_for('main.login'))
    elif form.errors:
        flash('Verifique as informações inseridas!', category='warning')

    return render_template('forms/cadastro.html', form=form)
