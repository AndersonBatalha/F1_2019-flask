from app.main import main
from app.main.forms import RegisterForm
from flask import redirect, url_for, render_template, flash
from app import db
from app.models import Usuario, Funcao


@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegisterForm()
    if form.validate_on_submit():
        usuario = Usuario(
            nome=form.nome.data,
            nome_usuario=form.nome_usuario.data,
            email=form.email.data,
            data_nasc=form.data_nasc.data,
            endereco=form.endereco.data,
            numero=form.numero.data,
            complemento=form.complemento.data,
            bairro=form.bairro.data,
            cidade=form.cidade.data,
            estado=form.estado.data,
            pais=form.pais.data,
            funcao = Funcao.query.get(form.itemSelecionado(form.funcao.data)),
            senha=form.senha.data,
        )

        db.session.add(usuario)
        db.session.commit()

        flash('Usuário registrado!', category='success')

        return redirect(url_for('main.login'))
    elif form.errors:
        flash('Verifique as informações inseridas!', category='warning')

    return render_template('forms/cadastro.html', form=form)
