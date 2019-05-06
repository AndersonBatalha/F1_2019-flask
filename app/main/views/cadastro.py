from app.main import main
from ..forms import RegisterForm
from flask import request, redirect, url_for, render_template

@main.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('cadastro.html', form=form)
