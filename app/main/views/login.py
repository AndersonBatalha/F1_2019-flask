from app.main import main
from ..forms import LoginForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user
from app.models import Usuario

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(nome_usuario=form.nome_usuario.data).first()
        if usuario and usuario.check_password(form.senha.data):
            login_user(usuario, remember=form.sessao.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        else:
            flash("Usuário ou senha inválido!", category='warning')
    return render_template('forms/login.html', form=form)

