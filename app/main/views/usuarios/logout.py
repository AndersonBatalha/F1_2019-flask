from app.main import main
from flask import redirect, url_for, flash
from flask_login import logout_user, login_required

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash("A sessão atual foi encerrada", category='info')
    return redirect(url_for('main.index'))
