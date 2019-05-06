from app.main import main
from ..forms import LoginForm
from flask import request, render_template, redirect, url_for

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)

